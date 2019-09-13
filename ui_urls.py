
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
import re
import handleurl


class UiURLS(QMainWindow):

    def __init__(self):
        super().__init__()
        self.textbox = QLineEdit(self)
        self.button = QPushButton('Submit', self)
        self.closeButton = QPushButton('Close', self)
        self.title = 'CGI task'
        self.left = 500
        self.top = 225
        self.width = 350
        self.height = 300
        self.provide_urls()

    def provide_urls(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox.move(30, 30)
        self.textbox.resize(300, 150)

        # Create a submit button in the window
        self.button.move(25, 200)
        # Create a close button in the window
        self.closeButton.move(200, 200)

        # Connect button to on_click function
        self.button.clicked.connect(self.on_click)
        self.closeButton.clicked.connect(self.close_window)
        self.show()

    def close_window(self):
        self.close()

    @pyqtSlot()
    def on_click(self):
        url_values = self.textbox.text()
        user_urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(url_values))
        handleurl.create_csv_file()
        handleurl.update_csv_file(handleurl.parse_urls(user_urls))
        self.textbox.setText("")
        return



