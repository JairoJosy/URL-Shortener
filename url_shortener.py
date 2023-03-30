import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy, QMessageBox
from PyQt5.QtGui import QPalette, QColor, QIcon, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pyshorteners

# Create a GUI using PyQt5
class UrlShortener(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the background color of the GUI
        self.setAutoFillBackground(True)
        pal = self.palette()
        pal.setColor(QPalette.Window, QColor(53, 53, 53))
        pal.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(pal)

        # Create the labels, text input box, and button for the GUI
        self.url_label = QLabel('Enter URL to shorten:', self)
        self.url_label.setStyleSheet('color: white')
        self.url_label.setFont(QFont('Arial', 16))
        self.url_input = QLineEdit(self)
        self.url_input.setFont(QFont('Arial', 16))
        self.url_input.setFixedWidth(400)
        self.shortened_label = QLabel(self)
        self.shortened_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.shortened_label.setAlignment(Qt.AlignCenter)
        self.shortened_label.setStyleSheet('color: yellow; font-weight: bold;')
        self.shortened_label.setFont(QFont('Arial', 20))
        self.shorten_button = QPushButton('Shorten URL', self)
        self.shorten_button.setStyleSheet('background-color: #4CAF50; color: white')
        self.shorten_button.setFont(QFont('Arial', 16))
        self.shorten_button.setFixedWidth(200)
        self.shorten_button.clicked.connect(self.shorten_url)
        
        # Create the copy icon button
        self.copy_button = QPushButton(QIcon('copy_icon.png'), '', self)
        self.copy_button.setToolTip('Copy Shortened URL')
        self.copy_button.setStyleSheet('background-color: transparent')
        self.copy_button.setFixedWidth(40)
        self.copy_button.clicked.connect(self.copy_url)

        # Create the layout for the GUI
        hbox = QHBoxLayout()
        hbox.addWidget(self.url_label)
        hbox.addWidget(self.url_input)
        hbox.addWidget(self.shorten_button)
        hbox.addWidget(self.copy_button)
        hbox.setSpacing(20)
        hbox.setContentsMargins(40, 40, 40, 40)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.shortened_label)
        vbox.setContentsMargins(40, 40, 40, 40)
        self.setLayout(vbox)
        self.setWindowTitle('URL Shortener')
        self.setGeometry(200, 200, 800, 400)
        self.show()

    def shorten_url(self):
        # Get the URL entered by the user
        url = self.url_input.text()

        # Shorten the URL using bit.ly and pyshorteners
        s = pyshorteners.Shortener(api_key='YOUR_BITLY_API_KEY_HERE')
        shortened_url = s.bitly.short(url)

        # Display the shortened URL in the GUI
        self.shortened_label.setText(shortened_url)

    def copy_url(self):
        # Get the shortened URL
        shortened_url = self.shortened_label.text()

        # Copy the shortened URL to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(shortened_url)

        # Animate the copy button to slowly disappear and show "Copied"
        self.copy_button.setIcon(QIcon())
        self.copy_button.setText('Copied')
        self.copy_button.setEnabled(False)
        self.copy_button.setGraphicsEffect(QGraphicsOpacityEffect(self.copy_button))
        self.opacity_animation = QPropertyAnimation(self.copy_button.graphicsEffect(), b"opacity")
        self.opacity_animation.setDuration(2000)
        self.opacity_animation.setStartValue(1.0)
        self.opacity_animation.setEndValue(0.0)
        self.opacity_animation.finished.connect(self.reset_copy_button)
        self.opacity_animation.start()

    def reset_copy_button(self):
        # Reset the copy button to its original state
        self.copy_button.setIcon(QIcon('copy_icon.png'))
        self.copy_button.setText('')
        self.copy_button.setEnabled(True)
        self.copy_button.setGraphicsEffect(None)




if __name__ == '__main__':
    # Start the GUI
    app = QApplication(sys.argv)
    ex = UrlShortener()
    sys.exit(app.exec_())
