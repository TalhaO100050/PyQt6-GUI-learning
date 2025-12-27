from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout

from PyQt6.QtGui import QFont

class BasicCalculator(QWidget):

    def __init__(self):
        super().__init__()

        ##App settings
        self.setWindowTitle("Simple Calculator")
        self.setFixedSize(250,350)

        ##Create objects
        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32))
        self.text_box.setStyleSheet("QLineEdit {background-color: #625478; color: #1F1D36}")

        self.grid = QGridLayout()

        self.clear = QPushButton("C")
        self.clear.setStyleSheet("QPushButton {font: 18pt Helvetica; background-color: #625478; color: #1F1D36}")
        self.delete = QPushButton("<")
        self.delete.setStyleSheet("QPushButton {font: 18pt Helvetica; background-color: #625478; color: #1F1D36}")

        #Creating the buttons
        self.buttons = ["7", "8", "9", "/",
                        "6", "5", "4", "*",
                        "3", "2", "1", "-",
                        "0", ".", "=", "+"]

        row = 0
        col = 0

        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton {font: 20pt Helvetica; padding: 5px; background-color: #625478; color: #1F1D36}")
            self.grid.addWidget(button, row, col)

            col += 1
            if col == 4:
                col = 0
                row += 1

        ##Design
        master_layout = QVBoxLayout()

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear, alignment=Qt.AlignmentFlag.AlignCenter)
        button_row.addWidget(self.delete, alignment=Qt.AlignmentFlag.AlignCenter)

        master_layout.addWidget(self.text_box, alignment=Qt.AlignmentFlag.AlignCenter)
        master_layout.addLayout(self.grid)
        master_layout.addLayout(button_row)

        master_layout.setContentsMargins(15,15,15,15)

        self.setLayout(master_layout)

        ##Functions
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    #Calculating function
    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try:
                for i in self.text_box.text():
                    if i not in self.buttons:
                        raise ValueError("Invalid character")
                res = eval(self.text_box.text())
                self.text_box.setText(str(res))
            except Exception as e:
                self.text_box.setText("Error")

        elif text == "C":
            self.text_box.clear()
        
        elif text == "<":
            self.text_box.setText(self.text_box.text()[:-1])

        else:
            self.text_box.setText(self.text_box.text() + text)

##Start app
if __name__ == "__main__":
    app = QApplication([])
    main_window = BasicCalculator()
    main_window.setStyleSheet("QWidget {background-color: #1F1D36}")
    main_window.show()
    app.exec()