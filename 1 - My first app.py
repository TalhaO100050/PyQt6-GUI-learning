from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from random import choice

#App settings 
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("My First App")
main_window.resize(600,400)

#Create all Objects/Widgets below here
title_text = QLabel("Rastgele Kelimeler")
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 = QPushButton("Click me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me!")

#Design
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title_text, alignment=Qt.AlignmentFlag.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignmentFlag.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignmentFlag.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignmentFlag.AlignCenter)

row3.addWidget(button1, alignment=Qt.AlignmentFlag.AlignCenter)
row3.addWidget(button2, alignment=Qt.AlignmentFlag.AlignCenter)
row3.addWidget(button3, alignment=Qt.AlignmentFlag.AlignCenter)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

#Functions
my_words = ["Merhaba", "Dünya", ":)", "Hey", "Help"]

def display_word(label):
    word = choice(my_words)
    label.setText(word)

#Events
button1.clicked.connect(lambda: display_word(text1))
button2.clicked.connect(lambda: display_word(text2))
button3.clicked.connect(lambda: display_word(text3))

#Start app
main_window.show()
app.exec()