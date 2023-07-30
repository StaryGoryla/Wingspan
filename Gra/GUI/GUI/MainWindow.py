import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI2 import Ui_MainWindow
from Register import Ui_RegisterWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

        self.ui.homebutton.clicked.connect(self.showHome)
        self.ui.profilebutton.clicked.connect(self.showProfile)
        self.ui.gamebutton.clicked.connect(self.showGame)
        self.ui.statsbutton.clicked.connect(self.showStats)
        self.ui.registerbutton.clicked.connect(self.showRegister)

    def show(self):
        self.main_win.show()

    def showHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

    def showGame(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Game)

    def showProfile(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Profile)

    def showStats(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Stats)

    def showRegister(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

