#!/bin/python3
# -*- coding: utf-8 -*-

import json, os, sys, urllib.request
from urllib.request import urlopen
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QTimer,QDateTime



class Ui_MainWindow(object):
    '''
    Thas class define for qt and use qt5 in this program.
    '''

    path = os.getcwd() # for get current directory.
    BingURL = 'https://www.bing.com' # base url that bing.com and use for get image .
    namePicture = "" # name picture that use several function.
    link = "" # link download image and it will be added to base url.
    finalPath = "" # final path that save image there.

    def setupUi(self, MainWindow):
        '''
        setup ui qt and set icon and ... there and commend just say this things
        does work where and how use it.
        in this function just define and create ui no any more.
        '''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(516, 209)
        '''
        set object name and create window.
        '''

        icon = QtGui.QIcon('BingWallpaper.png')
        MainWindow.setWindowIcon(icon)
        '''
        set icon for window.
        '''

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.Logo = QtWidgets.QLabel(self.centralwidget)
        self.Logo.setGeometry(QtCore.QRect(30, 120, 130, 75))
        self.Logo.setPixmap(QtGui.QPixmap("BingWallpaperLogo.png"))
        '''
        show logo in window in Coordinates thats defined.
        '''

        self.DownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadButton.setGeometry(QtCore.QRect(379, 10, 121, 25))
        self.DownloadButton.setObjectName("DownloadButton")
        self.DownloadButton.clicked.connect(self.downloadBingWallpaper)
        '''
        create button for downlaod and if click connect to function DownloadBingWallpaper.
        '''

        self.labelDateAndTime = QtWidgets.QLabel(self.centralwidget)
        self.labelDateAndTime.setGeometry(QtCore.QRect(290, 150, 211, 31))
        self.labelDateAndTime.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDateAndTime.setObjectName("labelDateAndTime")
        '''
        create lable thats show date and time.
        '''

        self.labelPath = QtWidgets.QLabel(self.centralwidget)
        self.labelPath.setGeometry(QtCore.QRect(20, 10, 271, 21))
        self.labelPath.setObjectName("labelPath")
        '''
        that lable just show text for explain that you wanna click select button till 
        open dialog.
        '''

        self.DirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.DirectoryButton.setGeometry(QtCore.QRect(290, 10, 80, 25))
        self.DirectoryButton.setObjectName("DirectoryButton")
        self.DirectoryButton.clicked.connect(self.useDialog)
        '''
        define button that clicked connect to function useDialog.
        '''

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 481, 31))
        self.textEdit.setObjectName("textEdit")
        '''
        this textEdit show directory we want to save image.  
        '''

        self.labelExistFile = QtWidgets.QLabel(self.centralwidget)
        self.labelExistFile.setGeometry(QtCore.QRect(20, 80, 361, 31))
        self.labelExistFile.setObjectName("labelExistFile")
        '''
        lable that say to us file exist or not.
        '''

        self.ExistButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExistButton.setGeometry(QtCore.QRect(389, 80, 111, 25))
        self.ExistButton.setObjectName("existButton")
        self.ExistButton.clicked.connect(self.getInfoPage)
        '''
        create button exist till check file exist or not.
        '''

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        '''
        for show time and update in 1s.
        '''


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        '''
        this function define till set text or title for programm.
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BingWallpaper"))
        self.DownloadButton.setText(_translate("MainWindow", "Download"))
        self.labelPath.setText(_translate("MainWindow", "Select Directory For Save Bing Wallpaper :"))
        self.DirectoryButton.setText(_translate("MainWindow", "Select"))
        self.labelExistFile.setText(_translate("MainWindow", "Press Check Till Check File Exist Or Not."))
        self.ExistButton.setText(_translate("MainWindow", "Check"))
 
    def msg(self, message):
        '''
        this function just show massage that we have error or download.
        '''
        icon = QtGui.QIcon('BingWallpaper.png')
        msg = QMessageBox()
        msg.setWindowIcon(icon)
        msg.setWindowTitle("BingWallpaper")
        msg.setText(message)
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        e = msg.exec_()

    def useDialog(self):
        '''
        this function define till show dialog for select directoy we wanna save image.
        '''
        self.path = QFileDialog.getExistingDirectory()
        if self.path:
            '''
            check path is exist or not and then change text edit to select directory.
            '''
            self.textEdit.setText(self.path)

    def showTime(self):
        '''
        for show time in the program.
        '''
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.labelDateAndTime.setText(timeDisplay)

    def checkFileExist(self):
        '''
        this function check file exist in directory or not baecuse if exist replace that file and 
        we dont want lost any file and then show in lable that file has exist or not and if file
        exist we want to rename that file or file dont matter for us.
        '''
        self.finalPath = self.path + "/" + self.namePicture
        if os.path.exists(self.finalPath):
            '''
            this if check file exist or not and change lable text.
            '''
            self.labelExistFile.setText("File Has Exist And Replace That If Downlaod It.")
        else:
            self.labelExistFile.setText("Click Download Button And Wait For Downlaod")

    def getInfoPage(self):
        '''
        this function check image in bing and get url for download and get name image and 
        we after get name and link check in directory for save to exist or not.
        '''
        try:
            URL = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-Us' 
            # url info image bing.
            pageData = json.loads(urlopen(URL).read().decode("utf-8")) 
            # get information page and save in pageData.

            imageDate = pageData['images'] # get information just related to image.
            self.link = imageDate[0]['url'] # get link image.
            name = imageDate[0]['copyright'].split(" (")[0] 
            # get name image and just get name picture for name that be saved.
            name = name + ".jpg" # add format jpg to image.
            self.namePicture = name
            self.checkFileExist() 
        except:
            self.msg("Can't Get Information Of Bing Please Try Again...")

    def downloadBingWallpaper(self):
        '''
        this function download image and send notification that downlaod or not. 
        if download is compelete use notify-send for send notification .
        '''
        try:
            urllib.request.urlretrieve(self.BingURL + self.link, self.finalPath) 
            os.system('notify-send --app-name=APP_NAME: "Bingwallpaper" --icon="$PWD/bing.ico" "Download Finished."')

        except:
            self.msg("Can't Downlaod Bing Wallpaper...")


if __name__ == "__main__":
    '''
    run the program and define main.
    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
