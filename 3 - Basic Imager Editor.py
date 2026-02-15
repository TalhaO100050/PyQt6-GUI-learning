from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QListWidget, QComboBox

class BasicImageEditor(QWidget):

    def __init__(self):
        super().__init__()

        ##App settings
        self.setWindowTitle("Simple Image Editor")
        self.resize(900,700)

        ##Create objects

        #Buttons
        self.button_select_folder = QPushButton("Select Folder")
        self.button_left = QPushButton("Left")
        self.button_right = QPushButton("Right")
        self.button_mirror = QPushButton("Mirror")
        self.button_sharpness = QPushButton("Sharpness")
        self.button_grey = QPushButton("Grey")
        self.button_color = QPushButton("Color")
        self.button_contrast = QPushButton("Contrast")
        self.button_blur = QPushButton("Blur")

        #Image list
        self.list_image_list = QListWidget()

        #Effect combo box
        self.combobox_effects = QComboBox()
        self.combobox_effects.addItem("Original")
        self.combobox_effects.addItem("Left")
        self.combobox_effects.addItem("Right")
        self.combobox_effects.addItem("Mirror")
        self.combobox_effects.addItem("Sharpness")
        self.combobox_effects.addItem("Grey")
        self.combobox_effects.addItem("Color")
        self.combobox_effects.addItem("Contrast")
        self.combobox_effects.addItem("Blur")

        #Image
        self.label_image = QLabel("Image will appear here")

        ##Design
        master_layout = QHBoxLayout()
        buttons_column = QVBoxLayout()
        image_column = QVBoxLayout()

        master_layout.addLayout(buttons_column, 20)
        master_layout.addLayout(image_column, 80)

        buttons_column.addWidget(self.button_select_folder)
        buttons_column.addWidget(self.list_image_list)
        buttons_column.addWidget(self.combobox_effects)
        buttons_column.addWidget(self.button_left)
        buttons_column.addWidget(self.button_right)
        buttons_column.addWidget(self.button_mirror)
        buttons_column.addWidget(self.button_sharpness)
        buttons_column.addWidget(self.button_grey)
        buttons_column.addWidget(self.button_color)
        buttons_column.addWidget(self.button_contrast)
        buttons_column.addWidget(self.button_blur)

        image_column.addWidget(self.label_image)

        self.setLayout(master_layout)

#Start app
if __name__ == "__main__":
    app = QApplication([])
    main_window = BasicImageEditor()
    main_window.show()
    app.exec()