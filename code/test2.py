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
        lay.setRowMinimumHeight(1, 100)
        lay.setColumnMinimumWidth(0, 100)
        lay.setHorizontalSpacing(1000)
        lay.setColumnStretch(1, 50)

        # Creating a button and a label
        button = QtWidgets.QPushButton("click me!")
        combo_box = QtWidgets.QComboBox()
        combo_box.addItem("Option 1")
        button2 = QtWidgets.QPushButton("click me too!")
        button_label = QtWidgets.QLabel("Click the button")
        combo_box_label = QtWidgets.QLabel("Choose an option")

        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setMarkdown(
            "## Tutorial \n You can use markdown in this text edit: \n``` py\nprint('Hello, PySide6!')\n``` "
        )
        self.text_edit.setFontItalic(True)
        self.text_edit.append("\nIt is also possible to have text in italic.")
        self.text_edit.setFontPointSize(5)
        self.text_edit.append("\nAnd to have text in a different size.")

        lay.setHorizontalSpacing(10)
        lay.setVerticalSpacing(0)
        lay.addWidget(button_label, 0, 0)
        lay.addWidget(combo_box_label, 0, 1)
        lay.addWidget(button, 1, 0)
        lay.addWidget(combo_box, 1, 1)
        lay.addWidget(button2, 2, 0)
        lay.addWidget(self.text_edit, 2, 1)

        # Connecting the button to the slot function
        button.clicked.connect(self.zoom)

    @Slot()
    def zoom(self):
        self.text_edit.zoomIn(2)
        print(self.text_edit.toPlainText())
        self.text_edit.toMarkdown()


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = UserInterface()
    window.show()
    app.exec()
