---
hide:
  - toc
---


In this tutorial, we will cover the steps to create a simple GUI application using PySide6. We will create a simple window with a button and a label. When the button is clicked, the label will display a message. First, it is necessary to install PySide6. Installation instructions can be found [here](../Installation_Guide.md). 

For this tutorial, we will only use the widgets inherited from the [`QtWidgets`](../QtWidgets)  class and the `Slot` class from the `QtCore` module. As a starting point let's create a new Python file `simple_gui.py` and import the necessary modules:

``` py title="simple_gui.py" linenums="1"
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
    <li><a href="creating_a_simple_window">1.</a> Create an empty window </li>
    <li><a href="adding_widgets_to_a_window">2.</a> Add the button and label widgets to the window </li>
    <li><a href="connecting_widgets_to_a_function">3.</a> Connect the button to a function that changes the label text </li>
</ul>

<br>

