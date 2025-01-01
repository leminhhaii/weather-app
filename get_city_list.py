import json
from pycountry import countries

def process_city_list(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        city_data = json.load(file)
    
    formatted_cities = []

    for city in city_data:
        city_name = city.get("name", "")
        country_code = city.get("country", "")

        country_obj = countries.get(alpha_2=country_code)
        country_name = country_obj.name if country_obj else "Unknown"
        country_name = country_name.split(",")[0].strip()

        formatted_cities.append(f"{city_name}, {country_name}")


    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("\n".join(formatted_cities))



def create_city_dict(city_file, dict_file):
    with open(city_file, 'r', encoding='utf-8') as file:
        cities = json.load(file)

    # Create a dictionary with "city_name,country_code" as keys
    city_dict = {
        f"{city['name'].lower()},{city['country'].upper()}": (city['coord']['lat'], city['coord']['lon'])
        for city in cities
    }

    # Save the dictionary to a JSON file
    with open(dict_file, 'w', encoding='utf-8') as dict_out:
        json.dump(city_dict, dict_out)

dict_file = "city_dict.json"  # File to save the dictionary
input_json_file = "city.list.json"  # Replace with your JSON file path
output_text_file = "formatted_cities.txt"

process_city_list(input_json_file, output_text_file)
create_city_dict(input_json_file, dict_file)