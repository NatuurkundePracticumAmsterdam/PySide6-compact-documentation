---
hide:
  - navigation
---


In this tutorial, we will cover the steps to create a simple GUI application using PySide6. We will create a simple window with a button and a label. When the button is clicked, the label will display a message. First, it is necessary to install PySide6. Installation instructions can be found [here](Installation_Guide.md). 

For this tutorial, we will only use the widgets inherited from the `QtWidgets` class and the `Slot` class from the `QtCore` module. As a starting point let's create a new Python file `simple_gui.py` and import the necessary modules:

``` py title="simple_gui.py"
import PySide6.QtWidgets as QtWidgets
from PySide6.QtCore import Slot
```

`QtWidgets` contains all the classes that provide a set of elements to create a graphical user interface, such as buttons, labels and layouts. Some of the most common classes from `QtWidgets` are documented in the [API reference](../QtWidgets). We will use the import statements above as a starting point for our code and build upon it. We will build `simple_gui.py` in three steps:

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

If we want to create an empty window, we need two ingredients: a [`QApplication`](../QtWidgets/QApplication) object and a [`QMainWindow`](../QtWidgets/QMainWindow) object. The `QApplication` object manages the GUI application's control flow and main settings, while the `QMainWindow` object provides the framework for building an application's user interface. 

```python title="simple_gui.py"
import PySide6.QtWidgets as QtWidgets
from PySide6.QtCore import Slot


app = QtWidgets.QApplication()
window = QtWidgets.QMainWindow()
window.show()
app.exec()
```

The code above creates an empty window. The [`show()`](../QtWidgets/QMainWindow/#QtWidgets.QMainWindow.show) method displays the window, and the [`exec()`](../QtWidgets/QApplication/#QtWidgets.QApplication.exec) method starts the application's event loop. The event loop is a loop that waits for events to happen and then dispatches them to the appropriate event handlers. Adding the above code to the script will show an empty window:

<img src="../images/empty_window.png" alt="Empty window" width="300">


<br>
<hr>

## 2. Adding widgets to the window

To add widgets to the window, we need to create the widgets and set their properties. In this case, we will add a layout to the window and then add a button and a label to the layout. 


<br>
<hr>

## 3. Connecting widgets to a function

<br>
<br>