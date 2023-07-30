# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 100, 631, 481))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setObjectName("Home")
        self.home_label = QtWidgets.QLabel(self.Home)
        self.home_label.setGeometry(QtCore.QRect(140, 70, 191, 171))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.home_label.setFont(font)
        self.home_label.setAlignment(QtCore.Qt.AlignCenter)
        self.home_label.setObjectName("home_label")
        self.stackedWidget.addWidget(self.Home)
        self.Game = QtWidgets.QWidget()
        self.Game.setObjectName("Game")
        self.game_label = QtWidgets.QLabel(self.Game)
        self.game_label.setGeometry(QtCore.QRect(110, 90, 261, 161))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.game_label.setFont(font)
        self.game_label.setAlignment(QtCore.Qt.AlignCenter)
        self.game_label.setObjectName("game_label")
        self.stackedWidget.addWidget(self.Game)
        self.Register = QtWidgets.QWidget()
        self.Register.setObjectName("Register")
        self.reg_login_label = QtWidgets.QLabel(self.Register)
        self.reg_login_label.setGeometry(QtCore.QRect(140, 120, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reg_login_label.setFont(font)
        self.reg_login_label.setObjectName("reg_login_label")
        self.reg_email_line = QtWidgets.QLineEdit(self.Register)
        self.reg_email_line.setGeometry(QtCore.QRect(230, 140, 151, 20))
        self.reg_email_line.setObjectName("reg_email_line")
        self.reg_email_label = QtWidgets.QLabel(self.Register)
        self.reg_email_label.setGeometry(QtCore.QRect(140, 140, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reg_email_label.setFont(font)
        self.reg_email_label.setObjectName("reg_email_label")
        self.reg_logine_line = QtWidgets.QLineEdit(self.Register)
        self.reg_logine_line.setGeometry(QtCore.QRect(230, 120, 151, 20))
        self.reg_logine_line.setObjectName("reg_logine_line")
        self.reg_pass_label = QtWidgets.QLabel(self.Register)
        self.reg_pass_label.setGeometry(QtCore.QRect(140, 160, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reg_pass_label.setFont(font)
        self.reg_pass_label.setObjectName("reg_pass_label")
        self.reg_confirm_line = QtWidgets.QLineEdit(self.Register)
        self.reg_confirm_line.setGeometry(QtCore.QRect(230, 180, 151, 20))
        self.reg_confirm_line.setObjectName("reg_confirm_line")
        self.password_label_3 = QtWidgets.QLabel(self.Register)
        self.password_label_3.setGeometry(QtCore.QRect(140, 180, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label_3.setFont(font)
        self.password_label_3.setObjectName("password_label_3")
        self.reg_passline = QtWidgets.QLineEdit(self.Register)
        self.reg_passline.setGeometry(QtCore.QRect(230, 160, 151, 20))
        self.reg_passline.setObjectName("reg_passline")
        self.reg_regbutton = QtWidgets.QPushButton(self.Register)
        self.reg_regbutton.setGeometry(QtCore.QRect(280, 220, 75, 23))
        self.reg_regbutton.setObjectName("reg_regbutton")
        self.reg_cancelbutton = QtWidgets.QPushButton(self.Register)
        self.reg_cancelbutton.setGeometry(QtCore.QRect(160, 220, 75, 23))
        self.reg_cancelbutton.setObjectName("reg_cancelbutton")
        self.stackedWidget.addWidget(self.Register)
        self.Profile = QtWidgets.QWidget()
        self.Profile.setObjectName("Profile")
        self.profile_label = QtWidgets.QLabel(self.Profile)
        self.profile_label.setGeometry(QtCore.QRect(110, 100, 241, 151))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.profile_label.setFont(font)
        self.profile_label.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_label.setObjectName("profile_label")
        self.stackedWidget.addWidget(self.Profile)
        self.Stats = QtWidgets.QWidget()
        self.Stats.setObjectName("Stats")
        self.stats_label = QtWidgets.QLabel(self.Stats)
        self.stats_label.setGeometry(QtCore.QRect(100, 100, 241, 171))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.stats_label.setFont(font)
        self.stats_label.setAlignment(QtCore.Qt.AlignCenter)
        self.stats_label.setObjectName("stats_label")
        self.stackedWidget.addWidget(self.Stats)
        self.homebutton = QtWidgets.QPushButton(self.centralwidget)
        self.homebutton.setGeometry(QtCore.QRect(230, 10, 75, 23))
        self.homebutton.setObjectName("homebutton")
        self.statsbutton = QtWidgets.QPushButton(self.centralwidget)
        self.statsbutton.setGeometry(QtCore.QRect(310, 40, 75, 23))
        self.statsbutton.setObjectName("statsbutton")
        self.gamebutton = QtWidgets.QPushButton(self.centralwidget)
        self.gamebutton.setGeometry(QtCore.QRect(230, 40, 75, 23))
        self.gamebutton.setObjectName("gamebutton")
        self.profilebutton = QtWidgets.QPushButton(self.centralwidget)
        self.profilebutton.setGeometry(QtCore.QRect(310, 10, 75, 23))
        self.profilebutton.setObjectName("profilebutton")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 10, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(410, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_label.setFont(font)
        self.login_label.setObjectName("login_label")
        self.login_line = QtWidgets.QLineEdit(self.centralwidget)
        self.login_line.setGeometry(QtCore.QRect(500, 10, 151, 20))
        self.login_line.setObjectName("login_line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(500, 30, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(410, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.registerbutton = QtWidgets.QPushButton(self.centralwidget)
        self.registerbutton.setGeometry(QtCore.QRect(520, 50, 131, 23))
        self.registerbutton.setObjectName("registerbutton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home_label.setText(_translate("MainWindow", "Home page"))
        self.game_label.setText(_translate("MainWindow", "Stats"))
        self.reg_login_label.setText(_translate("MainWindow", "Login:"))
        self.reg_email_line.setText(_translate("MainWindow", "e-mail"))
        self.reg_email_label.setText(_translate("MainWindow", "E-mail"))
        self.reg_logine_line.setText(_translate("MainWindow", "login"))
        self.reg_pass_label.setText(_translate("MainWindow", "Password:"))
        self.reg_confirm_line.setText(_translate("MainWindow", "password"))
        self.password_label_3.setText(_translate("MainWindow", "Password:"))
        self.reg_passline.setText(_translate("MainWindow", "password"))
        self.reg_regbutton.setText(_translate("MainWindow", "Register!"))
        self.reg_cancelbutton.setText(_translate("MainWindow", "Cancel"))
        self.profile_label.setText(_translate("MainWindow", "Game"))
        self.stats_label.setText(_translate("MainWindow", "Profile"))
        self.homebutton.setText(_translate("MainWindow", "Home"))
        self.statsbutton.setText(_translate("MainWindow", "Stats"))
        self.gamebutton.setText(_translate("MainWindow", "Game"))
        self.profilebutton.setText(_translate("MainWindow", "Profile"))
        self.title_label.setText(_translate("MainWindow", "Wingspan"))
        self.login_label.setText(_translate("MainWindow", "Login:"))
        self.login_line.setText(_translate("MainWindow", "login"))
        self.lineEdit.setText(_translate("MainWindow", "password"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.registerbutton.setText(_translate("MainWindow", "No account yet? Sign up!"))
        self.pushButton.setText(_translate("MainWindow", "Sign in!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

