---
hide:
  - navigation
---


In this tutorial, we will cover the steps to create a simple GUI application using Pyside6. We will create a simple window with a button and a label. When the button is clicked, the label will display a message. First, it is necessary to install Pyside6. Installation instructions can be found [here](Installation_Guide.md). 

For this tutorial, we will only use the widgets inherited from the `QtWidgets` class and the `Slot` class from the `QtCore` module:

```python

import PySide6.QtWidgets as QtWidgets
from PySide6.QtCore import Slot
```

`QtWidgets` contains all the classes that provide a set of elements to create a graphical user interface, such as buttons, labels and layouts. Some of the most common classes from `QtWidgets` are documented in the [API reference](../QtWidgets). We will use the import statements above as a starting point for our code and build upon it. We will build the GUI application in three steps:

<style>
    ul.no-bullets {
    list-style-type: none; /* Remove bullets */
    padding: 0; /* Remove padding */
    margin: 0; /* Remove margins */
    }
</style>

<ul class="no-bullets">
    <li><a href="#creating-a-simple-window">1.</a> Create an empty window </li>
    <li><a href="#adding-widgets-to-the-window">2.</a> Add the button and label widgets to the window </li>
    <li><a href="#connecting-widgets-to-a-function">3.</a> Connect the button to a function that changes the label text </li>
</ul>

<br>
<hr>
## 1. Creating a simple window

If we want to create an empty window, we need to ingredients: a [`QApplication`](../QtWidgets/QApplication) object and a [`QMainWindow`](../QtWidgets/QMainWindow) object. The `QApplication` object manages the GUI application's control flow and main settings, while the `QMainWindow` object provides a framework for building an application's user interface. 

```python

app = QtWidgets.QApplication()
window = QtWidgets.QMainWindow()
window.show()
app.exec()
```

<br>
<hr>

## 2. Adding widgets to the window

<br>
<hr>

## 3. Connecting widgets to a function

