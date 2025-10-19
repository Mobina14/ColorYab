import sys
import pyperclip
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow, QLabel, QVBoxLayout, QComboBox, QPushButton, QWidget, QHBoxLayout,QAction,QColorDialog,QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QTimer
from PIL import ImageGrab

class ColorPickerApp(QWidget):
    def __init__(self):
        
        super().__init__()

        self.setWindowTitle('Color Detector')
        self.setGeometry(100, 100, 400, 200)

        self.color_label = QLabel()
        self.color_label.setFixedSize(100, 100)
        self.color_label.setStyleSheet('background-color: #000000')

        self.color_code_label_Hex = QLabel('Hex Code: #000000')
        self.color_code_label_Hex.setStyleSheet('font-size: 16px;')

       

        self.color_code_label_RGB = QLabel('RGB Code:(0,0,0)')
        self.color_code_label_RGB.setStyleSheet('font-size: 16px;')
        

        self.color_code_label_HSV = QLabel('HSV Code: (0,0,0)')
        self.color_code_label_HSV.setStyleSheet('font-size: 16px;')



        self.color_format_combo = QComboBox()
        self.color_format_combo.addItems(['Hex', 'RGB', 'HSV'])

        self.copy_button = QPushButton('Copy to Clipboard')
        self.copy_button.clicked.connect(self.copy_to_clipboard)

        layout = QVBoxLayout()
        color_layout = QHBoxLayout()
        color_code_layout=QVBoxLayout()

        color_code_layout.addWidget(self.color_code_label_Hex)
        
        color_code_layout.addWidget(self.color_code_label_RGB)
        
        color_code_layout.addWidget(self.color_code_label_HSV)        
        
        color_layout.addWidget(self.color_label)
        
        color_layout.addLayout(color_code_layout)
        
        
        layout.addLayout(color_layout)
        layout.addWidget(self.color_format_combo)
        layout.addWidget(self.copy_button)

        self.setLayout(layout)

        
        self.shortcut = QtWidgets.QShortcut(Qt.Key_Return, self)
        self.shortcut.activated.connect(self.toggle_color_tracking)

        self.current_color = QColor(0, 0, 0)
        self.tracking = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.track_color)
        
        QMessageBox.information(self,"info","You can activate the program by pressing the Enter button \nand then move the mouse over the desired color\n to get its color.After reaching the color, click Enter again \nto fix it and you can copy it.")

    def toggle_color_tracking(self):
        if self.tracking:
            self.timer.stop()
            self.tracking = False
        else:
            self.timer.start(10)  
            self.tracking = True

    def track_color(self):
        
        pos = QtGui.QCursor.pos()
        screenshot = ImageGrab.grab(bbox=(pos.x(), pos.y(), pos.x() + 1, pos.y() + 1))
        color = screenshot.getpixel((0, 0))
        self.current_color = QColor(color[0], color[1], color[2])

        self.color_label.setStyleSheet(f'background-color: {self.current_color.name()}')

        self.update_color_code_label()

    def update_color_code_label(self):
        global color_code_hex,color_code_rgb,color_code_hsv
     
        
        color_code_hex = self.current_color.name()
        color_code_rgb = f'({self.current_color.red()}, {self.current_color.green()}, {self.current_color.blue()})'
        hsv = self.current_color.getHsv()
        color_code_hsv = f'({hsv[0]}, {hsv[1]}, {hsv[2]})'

        self.color_code_label_Hex.setText(f'Hex Code: {color_code_hex}')
        self.color_code_label_RGB.setText(f'RGB Code: {color_code_rgb}')
        self.color_code_label_HSV.setText(f'HSV Code: {color_code_hsv}')

    def copy_to_clipboard(self):
        
        selected_format = self.color_format_combo.currentText()
        if selected_format == 'Hex':
            pyperclip.copy(color_code_hex)
            
        elif selected_format == 'RGB':
            pyperclip.copy(color_code_rgb)
            
        elif selected_format == 'HSV':
            pyperclip.copy(color_code_hsv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    picker = ColorPickerApp()
    picker.setFixedSize(350,200)
    picker.move(800,300)
    picker.show()
    sys.exit(app.exec_())
