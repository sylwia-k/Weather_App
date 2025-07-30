import sys
import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from weather import Ui_MainWindow as WeatherUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 350, 450))
        self.label.setStyleSheet("background-color:rgb(105, 145, 97);\n"
                                 "border-radius:20px;\n"
                                 "")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgb(105, 145, 97);\n"
                                      "\n"
                                      "border-radius:20px;")
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(70, 120, 251, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "none"
        city = self.plainTextEdit.toPlainText()

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        self.weather_window = QtWidgets.QMainWindow()
        self.weather_ui = WeatherUi()
        self.weather_ui.setupUi(self.weather_window, city)

        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("Try again")
        else:

            self.weather_window.show()
            QtWidgets.QApplication.activeWindow().close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate(
            "MainWindow", "City not found, try again."))
        self.pushButton.setText(_translate("MainWindow", "Check"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
