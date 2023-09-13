import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets, QtCore
from GUI import Ui_MainWindow
from Register import Ui_RegisterWindow
from PyQt5.QtCore import QThread, pyqtSignal
import requests
import asyncio
import websockets


class ClientThread(QThread):
    server_online = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.server_url = 'http://127.0.0.1:8000/website/home/'
        self.running = True
        self.logged = False
        self.chat_windows = []

    def run(self):
        while self.running and not self.logged:
            try:
                response = requests.get(self.server_url)
                if response.status_code == 200:
                    self.server_online.emit(True)
                else:
                    self.server_online.emit(False)
            except Exception as e:
                print(f"Connection error: {e}")
                self.server_online.emit(False)

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
        self.chat_windows = []

        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

        self.ui.homebutton.clicked.connect(self.showHome)
        self.ui.profilebutton.clicked.connect(self.showProfile)
        self.ui.gamebutton.clicked.connect(self.showGame)
        self.ui.statsbutton.clicked.connect(self.showStats)
        self.ui.registerbutton.clicked.connect(self.showRegister)
        self.ui.loginbutton.clicked.connect(self.login_clicked)
        self.ui.logout_button.clicked.connect(self.logout_clicked)
        self.ui.channelbutton.clicked.connect(self.open_channel)

        self.client_thread = ClientThread()
        self.client_thread.server_online.connect(self.if_server_running)
        self.client_thread.start()

        self.ui.login_box.setVisible(False)

        self.ui.logout_button.setVisible(False)
        self.ui.profilebutton.setVisible(False)
        self.ui.gamebutton.setVisible(False)
        self.ui.statsbutton.setVisible(False)

        self.register_window = None

    def if_server_running(self, connected):
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
        print(response)
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

    def open_channel(self):
        channel_name = self.ui.channel_line.text()
        for window in self.chat_windows:
            if window.channel_name == channel_name:
                window.show()
                return

        chat_window = ChatWindow(channel_name)
        chat_window.closed.connect(self.remove_chat_window)
        self.chat_windows.append(chat_window)
        chat_window.show()
        self.ui.channel_line.clear()

    def remove_chat_window(self, channel_name):
        for window in self.chat_windows:
            if window.channel_name == channel_name:
                self.chat_windows.remove(window)
                return


class ChatWindow(QtWidgets.QWidget):
    closed = QtCore.pyqtSignal(str)

    def __init__(self, channel_name):
        super().__init__()
        self.channel_name = channel_name
        self.init_ui()
        self.websocket = None

    def init_ui(self):
        self.setWindowTitle(f"Chat - {self.channel_name}")
        self.setGeometry(100, 100, 800, 600)
        asyncio.get_event_loop().run_until_complete(self.connect_to_websocket())

    async def connect_to_websocket(self):
        uri = f"ws://127.0.0.1:8000/chat/{self.channel_name}/"
        print(uri)

        try:
            print(uri)
            self.websocket = await websockets.connect(uri)
        except Exception as e:
            # Obsłuż błąd połączenia
            print(f"WebSocket connection error: {e}")

    def closeEvent(self, event):
        if self.websocket:
            asyncio.get_event_loop().run_until_complete(self.websocket.close())

        self.closed.emit(self.channel_name)
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())