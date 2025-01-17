# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter, QMessageBox, QSizePolicy  
from PySide6.QtCore import QTimer, QTime, QDate, Qt, QStringListModel
from PySide6.QtGui import QPixmap, QPainter, QBrush
import requests
from datetime import datetime
import os
import sys
import json
from geopy.distance import geodesic
import requests
import json
from sklearn.neighbors import BallTree
import numpy as np
import requests
from geopy.distance import geodesic
import pycountry
from collections import Counter
import PySide6.QtCharts as QtCharts

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
# from PyQt5 import uic
API_key = ""

class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.cached_location = None
		self.lat = None
		self.lon = None
		self.hours = []
		self.temperatures = []
		self.chart = QtCharts.QChart()

		self.ui.progressBar.setVisible(False)
		self.ui.graph_widget.hide()
		self.ui.frame_11.hide()

		# Prompt app info
		self.ui.app_info_button.clicked.connect(self.show_app_info)
		self.ui.refresh_button.clicked.connect(self.refresh_data)
		# Get input
		# current location
		self.ui.toolButton.clicked.connect(self.current_position)
		# search location
		self.ui.pushButton.clicked.connect(self.get_input)
		self.ui.lineEdit.returnPressed.connect(self.get_input)
		
		# Setup time and date
		self.timer = QTimer(self)
		self.timer.timeout.connect(self.update_date_and_time)  
		self.timer.start(1000)
		self.update_date_and_time()
		
		city_list = self.load_city_list("formatted_cities.txt")
		self.fill_search(city_list)

	def convert_to_12_hour_format(self, hour):
		hour = int(hour)
		if hour == 0:
			return "12 AM"
		elif hour < 12:
			return f"{hour} AM"
		elif hour == 12:
			return "12 PM"
		else:
			return f"{hour - 12} PM"

	def draw_graph(self):
		self.ui.graph_widget.show()
		if hasattr(self, 'chartView') and self.chartView is not None:
			self.chartView.deleteLater()  # Remove the old chart view from memory

		# Clear the previous chart series (in case the chart object is reused)
		self.chart.removeAllSeries()
		for axis in self.chart.axes():
			self.chart.removeAxis(axis)
		
		self.series = QtCharts.QLineSeries()
		data = list(zip(self.hours[0:9], self.temperatures[0:9]))

		sorted_data = sorted(data, key=lambda x: float(x[0]))  # Sorting by the hour value

		# Append sorted data to the series
		for hour, temp in sorted_data:
			self.series.append(hour, temp)
	
		# Create the chart and set the title
		
		self.chart.legend().hide()  # Hide the legend
		self.chart.addSeries(self.series)  # Add the data series
		self.chart.setTitle("Weather forecast for every 3 hours")  # Set chart title

		x_axis = QtCharts.QCategoryAxis()
		x_axis.setTitleText("Hour")

		for hour, _ in sorted_data:
			formatted_hour = self.convert_to_12_hour_format(hour)
			x_axis.append(formatted_hour, float(hour)) 

		# Set the custom x-axis to the chart
		self.chart.addAxis(x_axis, Qt.AlignBottom)  # Add the x-axis to the bottom of the chart
		self.series.attachAxis(x_axis)

		# Configure Y-axis (temperatures)
		y_axis = QtCharts.QValueAxis()
		y_axis.setRange(min(self.temperatures) - 5, max(self.temperatures) + 5)  # Add padding to the temperature range
		y_axis.setTitleText("Temperature (°C)")
		self.chart.addAxis(y_axis, Qt.AlignLeft)    # Add the y-axis to the left of the chart
		self.series.attachAxis(y_axis)

		# Create the chart view
		self.chartView = QtCharts.QChartView(self.chart)
		self.chartView.setRenderHint(QPainter.Antialiasing)  
		self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

		# Set a size policy for the chart view
		sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.chartView.sizePolicy().hasHeightForWidth())
		self.chartView.setSizePolicy(sizePolicy)
		self.chartView.setMinimumSize(0, 300)  


		self.chart.setBackgroundBrush(QBrush(Qt.transparent))
		self.chartView.setStyleSheet("background: transparent;")
		self.chart.setPlotAreaBackgroundBrush(QBrush(Qt.transparent))

		self.ui.graph_widget.layout().addWidget(self.chartView)

	def refresh_data(self):
		city, country = self.cached_location
		lat = self.lat
		lon = self.lon
		self.display_data(city, country, lat, lon)

	def show_app_info(self):
		message_box = QMessageBox()
		message_box.setIcon(QMessageBox.Information)
		message_box.setWindowTitle("About This App")
		message_box.setText("This app provides the following functionalities:\n\n1. Display current weather information.\n2. Display nearby cities.\n3. Display weather forecast for each 3 hours/each day for 5 days.")
		message_box.setStandardButtons(QMessageBox.Ok)
		message_box.exec()

	def fill_search(self, city_list):
	# Initialize the model for QCompleter
		self.model = QStringListModel()  
		self.completer = QCompleter(self.model, self)
		self.completer.setCaseSensitivity(Qt.CaseInsensitive)  # Case insensitive matching
		self.completer.setFilterMode(Qt.MatchContains)         # Match any part of the city name
		self.ui.lineEdit.setCompleter(self.completer)

		# Connect textChanged signal to dynamically update QCompleter
		self.ui.lineEdit.textChanged.connect(lambda text: self.update_completer(text, city_list))

	def update_completer(self, input_text, city_list, max_results=20):
		# Filter and limit city_list to improve performance
		filtered_cities = [city for city in city_list if input_text.lower() in city.lower()]
		filtered_cities = filtered_cities[:max_results]  # Limit to top N matches
		
		# Update the model with filtered cities
		self.model.setStringList(filtered_cities)

	def build_ball_tree(self, city_file):
		with open(city_file, 'r', encoding='utf-8') as file:
			cities = json.load(file)

		coordinates = []  # List to store (lat, lon)
		city_names = []   # List to store city names

		for city in cities:
			lat = city['coord']['lat']
			lon = city['coord']['lon']
			coordinates.append((lat, lon))
			city, country = city['name'], city['country']
			city_names.append((city, country))

		# Convert coordinates into numpy array
		coordinates_array = np.array(coordinates)
		tree = BallTree(np.radians(coordinates_array), metric='haversine')  # Use haversine distance
		return tree, city_names, coordinates

	# Find nearest cities using Ball Tree
	def find_nearby_cities_ball_tree(self, lat, lon, tree, city_names, coordinates, max_results):
		lat_lon = np.radians([(lat, lon)])  # Convert target lat-lon to radians
		distances, indices = tree.query(lat_lon, k=max_results + 1)  # +1 to include the target city itself

		nearby_cities = []
		for i, index in enumerate(indices[0]):
			if i == 0:  # Skip the target city itself
				continue

			city_name, country = city_names[index]
			coord = coordinates[index]
			distance = geodesic((lat, lon), coord).kilometers  # Haversine distance
			nearby_cities.append((city_name, country, distance))
		
		return nearby_cities

	def get_valid_nearby_cities(self, lat, lon, city_file, max_results):
		tree, city_names, coordinates = self.build_ball_tree(city_file)

		nearby_cities = self.find_nearby_cities_ball_tree(lat, lon, tree, city_names, coordinates, max_results)

		valid_cities = []
		for city_name, country_name, distance in nearby_cities:
			valid_cities.append((city_name, country_name))
			if len(valid_cities) == max_results:
				break
		return valid_cities[:3]

	def load_city_list(self, file_path):
		try:
			with open(file_path, "r", encoding="utf-8") as file:
				city_list = [line.strip() for line in file if line.strip()]
			return city_list
		except FileNotFoundError:
			print(f"Error: File '{file_path}' not found.")
			return []

	def start_progress(self):
		self.ui.frame_11.show()
		self.ui.progressBar.setVisible(True)

		self.progress_value = 0
		self.ui.progressBar.setValue(self.progress_value)

		self.progress_timer = QTimer(self)
		self.progress_timer.timeout.connect(self.update_progress)
		self.progress_timer.start(100)

	def update_progress(self):
		self.progress_value += 20
		self.ui.progressBar.setValue(self.progress_value)

		if self.progress_value >= 100:
			self.progress_timer.stop()
			self.ui.frame_11.hide()
			self.ui.progressBar.setVisible(False)

	def current_position(self):
		if self.cached_location:
			city, country = self.cached_location
			print("Using cached location:", city, country)
			lat = self.lat
			lon = self.lon
			country = self.country_code_to_name(country)
			self.display_data(city, country, lat, lon)

		ACCESS_TOKEN = "6d4647ad82a34a"  
		response = requests.get(f'http://ipinfo.io/json?token={ACCESS_TOKEN}')
		data = response.json() 

		city = data.get('region', 'Unknown')
		country = data.get('country', 'Unknown')
		lat, lon = self.get_location(city)
		self.cached_location = (city, country)
		self.lat = lat
		self.lon = lon
		country = self.country_code_to_name(country)
		print("Fetched location:", city, country)
		self.display_data(city, country, lat, lon)

	def load_city_dict(self):
		dict_file = "city_dict.json"
		with open(dict_file, 'r', encoding='utf-8') as file:
			city_dict = json.load(file)
		return city_dict

	def get_coordinates(self, city_name, country_code):
		city_dict = self.load_city_dict()
		key = f"{city_name.lower()},{country_code.upper()}"
		coordinate = city_dict.get(key, None) 
		lat = coordinate[0]
		lon = coordinate[1]
		return lat, lon

	def get_input(self):
		input = self.ui.lineEdit.text()
		city_name, country_name = input.split(", ")
		if not city_name:
			print("City name is empty!")
			return
		country_code = self.country_name_to_code(country_name)
		lat, lon = self.get_coordinates(city_name, country_code)
		self.cached_location = (city_name, country_name)
		self.lat = lat
		self.lon = lon
		print("location:", city_name, country_name)
		self.display_data(city_name, country_name, lat, lon)

	def country_name_to_code(self, country_name):
		try:
			country = pycountry.countries.get(name=country_name)
			if country:
				return country.alpha_2
		except KeyError:
			pass
		return "Unknown"
	
	def country_code_to_name(self, country_code):
		try:
			country = pycountry.countries.get(alpha_2=country_code)
			if country:
				return country.name
		except KeyError:
			pass
		return "Unknown"
		
	def display_near_city(self, city, country, lat, lon):
		self.cached_location = (city, country)
		self.lat = lat
		self.lon = lon
		print("location:", city, country)
		self.display_data(city, country, lat, lon)

	def display_data(self, city_name, country, lat, lon):
		self.start_progress()
		self.ui.label_10.setText(f"Loading weather location for: {city_name}, {country}")
		self.ui.label_2.setText(f"Current weather in {city_name}, {country}")
		self.ui.label.setText(f"Weather forecast in {city_name}, {country}")

		buttons = [
			self.ui.nearby_button_1,
			self.ui.nearby_button_2,
			self.ui.nearby_button_3
			]

		# get 3 cities
		near_cities = self.get_valid_nearby_cities(lat, lon, "city.list.json", max_results = 10)
		for i,near_city in enumerate(near_cities):
			lat, lon = self.get_coordinates(near_city[0], near_city[1])
			buttons[i].setText(f'{near_city[0]}, {near_city[1]}')
			buttons[i].clicked.connect(lambda _, city=near_city, latitude=lat, longitude=lon: self.display_near_city(city[0], city[1], latitude, longitude))

		# get current weather data
		current_main, current_icon, current_temp, current_humid, current_wind_speed, current_cloud = self.get_weather_info(lat, lon, city_name)
		#display current weather
		self.ui.current_weather_label.setText(current_main)
		self.ui.current_humidity_label.setText(current_humid)
		self.ui.current_cloud_label.setText(current_cloud)
		self.ui.current_wind_label.setText(current_wind_speed)
		self.ui.current_temp_label.setText(current_temp)

		pixmap = QPixmap(f"images/{current_icon}.png")
		self.ui.current_weather_icon.setPixmap(pixmap)
		self.ui.current_weather_icon.setScaledContents(True) 
		self.set_weather_icon(getattr(self.ui, "current_weather_icon"), current_icon)

		# get future data
		self.daily_weather_forecast(lat, lon, city_name)
		self.three_hours_forecast(lat, lon, city_name)

	def get_weather_info(self, latitude, longitude, city):
		url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_key}&units=metric"

		response = requests.get(url)
		data = response.json()

		main = data['weather'][0]['main']
		description = data['weather'][0]['description']
		icon = data['weather'][0]['icon']
		temp = data['main']['temp']
		humidity = data['main']['humidity']
		wind_speed = data['wind']['speed'] 
		cloud = data['clouds']['all']

		return description, icon, str(round(temp, 1))+"°C", str(humidity)+"%", str(round(wind_speed*3.6,2))+"km/h", str(cloud)+"%"

	def get_location(self, city):
		limit = 1
		url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},&limit={limit}&appid={API_key}"
		response = requests.get(url)
		data = response.json()
		return data[0]['lat'], data[0]['lon']

	def daily_weather_forecast(self, latitude, longitude, city):
		url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_key}&units=metric"
		response = requests.get(url)
		data = response.json()
		daily_weather = {}

		for forecast in data['list']:
			date = forecast['dt_txt'].split(' ')[0]

			day_of_week = datetime.strptime(date, "%Y-%m-%d").strftime("%a")

			temp = forecast['main']['temp']
			humidity = forecast['main']['humidity']
			clouds = forecast['clouds']['all']
			wind_speed = forecast['wind']['speed']
			icon = forecast['weather'][0]['icon']

			if date not in daily_weather:
				daily_weather[date] = {
					"day": day_of_week,
					"high": temp,
					"low": temp,
					"humidity": [humidity],
					"clouds": [clouds],
					"wind_speed": [wind_speed],
					"icons": [icon]
				}
			else:
				daily_weather[date]["high"] = max(daily_weather[date]["high"], temp)
				daily_weather[date]["low"] = min(daily_weather[date]["low"], temp)
				
				daily_weather[date]["humidity"].append(humidity)
				daily_weather[date]["clouds"].append(clouds)
				daily_weather[date]["wind_speed"].append(wind_speed)
				daily_weather[date]["icons"].append(icon)

		for n, (date, weather) in enumerate(list(daily_weather.items())[:5]):
			avg_humidity = sum(weather['humidity']) / len(weather['humidity'])
			avg_clouds = sum(weather['clouds']) / len(weather['clouds'])
			avg_wind_speed = sum(weather['wind_speed']) / len(weather['wind_speed'])

			most_common_icon = Counter(weather['icons']).most_common(1)[0][0]
			self.set_weather_icon(getattr(self.ui, f'forecast2_icon_{n+1}'), most_common_icon)
			getattr(self.ui, f'day_number_{n+1}').setText(weather['day']+" "+date)
			getattr(self.ui, f'forecast2_high_{n+1}').setText(f"High: {weather['high']}°C")
			getattr(self.ui, f'forecast2_low_{n+1}').setText(f"Low: {weather['low']}°C")
			getattr(self.ui, f'forecast2_wind_{n+1}').setText(f"Wind: {round(avg_wind_speed*3.6)}km/h")
			getattr(self.ui, f'forecast2_humid_{n+1}').setText(f"Humidity: {round(avg_humidity)}%")
			getattr(self.ui, f'forecast2_cloud_{n+1}').setText(f"Cloudiness: {round(avg_clouds)}%")

	def set_weather_icon(self, label, icon):
		label.setPixmap(
			QPixmap(os.path.join('images', "%s.png" %icon)))

	def three_hours_forecast(self, latitude, longitude, city):
		url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_key}&units=metric"
		response = requests.get(url)
		data = response.json()
		self.temperatures.clear()
		self.hours.clear()

		for n, forecast in enumerate(data['list'][:15]):
			date_time = forecast['dt_txt']

			date = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
			day_of_week = date.strftime("%a")
			time_of_day = date.strftime("%H:%M")
			description = forecast['weather'][0]['description']
			icon = forecast['weather'][0]['icon']
			temp = forecast['main']['temp']
			humidity = forecast['main']['humidity']
			clouds = forecast['clouds']['all']
			wind_speed = forecast['wind']['speed']

			self.temperatures.append(float(temp))
			self.hours.append(float(date.strftime("%H")))

			getattr(self.ui, f'hour_number_{n+1}').setText(day_of_week + " " + time_of_day)
			self.set_weather_icon(getattr(self.ui, f'forecast1_icon_{n+1}'), icon)
			getattr(self.ui, f'forecast1_temp_{n+1}').setText(f"{temp}°C")
			getattr(self.ui, f'forecast1_describe_{n+1}').setText(description)
		self.draw_graph()

	def update_date_and_time(self):
		current_time = QTime.currentTime()
		label_time = current_time.toString('hh:mm:ss')
		self.ui.label_5.setText(label_time)

		current_date = QDate.currentDate()
		day_name = current_date.toString('dddd')  
		self.ui.label_6.setText(day_name)

		full_date = current_date.toString('d/M/yyyy')  
		self.ui.label_7.setText(full_date)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	widget = MainWindow()
	widget.show()
	sys.exit(app.exec())
