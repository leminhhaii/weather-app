# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1244, 943)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setStyleSheet(u"background-color:rgb(198,222, 255);\n"
"color: #000000;")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -158, 1251, 1154))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_container = QFrame(self.scrollAreaWidgetContents)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setAutoFillBackground(False)
        self.main_container.setStyleSheet(u"")
        self.main_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.main_container)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame = QFrame(self.main_container)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 80))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.gridLayout_7.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_51 = QFrame(self.main_container)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMinimumSize(QSize(0, 51))
        self.frame_51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label = QLabel(self.frame_51)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(239, 255, 219);\n"
"color: #000000;\n"
"padding: 10px;\n"
"border-radius: 20px;")

        self.horizontalLayout_17.addWidget(self.label)

        self.horizontalSpacer_5 = QSpacerItem(926, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_5)


        self.gridLayout_7.addWidget(self.frame_51, 7, 0, 1, 1)

        self.frame_50 = QFrame(self.main_container)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMinimumSize(QSize(0, 51))
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_2 = QLabel(self.frame_50)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(239, 255, 219);\n"
"color: #000000;\n"
"padding: 10px;\n"
"border-radius: 20px;")

        self.horizontalLayout_16.addWidget(self.label_2)

        self.refresh_button = QPushButton(self.frame_50)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setMinimumSize(QSize(120, 40))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.refresh_button.setIcon(icon)

        self.horizontalLayout_16.addWidget(self.refresh_button)

        self.horizontalSpacer_4 = QSpacerItem(934, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.app_info_button = QPushButton(self.frame_50)
        self.app_info_button.setObjectName(u"app_info_button")
        self.app_info_button.setMinimumSize(QSize(120, 40))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogInformation))
        self.app_info_button.setIcon(icon1)

        self.horizontalLayout_16.addWidget(self.app_info_button)


        self.gridLayout_7.addWidget(self.frame_50, 3, 0, 1, 1)

        self.frame_11 = QFrame(self.main_container)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 70))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_10.setFont(font2)

        self.verticalLayout_2.addWidget(self.label_10)

        self.progressBar = QProgressBar(self.frame_11)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	color: #000000\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.506, x2:1, y2:0.494, stop:0 rgba(252, 192, 125, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border-radius: 5px;\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.gridLayout_7.addWidget(self.frame_11, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.main_container)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(200, 200))
        self.frame_9.setMaximumSize(QSize(200, 200))
        self.frame_9.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 100px;\n"
"color: rgb(252, 191, 130);\n"
"background-color: transparent;\n"
"")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.current_weather_icon = QLabel(self.frame_9)
        self.current_weather_icon.setObjectName(u"current_weather_icon")
        self.current_weather_icon.setMinimumSize(QSize(100, 100))
        self.current_weather_icon.setMaximumSize(QSize(100, 100))
        self.current_weather_icon.setStyleSheet(u"border: none;\n"
"background: none;")
        self.current_weather_icon.setScaledContents(True)
        self.current_weather_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.current_weather_icon)

        self.current_weather_label = QLabel(self.frame_9)
        self.current_weather_label.setObjectName(u"current_weather_label")
        font3 = QFont()
        font3.setFamilies([u"Adobe Caslon Pro"])
        font3.setPointSize(12)
        self.current_weather_label.setFont(font3)
        self.current_weather_label.setStyleSheet(u"border: none;\n"
"padding: 15px;\n"
"background: none;\n"
"color:#000000;")
        self.current_weather_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_weather_label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.current_weather_label)

        self.current_weather_label.raise_()
        self.current_weather_icon.raise_()

        self.horizontalLayout.addWidget(self.frame_9)

        self.current_temp_label = QLabel(self.frame_3)
        self.current_temp_label.setObjectName(u"current_temp_label")
        self.current_temp_label.setMaximumSize(QSize(150, 16777215))
        font4 = QFont()
        font4.setPointSize(24)
        self.current_temp_label.setFont(font4)
        self.current_temp_label.setStyleSheet(u"background-color: rgb(238, 238, 255);\n"
"color: #000000;\n"
"padding: 10px;\n"
"border-radius: 20px;")

        self.horizontalLayout.addWidget(self.current_temp_label)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 16777215))
        self.frame_6.setStyleSheet(u"background-color: rgb(238, 238, 255);\n"
"color: #000000;\n"
"padding: 10px;\n"
"border-radius: 20px;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(50, 50))
        self.label_12.setMaximumSize(QSize(50, 50))
        self.label_12.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_12.setPixmap(QPixmap(u"icons/wind.png"))
        self.label_12.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.current_wind_label = QLabel(self.frame_6)
        self.current_wind_label.setObjectName(u"current_wind_label")
        self.current_wind_label.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setFamilies([u"Adobe Caslon Pro"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.current_wind_label.setFont(font5)
        self.current_wind_label.setStyleSheet(u"color: rgb(173, 167, 220);")

        self.gridLayout_3.addWidget(self.current_wind_label, 1, 2, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 50))
        self.label_13.setMaximumSize(QSize(50, 50))
        self.label_13.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_13.setPixmap(QPixmap(u"icons/humidity.png"))
        self.label_13.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(50, 50))
        self.label_8.setMaximumSize(QSize(50, 50))
        self.label_8.setStyleSheet(u"padding: 5px;\n"
"border: 2px solid rgb(103, 103, 103);\n"
"border-radius: 20px;\n"
"color: rgb(252, 191, 130);")
        self.label_8.setPixmap(QPixmap(u"icons/cloud.png"))
        self.label_8.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 30))
        self.label_15.setFont(font3)

        self.gridLayout_3.addWidget(self.label_15, 0, 1, 1, 1)

        self.current_cloud_label = QLabel(self.frame_6)
        self.current_cloud_label.setObjectName(u"current_cloud_label")
        self.current_cloud_label.setMinimumSize(QSize(0, 30))
        self.current_cloud_label.setFont(font5)
        self.current_cloud_label.setStyleSheet(u"color: rgb(173, 167, 220);")

        self.gridLayout_3.addWidget(self.current_cloud_label, 0, 2, 1, 1)

        self.current_humidity_label = QLabel(self.frame_6)
        self.current_humidity_label.setObjectName(u"current_humidity_label")
        self.current_humidity_label.setMinimumSize(QSize(0, 30))
        self.current_humidity_label.setFont(font5)
        self.current_humidity_label.setStyleSheet(u"color: rgb(173, 167, 220);")

        self.gridLayout_3.addWidget(self.current_humidity_label, 2, 2, 1, 1)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 30))
        self.label_17.setFont(font3)

        self.gridLayout_3.addWidget(self.label_17, 1, 1, 1, 1)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setFont(font3)

        self.gridLayout_3.addWidget(self.label_16, 2, 1, 1, 1)

        self.current_humidity_label.raise_()
        self.label_8.raise_()
        self.current_wind_label.raise_()
        self.label_12.raise_()
        self.label_16.raise_()
        self.label_13.raise_()
        self.label_17.raise_()
        self.current_cloud_label.raise_()
        self.label_15.raise_()

        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_53 = QFrame(self.frame_3)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setStyleSheet(u"background-color: rgb(238, 238, 255);\n"
"color: #000000;\n"
"border-radius: 20px;")
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_53)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_9 = QLabel(self.frame_53)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")

        self.verticalLayout_17.addWidget(self.label_9)

        self.frame_52 = QFrame(self.frame_53)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QSize(0, 0))
        self.frame_52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_52)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.nearby_button_1 = QPushButton(self.frame_52)
        self.nearby_button_1.setObjectName(u"nearby_button_1")
        self.nearby_button_1.setMinimumSize(QSize(0, 50))
        self.nearby_button_1.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black;\n"
"    background: transparent;\n"
"    color: black;  /* Text color */\n"
"    font-size: 14px;  /* Adjust font size as needed */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(0, 0, 0, 50);  /* Optional: a subtle hover effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: rgba(0, 0, 0, 100);  /* Optional: a subtle pressed effect */\n"
"}\n"
"")

        self.verticalLayout_16.addWidget(self.nearby_button_1)

        self.nearby_button_2 = QPushButton(self.frame_52)
        self.nearby_button_2.setObjectName(u"nearby_button_2")
        self.nearby_button_2.setMinimumSize(QSize(0, 50))
        self.nearby_button_2.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black;\n"
"    background: transparent;\n"
"    color: black;  /* Text color */\n"
"    font-size: 14px;  /* Adjust font size as needed */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(0, 0, 0, 50);  /* Optional: a subtle hover effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: rgba(0, 0, 0, 100);  /* Optional: a subtle pressed effect */\n"
"}\n"
"")

        self.verticalLayout_16.addWidget(self.nearby_button_2)

        self.nearby_button_3 = QPushButton(self.frame_52)
        self.nearby_button_3.setObjectName(u"nearby_button_3")
        self.nearby_button_3.setMinimumSize(QSize(0, 50))
        self.nearby_button_3.setStyleSheet(u"QPushButton {\n"
"    border: 1px solid black;\n"
"    background: transparent;\n"
"    color: black;  /* Text color */\n"
"    font-size: 14px;  /* Adjust font size as needed */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(0, 0, 0, 50);  /* Optional: a subtle hover effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: rgba(0, 0, 0, 100);  /* Optional: a subtle pressed effect */\n"
"}\n"
"")

        self.verticalLayout_16.addWidget(self.nearby_button_3)


        self.verticalLayout_17.addWidget(self.frame_52)


        self.horizontalLayout.addWidget(self.frame_53)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(238, 238, 255);\n"
"color: #000000;\n"
"border-radius: 20px;")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.gridLayout_5.addWidget(self.frame_10, 3, 0, 1, 2)

        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 50))
        self.label_14.setMaximumSize(QSize(50, 50))
        self.label_14.setPixmap(QPixmap(u"icons/calendar_1.png"))

        self.gridLayout_5.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        font6 = QFont()
        font6.setPointSize(18)
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 10px;\n"
"border-radius: 20px;")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.gridLayout_5.addWidget(self.frame_16, 1, 0, 1, 2)


        self.horizontalLayout.addWidget(self.frame_8)


        self.gridLayout_7.addWidget(self.frame_3, 6, 0, 1, 1)

        self.frame_2 = QFrame(self.main_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 60))
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 10px;\n"
"border-radius: 20px;")

        self.gridLayout_4.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 3, 1, 1)

        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(0, 40))
        self.toolButton.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.toolButton, 1, 4, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background-color: rgb(239, 255, 219);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 10px;")

        self.gridLayout_4.addWidget(self.label_11, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setStyleSheet(u"")
        icon2 = QIcon(QIcon.fromTheme(u"edit-find"))
        self.pushButton.setIcon(icon2)

        self.gridLayout_4.addWidget(self.pushButton, 1, 2, 1, 1)


        self.gridLayout_7.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tabWidget = QTabWidget(self.main_container)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(983, 320))
        self.tabWidget.setMaximumSize(QSize(20000, 20000))
        self.three_hour_forecast = QWidget()
        self.three_hour_forecast.setObjectName(u"three_hour_forecast")
        self.verticalLayout_7 = QVBoxLayout(self.three_hour_forecast)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_2 = QScrollArea(self.three_hour_forecast)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 2177, 300))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(238, 238, 255);\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.frame_12)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(80, 80))
        self.frame_5.setMaximumSize(QSize(80, 80))
        self.frame_5.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_5)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.forecast1_icon_1 = QLabel(self.frame_5)
        self.forecast1_icon_1.setObjectName(u"forecast1_icon_1")
        self.forecast1_icon_1.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_1.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_1.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_1.setScaledContents(True)
        self.forecast1_icon_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_18.addWidget(self.forecast1_icon_1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_5, 1, 0, 1, 1)

        self.forecast1_temp_1 = QLabel(self.frame_12)
        self.forecast1_temp_1.setObjectName(u"forecast1_temp_1")

        self.gridLayout.addWidget(self.forecast1_temp_1, 2, 0, 1, 1)

        self.forecast1_describe_1 = QLabel(self.frame_12)
        self.forecast1_describe_1.setObjectName(u"forecast1_describe_1")
        font7 = QFont()
        font7.setBold(True)
        self.forecast1_describe_1.setFont(font7)

        self.gridLayout.addWidget(self.forecast1_describe_1, 3, 0, 1, 1)

        self.hour_number_1 = QLabel(self.frame_12)
        self.hour_number_1.setObjectName(u"hour_number_1")
        self.hour_number_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.hour_number_1, 0, 0, 1, 2)


        self.horizontalLayout_3.addWidget(self.frame_12)

        self.frame_17 = QFrame(self.frame_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_17)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_7 = QFrame(self.frame_17)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(80, 80))
        self.frame_7.setMaximumSize(QSize(80, 80))
        self.frame_7.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_7)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.forecast1_icon_2 = QLabel(self.frame_7)
        self.forecast1_icon_2.setObjectName(u"forecast1_icon_2")
        self.forecast1_icon_2.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_2.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_2.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_2.setScaledContents(True)
        self.forecast1_icon_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_19.addWidget(self.forecast1_icon_2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame_7, 2, 0, 1, 1)

        self.forecast1_temp_2 = QLabel(self.frame_17)
        self.forecast1_temp_2.setObjectName(u"forecast1_temp_2")

        self.gridLayout_6.addWidget(self.forecast1_temp_2, 3, 0, 1, 1)

        self.hour_number_2 = QLabel(self.frame_17)
        self.hour_number_2.setObjectName(u"hour_number_2")
        self.hour_number_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.hour_number_2, 0, 0, 1, 2)

        self.forecast1_describe_2 = QLabel(self.frame_17)
        self.forecast1_describe_2.setObjectName(u"forecast1_describe_2")
        self.forecast1_describe_2.setFont(font7)

        self.gridLayout_6.addWidget(self.forecast1_describe_2, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_4)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_18)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(80, 80))
        self.frame_19.setMaximumSize(QSize(80, 80))
        self.frame_19.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_19)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.forecast1_icon_3 = QLabel(self.frame_19)
        self.forecast1_icon_3.setObjectName(u"forecast1_icon_3")
        self.forecast1_icon_3.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_3.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_3.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_3.setScaledContents(True)
        self.forecast1_icon_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_20.addWidget(self.forecast1_icon_3, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame_19, 2, 0, 1, 1)

        self.forecast1_temp_3 = QLabel(self.frame_18)
        self.forecast1_temp_3.setObjectName(u"forecast1_temp_3")

        self.gridLayout_8.addWidget(self.forecast1_temp_3, 3, 0, 1, 1)

        self.hour_number_3 = QLabel(self.frame_18)
        self.hour_number_3.setObjectName(u"hour_number_3")
        self.hour_number_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.hour_number_3, 0, 0, 1, 2)

        self.forecast1_describe_3 = QLabel(self.frame_18)
        self.forecast1_describe_3.setObjectName(u"forecast1_describe_3")
        self.forecast1_describe_3.setFont(font7)

        self.gridLayout_8.addWidget(self.forecast1_describe_3, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_18)

        self.frame_20 = QFrame(self.frame_4)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background-color: rgb(255, 233, 236);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background: transparent;\n"
"")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_20)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(80, 80))
        self.frame_21.setMaximumSize(QSize(80, 80))
        self.frame_21.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_21)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.forecast1_icon_4 = QLabel(self.frame_21)
        self.forecast1_icon_4.setObjectName(u"forecast1_icon_4")
        self.forecast1_icon_4.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_4.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_4.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_4.setScaledContents(True)
        self.forecast1_icon_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_21.addWidget(self.forecast1_icon_4, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_21, 2, 0, 1, 1)

        self.forecast1_temp_4 = QLabel(self.frame_20)
        self.forecast1_temp_4.setObjectName(u"forecast1_temp_4")

        self.gridLayout_13.addWidget(self.forecast1_temp_4, 3, 0, 1, 1)

        self.hour_number_4 = QLabel(self.frame_20)
        self.hour_number_4.setObjectName(u"hour_number_4")
        self.hour_number_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_13.addWidget(self.hour_number_4, 0, 0, 1, 2)

        self.forecast1_describe_4 = QLabel(self.frame_20)
        self.forecast1_describe_4.setObjectName(u"forecast1_describe_4")
        self.forecast1_describe_4.setFont(font7)

        self.gridLayout_13.addWidget(self.forecast1_describe_4, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_20)

        self.frame_22 = QFrame(self.frame_4)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_22)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMinimumSize(QSize(80, 80))
        self.frame_23.setMaximumSize(QSize(80, 80))
        self.frame_23.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_23)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.forecast1_icon_5 = QLabel(self.frame_23)
        self.forecast1_icon_5.setObjectName(u"forecast1_icon_5")
        self.forecast1_icon_5.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_5.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_5.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_5.setScaledContents(True)
        self.forecast1_icon_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_22.addWidget(self.forecast1_icon_5, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_23, 2, 0, 1, 1)

        self.forecast1_temp_5 = QLabel(self.frame_22)
        self.forecast1_temp_5.setObjectName(u"forecast1_temp_5")

        self.gridLayout_14.addWidget(self.forecast1_temp_5, 3, 0, 1, 1)

        self.hour_number_5 = QLabel(self.frame_22)
        self.hour_number_5.setObjectName(u"hour_number_5")
        self.hour_number_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_14.addWidget(self.hour_number_5, 0, 0, 1, 2)

        self.forecast1_describe_5 = QLabel(self.frame_22)
        self.forecast1_describe_5.setObjectName(u"forecast1_describe_5")
        self.forecast1_describe_5.setFont(font7)

        self.gridLayout_14.addWidget(self.forecast1_describe_5, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_22)

        self.frame_24 = QFrame(self.frame_4)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_24)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(80, 80))
        self.frame_25.setMaximumSize(QSize(80, 80))
        self.frame_25.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_25)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.forecast1_icon_6 = QLabel(self.frame_25)
        self.forecast1_icon_6.setObjectName(u"forecast1_icon_6")
        self.forecast1_icon_6.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_6.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_6.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_6.setScaledContents(True)
        self.forecast1_icon_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_23.addWidget(self.forecast1_icon_6, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame_25, 2, 0, 1, 1)

        self.forecast1_temp_6 = QLabel(self.frame_24)
        self.forecast1_temp_6.setObjectName(u"forecast1_temp_6")

        self.gridLayout_15.addWidget(self.forecast1_temp_6, 3, 0, 1, 1)

        self.hour_number_6 = QLabel(self.frame_24)
        self.hour_number_6.setObjectName(u"hour_number_6")
        self.hour_number_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.hour_number_6, 0, 0, 1, 2)

        self.forecast1_describe_6 = QLabel(self.frame_24)
        self.forecast1_describe_6.setObjectName(u"forecast1_describe_6")
        self.forecast1_describe_6.setFont(font7)

        self.gridLayout_15.addWidget(self.forecast1_describe_6, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_24)

        self.frame_26 = QFrame(self.frame_4)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_26)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(80, 80))
        self.frame_27.setMaximumSize(QSize(80, 80))
        self.frame_27.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_27)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.forecast1_icon_7 = QLabel(self.frame_27)
        self.forecast1_icon_7.setObjectName(u"forecast1_icon_7")
        self.forecast1_icon_7.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_7.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_7.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_7.setScaledContents(True)
        self.forecast1_icon_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_24.addWidget(self.forecast1_icon_7, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_27, 2, 0, 1, 1)

        self.forecast1_temp_7 = QLabel(self.frame_26)
        self.forecast1_temp_7.setObjectName(u"forecast1_temp_7")

        self.gridLayout_16.addWidget(self.forecast1_temp_7, 3, 0, 1, 1)

        self.hour_number_7 = QLabel(self.frame_26)
        self.hour_number_7.setObjectName(u"hour_number_7")
        self.hour_number_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_16.addWidget(self.hour_number_7, 0, 0, 1, 2)

        self.forecast1_describe_7 = QLabel(self.frame_26)
        self.forecast1_describe_7.setObjectName(u"forecast1_describe_7")
        self.forecast1_describe_7.setFont(font7)

        self.gridLayout_16.addWidget(self.forecast1_describe_7, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_26)

        self.frame_28 = QFrame(self.frame_4)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_28)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(80, 80))
        self.frame_29.setMaximumSize(QSize(80, 80))
        self.frame_29.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_29)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.forecast1_icon_8 = QLabel(self.frame_29)
        self.forecast1_icon_8.setObjectName(u"forecast1_icon_8")
        self.forecast1_icon_8.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_8.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_8.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_8.setScaledContents(True)
        self.forecast1_icon_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_25.addWidget(self.forecast1_icon_8, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.frame_29, 2, 0, 1, 1)

        self.forecast1_temp_8 = QLabel(self.frame_28)
        self.forecast1_temp_8.setObjectName(u"forecast1_temp_8")

        self.gridLayout_17.addWidget(self.forecast1_temp_8, 3, 0, 1, 1)

        self.hour_number_8 = QLabel(self.frame_28)
        self.hour_number_8.setObjectName(u"hour_number_8")
        self.hour_number_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_17.addWidget(self.hour_number_8, 0, 0, 1, 2)

        self.forecast1_describe_8 = QLabel(self.frame_28)
        self.forecast1_describe_8.setObjectName(u"forecast1_describe_8")
        self.forecast1_describe_8.setFont(font7)

        self.gridLayout_17.addWidget(self.forecast1_describe_8, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_28)

        self.frame_30 = QFrame(self.frame_4)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_30)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(80, 80))
        self.frame_32.setMaximumSize(QSize(80, 80))
        self.frame_32.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_32)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.forecast1_icon_9 = QLabel(self.frame_32)
        self.forecast1_icon_9.setObjectName(u"forecast1_icon_9")
        self.forecast1_icon_9.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_9.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_9.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_9.setScaledContents(True)
        self.forecast1_icon_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_32.addWidget(self.forecast1_icon_9, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.frame_32, 2, 0, 1, 1)

        self.forecast1_temp_9 = QLabel(self.frame_30)
        self.forecast1_temp_9.setObjectName(u"forecast1_temp_9")

        self.gridLayout_31.addWidget(self.forecast1_temp_9, 3, 0, 1, 1)

        self.hour_number_9 = QLabel(self.frame_30)
        self.hour_number_9.setObjectName(u"hour_number_9")
        self.hour_number_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_31.addWidget(self.hour_number_9, 0, 0, 1, 2)

        self.forecast1_describe_9 = QLabel(self.frame_30)
        self.forecast1_describe_9.setObjectName(u"forecast1_describe_9")
        self.forecast1_describe_9.setFont(font7)

        self.gridLayout_31.addWidget(self.forecast1_describe_9, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_30)

        self.frame_34 = QFrame(self.frame_4)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_34)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(80, 80))
        self.frame_36.setMaximumSize(QSize(80, 80))
        self.frame_36.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_34 = QGridLayout(self.frame_36)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.forecast1_icon_10 = QLabel(self.frame_36)
        self.forecast1_icon_10.setObjectName(u"forecast1_icon_10")
        self.forecast1_icon_10.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_10.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_10.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_10.setScaledContents(True)
        self.forecast1_icon_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_34.addWidget(self.forecast1_icon_10, 0, 0, 1, 1)


        self.gridLayout_33.addWidget(self.frame_36, 2, 0, 1, 1)

        self.forecast1_temp_10 = QLabel(self.frame_34)
        self.forecast1_temp_10.setObjectName(u"forecast1_temp_10")

        self.gridLayout_33.addWidget(self.forecast1_temp_10, 3, 0, 1, 1)

        self.hour_number_10 = QLabel(self.frame_34)
        self.hour_number_10.setObjectName(u"hour_number_10")
        self.hour_number_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_33.addWidget(self.hour_number_10, 0, 0, 1, 2)

        self.forecast1_describe_10 = QLabel(self.frame_34)
        self.forecast1_describe_10.setObjectName(u"forecast1_describe_10")
        self.forecast1_describe_10.setFont(font7)

        self.gridLayout_33.addWidget(self.forecast1_describe_10, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_34)

        self.frame_38 = QFrame(self.frame_4)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_38)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(80, 80))
        self.frame_39.setMaximumSize(QSize(80, 80))
        self.frame_39.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_39)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.forecast1_icon_11 = QLabel(self.frame_39)
        self.forecast1_icon_11.setObjectName(u"forecast1_icon_11")
        self.forecast1_icon_11.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_11.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_11.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_11.setScaledContents(True)
        self.forecast1_icon_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_36.addWidget(self.forecast1_icon_11, 0, 0, 1, 1)


        self.gridLayout_35.addWidget(self.frame_39, 2, 0, 1, 1)

        self.forecast1_temp_11 = QLabel(self.frame_38)
        self.forecast1_temp_11.setObjectName(u"forecast1_temp_11")

        self.gridLayout_35.addWidget(self.forecast1_temp_11, 3, 0, 1, 1)

        self.hour_number_11 = QLabel(self.frame_38)
        self.hour_number_11.setObjectName(u"hour_number_11")
        self.hour_number_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_35.addWidget(self.hour_number_11, 0, 0, 1, 2)

        self.forecast1_describe_11 = QLabel(self.frame_38)
        self.forecast1_describe_11.setObjectName(u"forecast1_describe_11")
        self.forecast1_describe_11.setFont(font7)

        self.gridLayout_35.addWidget(self.forecast1_describe_11, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_38)

        self.frame_40 = QFrame(self.frame_4)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_40)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMinimumSize(QSize(80, 80))
        self.frame_41.setMaximumSize(QSize(80, 80))
        self.frame_41.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_41)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.forecast1_icon_12 = QLabel(self.frame_41)
        self.forecast1_icon_12.setObjectName(u"forecast1_icon_12")
        self.forecast1_icon_12.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_12.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_12.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_12.setScaledContents(True)
        self.forecast1_icon_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_38.addWidget(self.forecast1_icon_12, 0, 0, 1, 1)


        self.gridLayout_37.addWidget(self.frame_41, 2, 0, 1, 1)

        self.forecast1_temp_12 = QLabel(self.frame_40)
        self.forecast1_temp_12.setObjectName(u"forecast1_temp_12")

        self.gridLayout_37.addWidget(self.forecast1_temp_12, 3, 0, 1, 1)

        self.hour_number_12 = QLabel(self.frame_40)
        self.hour_number_12.setObjectName(u"hour_number_12")
        self.hour_number_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_37.addWidget(self.hour_number_12, 0, 0, 1, 2)

        self.forecast1_describe_12 = QLabel(self.frame_40)
        self.forecast1_describe_12.setObjectName(u"forecast1_describe_12")
        self.forecast1_describe_12.setFont(font7)

        self.gridLayout_37.addWidget(self.forecast1_describe_12, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_40)

        self.frame_42 = QFrame(self.frame_4)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_42.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_42)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setMinimumSize(QSize(80, 80))
        self.frame_43.setMaximumSize(QSize(80, 80))
        self.frame_43.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_43.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_43)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.forecast1_icon_13 = QLabel(self.frame_43)
        self.forecast1_icon_13.setObjectName(u"forecast1_icon_13")
        self.forecast1_icon_13.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_13.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_13.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_13.setScaledContents(True)
        self.forecast1_icon_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_40.addWidget(self.forecast1_icon_13, 0, 0, 1, 1)


        self.gridLayout_39.addWidget(self.frame_43, 2, 0, 1, 1)

        self.forecast1_temp_13 = QLabel(self.frame_42)
        self.forecast1_temp_13.setObjectName(u"forecast1_temp_13")

        self.gridLayout_39.addWidget(self.forecast1_temp_13, 3, 0, 1, 1)

        self.hour_number_13 = QLabel(self.frame_42)
        self.hour_number_13.setObjectName(u"hour_number_13")
        self.hour_number_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_39.addWidget(self.hour_number_13, 0, 0, 1, 2)

        self.forecast1_describe_13 = QLabel(self.frame_42)
        self.forecast1_describe_13.setObjectName(u"forecast1_describe_13")
        self.forecast1_describe_13.setFont(font7)

        self.gridLayout_39.addWidget(self.forecast1_describe_13, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_42)

        self.frame_44 = QFrame(self.frame_4)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_44.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_41 = QGridLayout(self.frame_44)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setMinimumSize(QSize(80, 80))
        self.frame_45.setMaximumSize(QSize(80, 80))
        self.frame_45.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_45.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_45)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.forecast1_icon_14 = QLabel(self.frame_45)
        self.forecast1_icon_14.setObjectName(u"forecast1_icon_14")
        self.forecast1_icon_14.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_14.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_14.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_14.setScaledContents(True)
        self.forecast1_icon_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_42.addWidget(self.forecast1_icon_14, 0, 0, 1, 1)


        self.gridLayout_41.addWidget(self.frame_45, 2, 0, 1, 1)

        self.forecast1_temp_14 = QLabel(self.frame_44)
        self.forecast1_temp_14.setObjectName(u"forecast1_temp_14")

        self.gridLayout_41.addWidget(self.forecast1_temp_14, 3, 0, 1, 1)

        self.hour_number_14 = QLabel(self.frame_44)
        self.hour_number_14.setObjectName(u"hour_number_14")
        self.hour_number_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_41.addWidget(self.hour_number_14, 0, 0, 1, 2)

        self.forecast1_describe_14 = QLabel(self.frame_44)
        self.forecast1_describe_14.setObjectName(u"forecast1_describe_14")
        self.forecast1_describe_14.setFont(font7)

        self.gridLayout_41.addWidget(self.forecast1_describe_14, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_44)

        self.frame_46 = QFrame(self.frame_4)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;\n"
"background-color: transparent;")
        self.frame_46.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_46)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.frame_47 = QFrame(self.frame_46)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMinimumSize(QSize(80, 80))
        self.frame_47.setMaximumSize(QSize(80, 80))
        self.frame_47.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_47.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_47)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.forecast1_icon_15 = QLabel(self.frame_47)
        self.forecast1_icon_15.setObjectName(u"forecast1_icon_15")
        self.forecast1_icon_15.setMinimumSize(QSize(40, 40))
        self.forecast1_icon_15.setMaximumSize(QSize(40, 40))
        self.forecast1_icon_15.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast1_icon_15.setScaledContents(True)
        self.forecast1_icon_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_44.addWidget(self.forecast1_icon_15, 0, 0, 1, 1)


        self.gridLayout_43.addWidget(self.frame_47, 2, 0, 1, 1)

        self.forecast1_temp_15 = QLabel(self.frame_46)
        self.forecast1_temp_15.setObjectName(u"forecast1_temp_15")

        self.gridLayout_43.addWidget(self.forecast1_temp_15, 3, 0, 1, 1)

        self.hour_number_15 = QLabel(self.frame_46)
        self.hour_number_15.setObjectName(u"hour_number_15")
        self.hour_number_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_43.addWidget(self.hour_number_15, 0, 0, 1, 2)

        self.forecast1_describe_15 = QLabel(self.frame_46)
        self.forecast1_describe_15.setObjectName(u"forecast1_describe_15")
        self.forecast1_describe_15.setFont(font7)

        self.gridLayout_43.addWidget(self.forecast1_describe_15, 4, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_46)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.three_hour_forecast, "")
        self.Daily_forecast = QWidget()
        self.Daily_forecast.setObjectName(u"Daily_forecast")
        self.verticalLayout_6 = QVBoxLayout(self.Daily_forecast)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_13 = QFrame(self.Daily_forecast)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_13)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"background-color: rgb(238, 238, 255);\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: none;")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"background-color: transparent;\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.forecast2_cloud_1 = QLabel(self.frame_15)
        self.forecast2_cloud_1.setObjectName(u"forecast2_cloud_1")
        self.forecast2_cloud_1.setMinimumSize(QSize(0, 30))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setPointSize(9)
        font8.setBold(True)
        self.forecast2_cloud_1.setFont(font8)
        self.forecast2_cloud_1.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_2.addWidget(self.forecast2_cloud_1, 4, 0, 1, 2)

        self.forecast2_high_1 = QLabel(self.frame_15)
        self.forecast2_high_1.setObjectName(u"forecast2_high_1")
        self.forecast2_high_1.setStyleSheet(u"border:none;")

        self.gridLayout_2.addWidget(self.forecast2_high_1, 1, 1, 1, 1)

        self.day_number_1 = QLabel(self.frame_15)
        self.day_number_1.setObjectName(u"day_number_1")
        self.day_number_1.setStyleSheet(u"border:none;")
        self.day_number_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.day_number_1, 0, 0, 1, 2)

        self.forecast2_low_1 = QLabel(self.frame_15)
        self.forecast2_low_1.setObjectName(u"forecast2_low_1")
        self.forecast2_low_1.setStyleSheet(u"border:none;")

        self.gridLayout_2.addWidget(self.forecast2_low_1, 2, 1, 1, 1)

        self.frame_54 = QFrame(self.frame_15)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMinimumSize(QSize(80, 80))
        self.frame_54.setMaximumSize(QSize(80, 80))
        self.frame_54.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_26 = QGridLayout(self.frame_54)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.forecast2_icon_1 = QLabel(self.frame_54)
        self.forecast2_icon_1.setObjectName(u"forecast2_icon_1")
        self.forecast2_icon_1.setMinimumSize(QSize(40, 40))
        self.forecast2_icon_1.setMaximumSize(QSize(40, 40))
        self.forecast2_icon_1.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast2_icon_1.setScaledContents(True)
        self.forecast2_icon_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_26.addWidget(self.forecast2_icon_1, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_54, 1, 0, 2, 1)

        self.forecast2_wind_1 = QLabel(self.frame_15)
        self.forecast2_wind_1.setObjectName(u"forecast2_wind_1")
        self.forecast2_wind_1.setMinimumSize(QSize(0, 30))
        self.forecast2_wind_1.setFont(font8)
        self.forecast2_wind_1.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_2.addWidget(self.forecast2_wind_1, 3, 0, 1, 2)

        self.forecast2_humid_1 = QLabel(self.frame_15)
        self.forecast2_humid_1.setObjectName(u"forecast2_humid_1")
        self.forecast2_humid_1.setMinimumSize(QSize(0, 30))
        self.forecast2_humid_1.setFont(font8)
        self.forecast2_humid_1.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_2.addWidget(self.forecast2_humid_1, 5, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_15)

        self.frame_31 = QFrame(self.frame_14)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"background-color: transparent;\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: 1px solid black;")
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_31)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.forecast2_cloud_2 = QLabel(self.frame_31)
        self.forecast2_cloud_2.setObjectName(u"forecast2_cloud_2")
        self.forecast2_cloud_2.setMinimumSize(QSize(0, 30))
        self.forecast2_cloud_2.setFont(font8)
        self.forecast2_cloud_2.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_9.addWidget(self.forecast2_cloud_2, 4, 0, 1, 2)

        self.forecast2_low_2 = QLabel(self.frame_31)
        self.forecast2_low_2.setObjectName(u"forecast2_low_2")
        self.forecast2_low_2.setStyleSheet(u"border:none;")

        self.gridLayout_9.addWidget(self.forecast2_low_2, 2, 1, 1, 1)

        self.forecast2_high_2 = QLabel(self.frame_31)
        self.forecast2_high_2.setObjectName(u"forecast2_high_2")
        self.forecast2_high_2.setStyleSheet(u"border:none;")

        self.gridLayout_9.addWidget(self.forecast2_high_2, 1, 1, 1, 1)

        self.frame_55 = QFrame(self.frame_31)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setMinimumSize(QSize(80, 80))
        self.frame_55.setMaximumSize(QSize(80, 80))
        self.frame_55.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_55.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_55)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.forecast2_icon_2 = QLabel(self.frame_55)
        self.forecast2_icon_2.setObjectName(u"forecast2_icon_2")
        self.forecast2_icon_2.setMinimumSize(QSize(40, 40))
        self.forecast2_icon_2.setMaximumSize(QSize(40, 40))
        self.forecast2_icon_2.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast2_icon_2.setScaledContents(True)
        self.forecast2_icon_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_27.addWidget(self.forecast2_icon_2, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_55, 1, 0, 2, 1)

        self.day_number_2 = QLabel(self.frame_31)
        self.day_number_2.setObjectName(u"day_number_2")
        self.day_number_2.setStyleSheet(u"border: none;")
        self.day_number_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_9.addWidget(self.day_number_2, 0, 0, 1, 2)

        self.forecast2_wind_2 = QLabel(self.frame_31)
        self.forecast2_wind_2.setObjectName(u"forecast2_wind_2")
        self.forecast2_wind_2.setMinimumSize(QSize(0, 30))
        self.forecast2_wind_2.setFont(font8)
        self.forecast2_wind_2.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_9.addWidget(self.forecast2_wind_2, 3, 0, 1, 2)

        self.forecast2_humid_2 = QLabel(self.frame_31)
        self.forecast2_humid_2.setObjectName(u"forecast2_humid_2")
        self.forecast2_humid_2.setMinimumSize(QSize(0, 30))
        self.forecast2_humid_2.setFont(font8)
        self.forecast2_humid_2.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_9.addWidget(self.forecast2_humid_2, 5, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_31)

        self.frame_33 = QFrame(self.frame_14)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"background-color: transparent;\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: 1px solid black;")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_33)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.day_number_3 = QLabel(self.frame_33)
        self.day_number_3.setObjectName(u"day_number_3")
        self.day_number_3.setStyleSheet(u"border:none;")
        self.day_number_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_10.addWidget(self.day_number_3, 0, 0, 1, 2)

        self.frame_56 = QFrame(self.frame_33)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMinimumSize(QSize(80, 80))
        self.frame_56.setMaximumSize(QSize(80, 80))
        self.frame_56.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_56.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_28 = QGridLayout(self.frame_56)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.forecast2_icon_3 = QLabel(self.frame_56)
        self.forecast2_icon_3.setObjectName(u"forecast2_icon_3")
        self.forecast2_icon_3.setMinimumSize(QSize(40, 40))
        self.forecast2_icon_3.setMaximumSize(QSize(40, 40))
        self.forecast2_icon_3.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast2_icon_3.setScaledContents(True)
        self.forecast2_icon_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_28.addWidget(self.forecast2_icon_3, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_56, 1, 0, 2, 1)

        self.forecast2_high_3 = QLabel(self.frame_33)
        self.forecast2_high_3.setObjectName(u"forecast2_high_3")
        self.forecast2_high_3.setStyleSheet(u"border:none;")

        self.gridLayout_10.addWidget(self.forecast2_high_3, 1, 1, 1, 1)

        self.forecast2_low_3 = QLabel(self.frame_33)
        self.forecast2_low_3.setObjectName(u"forecast2_low_3")
        self.forecast2_low_3.setStyleSheet(u"border:none;")

        self.gridLayout_10.addWidget(self.forecast2_low_3, 2, 1, 1, 1)

        self.forecast2_cloud_3 = QLabel(self.frame_33)
        self.forecast2_cloud_3.setObjectName(u"forecast2_cloud_3")
        self.forecast2_cloud_3.setMinimumSize(QSize(0, 30))
        self.forecast2_cloud_3.setFont(font8)
        self.forecast2_cloud_3.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_10.addWidget(self.forecast2_cloud_3, 4, 0, 1, 2)

        self.forecast2_humid_3 = QLabel(self.frame_33)
        self.forecast2_humid_3.setObjectName(u"forecast2_humid_3")
        self.forecast2_humid_3.setMinimumSize(QSize(0, 30))
        self.forecast2_humid_3.setFont(font8)
        self.forecast2_humid_3.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_10.addWidget(self.forecast2_humid_3, 5, 0, 1, 2)

        self.forecast2_wind_3 = QLabel(self.frame_33)
        self.forecast2_wind_3.setObjectName(u"forecast2_wind_3")
        self.forecast2_wind_3.setMinimumSize(QSize(0, 30))
        self.forecast2_wind_3.setFont(font8)
        self.forecast2_wind_3.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_10.addWidget(self.forecast2_wind_3, 3, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_33)

        self.frame_35 = QFrame(self.frame_14)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"background-color: transparent;\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: 1px solid black;")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_35)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.forecast2_cloud_4 = QLabel(self.frame_35)
        self.forecast2_cloud_4.setObjectName(u"forecast2_cloud_4")
        self.forecast2_cloud_4.setMinimumSize(QSize(0, 30))
        self.forecast2_cloud_4.setFont(font8)
        self.forecast2_cloud_4.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_12.addWidget(self.forecast2_cloud_4, 4, 0, 1, 2)

        self.forecast2_low_4 = QLabel(self.frame_35)
        self.forecast2_low_4.setObjectName(u"forecast2_low_4")
        self.forecast2_low_4.setStyleSheet(u"border:none;")

        self.gridLayout_12.addWidget(self.forecast2_low_4, 2, 1, 1, 1)

        self.frame_57 = QFrame(self.frame_35)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setMinimumSize(QSize(80, 80))
        self.frame_57.setMaximumSize(QSize(80, 80))
        self.frame_57.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_57.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_29 = QGridLayout(self.frame_57)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.forecast2_icon_4 = QLabel(self.frame_57)
        self.forecast2_icon_4.setObjectName(u"forecast2_icon_4")
        self.forecast2_icon_4.setMinimumSize(QSize(40, 40))
        self.forecast2_icon_4.setMaximumSize(QSize(40, 40))
        self.forecast2_icon_4.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast2_icon_4.setScaledContents(True)
        self.forecast2_icon_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_29.addWidget(self.forecast2_icon_4, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.frame_57, 1, 0, 2, 1)

        self.day_number_4 = QLabel(self.frame_35)
        self.day_number_4.setObjectName(u"day_number_4")
        self.day_number_4.setStyleSheet(u"border:none;")
        self.day_number_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_12.addWidget(self.day_number_4, 0, 0, 1, 2)

        self.forecast2_high_4 = QLabel(self.frame_35)
        self.forecast2_high_4.setObjectName(u"forecast2_high_4")
        self.forecast2_high_4.setStyleSheet(u"border:none;")

        self.gridLayout_12.addWidget(self.forecast2_high_4, 1, 1, 1, 1)

        self.forecast2_humid_4 = QLabel(self.frame_35)
        self.forecast2_humid_4.setObjectName(u"forecast2_humid_4")
        self.forecast2_humid_4.setMinimumSize(QSize(0, 30))
        self.forecast2_humid_4.setFont(font8)
        self.forecast2_humid_4.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_12.addWidget(self.forecast2_humid_4, 5, 0, 1, 2)

        self.forecast2_wind_4 = QLabel(self.frame_35)
        self.forecast2_wind_4.setObjectName(u"forecast2_wind_4")
        self.forecast2_wind_4.setMinimumSize(QSize(0, 30))
        self.forecast2_wind_4.setFont(font8)
        self.forecast2_wind_4.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_12.addWidget(self.forecast2_wind_4, 3, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_35)

        self.frame_37 = QFrame(self.frame_14)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"background-color: transparent;\n"
"color: #000000;\n"
"padding: 5px;\n"
"border-radius: 20px;\n"
"border: 1px solid black;")
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_37)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_58 = QFrame(self.frame_37)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setMinimumSize(QSize(80, 80))
        self.frame_58.setMaximumSize(QSize(80, 80))
        self.frame_58.setStyleSheet(u"padding: 5px;\n"
"border: 5px solid rgb(103, 103, 103);\n"
"border-radius: 40px;\n"
"color: rgb(252, 191, 130);")
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_58)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.forecast2_icon_5 = QLabel(self.frame_58)
        self.forecast2_icon_5.setObjectName(u"forecast2_icon_5")
        self.forecast2_icon_5.setMinimumSize(QSize(40, 40))
        self.forecast2_icon_5.setMaximumSize(QSize(40, 40))
        self.forecast2_icon_5.setStyleSheet(u"border: none;\n"
"background: none;")
        self.forecast2_icon_5.setScaledContents(True)
        self.forecast2_icon_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_30.addWidget(self.forecast2_icon_5, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_58, 1, 0, 2, 1)

        self.forecast2_cloud_5 = QLabel(self.frame_37)
        self.forecast2_cloud_5.setObjectName(u"forecast2_cloud_5")
        self.forecast2_cloud_5.setMinimumSize(QSize(0, 30))
        self.forecast2_cloud_5.setFont(font8)
        self.forecast2_cloud_5.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_11.addWidget(self.forecast2_cloud_5, 5, 0, 1, 2)

        self.forecast2_high_5 = QLabel(self.frame_37)
        self.forecast2_high_5.setObjectName(u"forecast2_high_5")
        self.forecast2_high_5.setStyleSheet(u"border:none;")

        self.gridLayout_11.addWidget(self.forecast2_high_5, 1, 1, 1, 1)

        self.day_number_5 = QLabel(self.frame_37)
        self.day_number_5.setObjectName(u"day_number_5")
        self.day_number_5.setStyleSheet(u"border:none;")
        self.day_number_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.day_number_5, 0, 0, 1, 2)

        self.forecast2_low_5 = QLabel(self.frame_37)
        self.forecast2_low_5.setObjectName(u"forecast2_low_5")
        self.forecast2_low_5.setStyleSheet(u"border:none;")

        self.gridLayout_11.addWidget(self.forecast2_low_5, 2, 1, 1, 1)

        self.forecast2_wind_5 = QLabel(self.frame_37)
        self.forecast2_wind_5.setObjectName(u"forecast2_wind_5")
        self.forecast2_wind_5.setMinimumSize(QSize(0, 30))
        self.forecast2_wind_5.setFont(font8)
        self.forecast2_wind_5.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_11.addWidget(self.forecast2_wind_5, 3, 0, 1, 2)

        self.forecast2_humid_5 = QLabel(self.frame_37)
        self.forecast2_humid_5.setObjectName(u"forecast2_humid_5")
        self.forecast2_humid_5.setMinimumSize(QSize(0, 30))
        self.forecast2_humid_5.setFont(font8)
        self.forecast2_humid_5.setStyleSheet(u"color: #000000;border: none;")

        self.gridLayout_11.addWidget(self.forecast2_humid_5, 4, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_37)


        self.verticalLayout_8.addWidget(self.frame_14)


        self.verticalLayout_6.addWidget(self.frame_13)

        self.tabWidget.addTab(self.Daily_forecast, "")

        self.gridLayout_7.addWidget(self.tabWidget, 8, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.main_container)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_5.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Weather app</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Weather forecast", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Current weather", None))
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh data", None))
        self.app_info_button.setText(QCoreApplication.translate("MainWindow", u"About app", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Loading weather location:", None))
        self.current_weather_icon.setText("")
        self.current_weather_label.setText(QCoreApplication.translate("MainWindow", u"Please wait.. ", None))
        self.current_temp_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Please </p><p>wait...</p></body></html>", None))
        self.label_12.setText("")
        self.current_wind_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">please wait..</span></p></body></html>", None))
        self.label_13.setText("")
        self.label_8.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Cloudiness</span></p></body></html>", None))
        self.current_cloud_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">please wait..</span></p></body></html>", None))
        self.current_humidity_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">please wait..</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wind speed</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">Humidity</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nearby cities</span></p></body></html>", None))
        self.nearby_button_1.setText(QCoreApplication.translate("MainWindow", u"City, Country", None))
        self.nearby_button_2.setText(QCoreApplication.translate("MainWindow", u"City, Country", None))
        self.nearby_button_3.setText(QCoreApplication.translate("MainWindow", u"City, Country", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">2024-12-03</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Monday</p></body></html>", None))
        self.label_14.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Time and date</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">00:00</span></p></body></html>", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search location...", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"Current location", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Search location:", None))
        self.pushButton.setText("")
        self.forecast1_icon_1.setText("")
        self.forecast1_temp_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.forecast1_describe_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.hour_number_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_icon_2.setText("")
        self.forecast1_temp_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_3.setText("")
        self.forecast1_temp_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_4.setText("")
        self.forecast1_temp_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_5.setText("")
        self.forecast1_temp_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_6.setText("")
        self.forecast1_temp_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_7.setText("")
        self.forecast1_temp_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_8.setText("")
        self.forecast1_temp_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_9.setText("")
        self.forecast1_temp_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_10.setText("")
        self.forecast1_temp_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_11.setText("")
        self.forecast1_temp_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_12.setText("")
        self.forecast1_temp_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_13.setText("")
        self.forecast1_temp_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_14.setText("")
        self.forecast1_temp_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.forecast1_icon_15.setText("")
        self.forecast1_temp_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">temp</span></p></body></html>", None))
        self.hour_number_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+3 hour</span></p></body></html>", None))
        self.forecast1_describe_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">description</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.three_hour_forecast), QCoreApplication.translate("MainWindow", u"Every 3 hours", None))
        self.forecast2_cloud_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>cloud</p></body></html>", None))
        self.forecast2_high_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>high</p></body></html>", None))
        self.day_number_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">+1 day</p></body></html>", None))
        self.forecast2_low_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>low</p></body></html>", None))
        self.forecast2_icon_1.setText("")
        self.forecast2_wind_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>wind</p></body></html>", None))
        self.forecast2_humid_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>humid</p></body></html>", None))
        self.forecast2_cloud_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>cloud</p></body></html>", None))
        self.forecast2_low_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>low</p></body></html>", None))
        self.forecast2_high_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>high</p></body></html>", None))
        self.forecast2_icon_2.setText("")
        self.day_number_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">+1 day</p></body></html>", None))
        self.forecast2_wind_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>wind</p></body></html>", None))
        self.forecast2_humid_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>humid</p></body></html>", None))
        self.day_number_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+1 day</span></p></body></html>", None))
        self.forecast2_icon_3.setText("")
        self.forecast2_high_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">high </span></p></body></html>", None))
        self.forecast2_low_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">low </span></p></body></html>", None))
        self.forecast2_cloud_3.setText(QCoreApplication.translate("MainWindow", u"cloud ", None))
        self.forecast2_humid_3.setText(QCoreApplication.translate("MainWindow", u"humid", None))
        self.forecast2_wind_3.setText(QCoreApplication.translate("MainWindow", u"wind ", None))
        self.forecast2_cloud_4.setText(QCoreApplication.translate("MainWindow", u"cloud ", None))
        self.forecast2_low_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">low </span></p></body></html>", None))
        self.forecast2_icon_4.setText("")
        self.day_number_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+1 day</span></p></body></html>", None))
        self.forecast2_high_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">high </span></p></body></html>", None))
        self.forecast2_humid_4.setText(QCoreApplication.translate("MainWindow", u"humid", None))
        self.forecast2_wind_4.setText(QCoreApplication.translate("MainWindow", u"wind ", None))
        self.forecast2_icon_5.setText("")
        self.forecast2_cloud_5.setText(QCoreApplication.translate("MainWindow", u"cloud ", None))
        self.forecast2_high_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">high </span></p></body></html>", None))
        self.day_number_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#000000;\">+1 day</span></p></body></html>", None))
        self.forecast2_low_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#000000;\">low </span></p></body></html>", None))
        self.forecast2_wind_5.setText(QCoreApplication.translate("MainWindow", u"wind ", None))
        self.forecast2_humid_5.setText(QCoreApplication.translate("MainWindow", u"humid", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Daily_forecast), QCoreApplication.translate("MainWindow", u"Daily", None))
    # retranslateUi

