To make a widget interactive, you need to connect it to a function. We can do this by using a signal-slot mechanism. A signal is emitted when a particular event occurs, and a slot is a function that is called in response to the signal. In PySide6, you can connect a signal to a slot using the `connect` method of the signal object. 

<hr>


## Creating a slot function

The slot function doesn't take any arguments. To handle this, we can group all the widgets together with all slot functions in a single class. This way, we can access the widgets inside the slot function through the `self` reference. Assuming that the following code is inside a class in which a [`QLabel`](../../QtWidgets/Qlabel) widget is defined as `self.label`, we can define a slot function as follows:


```python
@Slot()
def change_label_text(self):
    self.label.setText("Hello, PySide6!")
```

In the code above, we use the `@Slot()` decorator to indicate that the function is a slot. So, if we want to connect this slot function to the signal of the `QPushButton` in our `simple_gui.py` file, we first need to change up our code quite a bit. We can put all the code in a class that inherits from [`QMainWindow`](../../QtWidgets/QMainWindow) and let's call it `UserInterface`: 

=== "Without class"

    ```python title="simple_gui.py" linenums="1"
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
    label.setText("Hello, User! Please click the button.")
    button = QtWidgets.QPushButton()
    button.setText("Click me!")

    # Adding the button and label to the layout
    vbox.addWidget(label)
    vbox.addWidget(button)

    window.show()
    app.exec()
    ```

===+ "With class"


    ```python title="simple_gui.py" linenums="1" hl_lines="5-7 11 18-19 24 28-30" 

    import PySide6.QtWidgets as QtWidgets
    from PySide6.QtCore import Slot


    class UserInterface(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__() # (1)

            # Setting the central widget 
            central_widget = QtWidgets.QWidget()
            self.setCentralWidget(central_widget) # (2)

            # Adding a layout to the central widget
            vbox = QtWidgets.QVBoxLayout()
            central_widget.setLayout(vbox)

            # Creating a button and a label
            self.label = QtWidgets.QLabel() 
            self.label.setText("Hello, User! Please click the button.") # (3)
            button = QtWidgets.QPushButton()
            button.setText("Click me!")

            # Adding the button and label to the layout
            vbox.addWidget(self.label)
            vbox.addWidget(button)


    if __name__ == "__main__": # (4)
        app = QtWidgets.QApplication() 
        window = UserInterface() # (5)
        window.show()
        app.exec()
    ```

    1. With this line of code, we call the `__init__` method of the parent class `QMainWindow`. In the **without class** case, we do this implicitly when we create the `QMainWindow` object: 
    ```python linenums="6"
    window = QtWidgets.QMainWindow()
    ```
    2. In this case, we use the `self` reference to access the `QMainWindow` object. The equivalent line in the **without class** case is:
    ```python linenums="10"
    window.setCentralWidget(central_widget)
    ```
    3. We give the `Qlabel` to the `self` reference so that we can access it in slot functions, which we will add later. The equivalent lines in the **without class** case are:
    ```python linenums="17-18"
    label = QtWidgets.QLabel()
    label.setText("Hello, User! Please click the button.")
    ```
    4. We only execute the code if the script is run as the main program, not as an imported module. This is a common Python idiom :wink:.

    5. Equivalent lines in the **without class** case are:
    ```python linenums="5"
    app = QtWidgets.QApplication()
    window = QtWidgets.QMainWindow()
    ```
    
In the code above the changes made to `simple_gui.py` are highlighted. Press the :material-plus-circle: buttons for more information about specific lines of code.


<hr>

## Connecting the slot function to a widget

Now we can connect a slot function to the signal of a widget. Some relevant signals of `QWidgets` are mentioned in the [API reference](../QtWidgets). We can for example connect the `CurrentTextChanged` signal of a [`QComboBox`](../../QtWidgets/QComboBox) to a slot function as follows:

```python
combobox = QtWidgets.QComboBox()
combobox.currentTextChanged.connect(do_something)
```

In the code above is assumed the the `do_something` slot function is defined in the same scope as the `combobox` object. In the same way, we can connect the `clicked` signal of a [`QPushButton`](../../QtWidgets/QPushButton) to the `change_label_text` slot function in `simple_gui.py`:

```python title="simple_gui.py" linenums="1" hl_lines="27-32" 

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
```


## Final Result

That's it ! You have succesfully created your first interactive GUI application using PySide6 :material-party-popper: :material-party-popper:. The final result of running `simple_gui.py` is shown below:

=== "Before click"

    <img src="../images/button_and_label.png" alt="Label and button" width="300">

=== "After click"

    <img src="../images/button_clicked.png" alt="Label and button" width="300">


<br>