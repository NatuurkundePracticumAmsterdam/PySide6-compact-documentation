---
hide:
  - toc
  - footer
---

In this API Reference we will cover relevant classes and functions which are part of the `QtWidgets` module. The `QtWidgets` module contains classes that provide a set of UI elements to create classic desktop-style graphical user interfaces (GUI's). The `QWidget` class is the base class for all UI objects, and the `QLayout` class is the base class for all layout objects. An overview of the classes and functions in the `QtWidgets` module is provided at the bottom of this page.


!!! note
    Methods from parent classes (i.e. `QWidget` and `QLayout`) are not repeated in the reference of each subclass. However, as always in Python ( :nerd: ), these methods are applicable to all subclasses. 


!!! note
    Note the difference between **`QtWidgets`** and **`QWidget`**, which are a module and class respectively. Convince yourself by examining the following code:
    ```py 
    from PySide6 import QtWidgets
    from PySide6.QtWidgets import QWidget

    # The following two lines are equivalent:
    widget = QtWidgets.QWidget()
    widget = QWidget()
    ```
    In the above code we create an instance of the `QWidget` in two ways. In practice we do not use direct instances of `QWidget` to build our GUI, but rather use its subclasses (see the list below). 

<hr>

## All classes from the `QtWidgets` module:

  - [`QApplication`](QApplication.md): Manages the GUI application's control flow and main settings.
  - [`QLayout`](QLayout.md): Base class of all layout objects in `QtWidgets`.  
  - [`QWidget`](QWidget.md): Base class of all widget objects in `QtWidgets`.
<br>

- ### Subclasses derived from `QLayout`:
    - [`QHBoxLayout`](QHBoxLayout.md): Manages a horizontal layout of widgets. 
    - [`QVBoxLayout`](QVBoxLayout.md): Manages a vertical layout of other widgets. 
    - [`QGridLayout`](QGridLayout.md): Manages a grid layout where space is divided up into rows and columns.
<br> 

- ### Subclasses derived from `QWidget`:
    - [`QMainWindow`](QMainWindow.md): Provides a framework for building an application's user interface.
    - [`QGroupBox`](QGroupBox.md): Provides a frame, a title on top, and can display various other widgets inside itself.
    - [`QTextEdit`](QTextEdit.md): Displays text and allows the user to edit it.
    - [`QCheckBox`](QCheckBox.md): Toggle button with a checkbox indicator.  
    - [`QLabel`](QLabel.md): A widget that displays text.
    - [`QComboBox`](QComboBox.md): A widget that allows the user to choose from a list of options. 
    - [`QSpinBox`](QSpinBox.md): A widget that allows the user to choose a number from a range.
    - [`QDoubleSpinBox`](QDoubleSpinBox.md): A widget that allows the user to choose a floating-point number from a range.
    - [`QPushButton`](QPushButton.md): A push button that can be clicked by the user.

<br>
<br>
