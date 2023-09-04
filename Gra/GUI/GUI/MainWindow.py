import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets
from GUI import Ui_MainWindow
from Register import Ui_RegisterWindow
from PyQt5.QtCore import QThread, pyqtSignal
import requests

class ClientThread(QThread):
    connection_changed = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.server_url = 'http://127.0.0.1:8000/website/home/'
        self.running = True
        self.logged = False

    def run(self):
        while self.running and not self.logged:
            try:
                response = requests.get(self.server_url)
                if response.status_code == 200:
                    self.connection_changed.emit(True)
                else:
                    self.connection_changed.emit(False)
            except Exception as e:
                print(f"Connection error: {e}")
                self.connection_changed.emit(False)
            self.msleep(5000)

    def stop(self):
        self.running = False

    def on_logging(self):
        self.logged = True

    def on_logging_out(self):
        self.logged = False

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.logged = False

        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

        self.ui.homebutton.clicked.connect(self.showHome)
        self.ui.profilebutton.clicked.connect(self.showProfile)
        self.ui.gamebutton.clicked.connect(self.showGame)
        self.ui.statsbutton.clicked.connect(self.showStats)
        self.ui.registerbutton.clicked.connect(self.showRegister)
        self.ui.loginbutton.clicked.connect(self.login_clicked)
        self.ui.logout_button.clicked.connect(self.logout_clicked)

        self.client_thread = ClientThread()
        self.client_thread.connection_changed.connect(self.on_connection_changed)
        self.client_thread.start()

        self.ui.login_box.setVisible(False)
        self.ui.logout_button.setVisible(False)
        self.ui.profilebutton.setVisible(False)
        self.ui.gamebutton.setVisible(False)
        self.ui.statsbutton.setVisible(False)

        self.register_window = None

    def on_connection_changed(self, connected):
        if connected:
            self.ui.status_label.setVisible(False)
            self.ui.login_box.setVisible(True)
            self.ui.logout_button.setVisible(False)
            self.ui.profilebutton.setVisible(False)
            self.ui.gamebutton.setVisible(False)
            self.ui.statsbutton.setVisible(False)
        else:
            self.ui.status_label.setVisible(True)
            self.ui.login_box.setVisible(False)
            self.ui.logout_button.setVisible(False)
            self.ui.profilebutton.setVisible(False)
            self.ui.gamebutton.setVisible(False)
            self.ui.statsbutton.setVisible(False)

    def login_clicked(self):
        login_url = 'http://127.0.0.1:8000/users/login_gui/'
        username = self.ui.login_line.text()
        password = self.ui.password_line.text()
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(login_url, data=data)
        print("wysłane")
        if response.status_code == 200:
            print("login")
            self.client_thread.on_logging()
            self.ui.login_box.setVisible(False)
            self.ui.logout_button.setVisible(True)
            self.ui.profilebutton.setVisible(True)
            self.ui.gamebutton.setVisible(True)
            self.ui.statsbutton.setVisible(True)
        else:
            print("error")
            QtWidgets.QMessageBox.warning(self.main_win, 'Login error', 'Invalid login or password')

    def logout_clicked(self):
        logout_url = 'http://127.0.0.1:8000/users/logout_gui/'
        response = requests.post(logout_url)
        print('Sent')
        self.client_thread.on_logging_out()

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
        if not self.register_window:
            self.register_window = QtWidgets.QMainWindow()
            self.register_ui = Ui_RegisterWindow()
            self.register_ui.setupUi(self.register_window)
            self.register_ui.reg_cancelbutton_2.clicked.connect(self.closeRegister)
            self.register_window.show()

    def closeRegister(self):
        self.register_window.close()
        self.register_window = None

    def closeEvent(self, event):
        self.client_thread.stop()
        self.client_thread.wait()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

#AAA