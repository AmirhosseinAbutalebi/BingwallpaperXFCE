#!/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer,QDateTime, Qt
import json, os
import urllib.request
from urllib.request import urlopen
import os


class Ui_MainWindow(object):

    path = os.getcwd()
    BingURL = 'https://www.bing.com'
    namePicture = ""
    link = ""
    finalPath = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 209)

        icon = QtGui.QIcon('BingWallpaper.png')
        MainWindow.setWindowIcon(icon)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(30, 120, 130, 75))
        self.Logo.setPixmap(QtGui.QPixmap("BingWallpaperLogo.png"))

        self.DownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadButton.setGeometry(QtCore.QRect(379, 10, 121, 25))
        self.DownloadButton.setObjectName("DownloadButton")
        self.DownloadButton.clicked.connect(self.DownloadBingWallpaper)

        self.labelDateAndTime = QtWidgets.QLabel(self.centralwidget)
        self.labelDateAndTime.setGeometry(QtCore.QRect(290, 150, 211, 31))
        self.labelDateAndTime.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDateAndTime.setObjectName("labelDateAndTime")

        self.labelPath = QtWidgets.QLabel(self.centralwidget)
        self.labelPath.setGeometry(QtCore.QRect(20, 10, 271, 21))
        self.labelPath.setObjectName("labelPath")

        self.DirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.DirectoryButton.setGeometry(QtCore.QRect(290, 10, 80, 25))
        self.DirectoryButton.setObjectName("DirectoryButton")
        self.DirectoryButton.clicked.connect(self.useDialog)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 481, 31))
        self.textEdit.setObjectName("textEdit")

        self.labelExistFile = QtWidgets.QLabel(self.centralwidget)
        self.labelExistFile.setGeometry(QtCore.QRect(20, 80, 361, 31))
        self.labelExistFile.setObjectName("labelExistFile")

        self.ExistButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExistButton.setGeometry(QtCore.QRect(389, 80, 111, 25))
        self.ExistButton.setObjectName("existButton")
        self.ExistButton.clicked.connect(self.getInfoPage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BingWallpaper"))
        self.DownloadButton.setText(_translate("MainWindow", "Download"))
        self.labelPath.setText(_translate("MainWindow", "Select Directory For Save Bing Wallpaper :"))
        self.DirectoryButton.setText(_translate("MainWindow", "Select"))
        self.labelExistFile.setText(_translate("MainWindow", "Press Check Till Check File Exist Or Not."))
        self.ExistButton.setText(_translate("MainWindow", "Check"))
 
    def msg(self, message):
        icon = QtGui.QIcon('BingWallpaper.png')
        msg = QMessageBox()
        msg.setWindowIcon(icon)
        msg.setWindowTitle("BingWallpaper")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        e = msg.exec_()

    def useDialog(self):
        self.path = QFileDialog.getExistingDirectory()
        if self.path:
            self.textEdit.setText(self.path)

    def showTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.labelDateAndTime.setText(timeDisplay)

    def checkFileExist(self):
        self.finalPath = self.path + "/" + self.namePicture
        if os.path.exists(self.finalPath):
            self.labelExistFile.setText("File Has Exist And Replace That If Downlaod It.")
        else:
            self.labelExistFile.setText("Click Download Button And Wait For Downlaod")

    def getInfoPage(self):
        try:
            URL = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-Us'
            pageData = json.loads(urlopen(URL).read().decode("utf-8"))

            imageDate = pageData['images']
            self.link = imageDate[0]['url']
            name = imageDate[0]['copyright'].split(" (")[0]
            name = name + ".jpg"
            self.namePicture = name
            self.checkFileExist()
        except:
            self.msg("Can't Get Information Of Bing Please Try Again...")

    def DownloadBingWallpaper(self):
        try:
            urllib.request.urlretrieve(self.BingURL + self.link, self.finalPath) 
            os.system('notify-send --app-name=APP_NAME: "Bingwallpaper" --icon="$PWD/bing.ico" "Download Finished."')

        except:
            self.msg("Can't Downlaod Bing Wallpaper...")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
