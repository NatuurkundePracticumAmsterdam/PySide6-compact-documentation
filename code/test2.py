import PySide6.QtWidgets as QtWidgets
from PySide6.QtCore import Slot


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting the central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Adding a layout to the central widget
        lay = QtWidgets.QGridLayout()
        central_widget.setLayout(lay)

        # Creating a button and a label
        button = QtWidgets.QPushButton("click me!")
        combo_box = QtWidgets.QComboBox()
        combo_box.addItem("Option 1")
        button2 = QtWidgets.QPushButton("click me too!")
        button_label = QtWidgets.QLabel("Click the button")
        combo_box_label = QtWidgets.QLabel("Choose an option")

        lay.setHorizontalSpacing(10)
        lay.setVerticalSpacing(0)
        lay.addWidget(button_label, 0, 0)
        lay.addWidget(combo_box_label, 0, 1)
        lay.addWidget(button, 1, 0)
        lay.addWidget(combo_box, 1, 1)
        lay.addWidget(button2, 2, 0)

        # Connecting the button to the slot function
        button.clicked.connect(self.change_label_text)

    @Slot()
    def change_label_text(self):
        self.label.setText("Hello, PySide6!")


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = UserInterface()
    window.show()
    app.exec()
