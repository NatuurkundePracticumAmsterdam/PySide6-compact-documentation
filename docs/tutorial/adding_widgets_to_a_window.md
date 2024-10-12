To add widgets to the window, we need to create the widgets and set their properties. In this case, we will first add a central widget to the window, then add a layout to the central widget, and finally add a button and a label to the layout.

<hr>

## Adding a layout

First we need to keep in mind that every [`QMainWindow`](../QtWidgets/QMainWindow.md) has to have a central widget. This usually is a generic [`QWidget`](../QtWidgets/QWidget.md) object. Next, we will add a layout to the central widget. A layout is a container that manages the position of child widgets. In this case, we will use a [`QVBoxLayout`](../QtWidgets/QVBoxLayout.md) ('V' for 'vertical') to manage the position of widgets in our window. The newly added code is highlighted below:

```python title="simple_gui.py" hl_lines="8-14" linenums="1"

from PySide6 import QtWidgets
from PySide6.QtCore import Slot


app = QtWidgets.QApplication()
window = QtWidgets.QMainWindow()

# Setting the central widget 
central_widget = QtWidgets.QWidget()
window.setCentralWidget(central_widget)

# Adding a layout to the central widget
vbox = QtWidgets.QVBoxLayout()
central_widget.setLayout(vbox)

window.show()
app.exec()

```

Running the code above will still show an empty window, as we have added an empty layout to the window. Next, we will add widgets to this layout.

<hr>

## Adding widgets to the layout

We can create a button using the [`QPushButton`](../QtWidgets/QPushButton.md) class and a label using the [`QLabel`](../QtWidgets/QLabel.md) class as follows:

```python 

button = QtWidgets.QPushButton()
button.setText("Click me!")

label = QtWidgets.QLabel()
label.setText("Hello, PySide6!")
```

If we simply add the above code to `simple_gui.py`, the button and label will not be visible. This is because we have not added them to the layout. To add the button and label to the layout, we can use the `#!python addWidget()` method of the layout:

```python
vbox.addWidget(button)	
vbox.addWidget(label)
```

Let's add this code to `simple_gui.py` and see how the window looks:

```python title="simple_gui.py" hl_lines="16-24" linenums="1"

from PySide6 import QtWidgets
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
label.setText("Hello, User! Please click the button.")
button = QtWidgets.QPushButton()
button.setText("Click me!")

# Adding the button and label to the layout
vbox.addWidget(label)
vbox.addWidget(button)

window.show()
app.exec()

```

Running the above code will show a window with a label with a button that does absolutely nothing when clicked (which we will fix in the next step :fontawesome-regular-face-laugh-wink:).

<img src="../images/button_and_label.png" alt="Button and label" width="300">


