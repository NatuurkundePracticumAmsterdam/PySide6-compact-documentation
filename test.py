import PySide6.QtWidgets as QtWidgets
from PySide6.QtCore import Slot


app = QtWidgets.QApplication()
window = QtWidgets.QMainWindow()

# Setting the central widget
central_widget = QtWidgets.QWidget()
window.setCentralWidget(central_widget)

# Adding a layout to the central widget
vbox = QtWidgets.QVBoxLayout()
central_widget.setLayout(vbox)

# Creating a button and a label
label = QtWidgets.QLabel()
label.setText("Hello, PySide6!")
button = QtWidgets.QPushButton()
button.setText("Click me!")

# Adding the button and label to the layout
vbox.addWidget(label)
vbox.addWidget(button)

window.show()
app.exec()
