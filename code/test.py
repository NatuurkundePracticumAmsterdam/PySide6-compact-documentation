import PySide6.QtWidgets as QtWidgets
from PySide6.QtCore import Slot


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting the central widget
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # Adding a layout to the central widget
        vbox = QtWidgets.QVBoxLayout()
        central_widget.setLayout(vbox)

        # Creating a button and a label
        self.label = QtWidgets.QLabel()
        self.label.setText("Hello, User! Please click the button.")
        button = QtWidgets.QPushButton()
        button.setText("Click me!")

        # Adding the button and label to the layout
        vbox.addWidget(self.label)
        vbox.addWidget(button)

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
