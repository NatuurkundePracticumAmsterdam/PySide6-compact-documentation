To make a widget interactive, you need to connect it to a function. We can do this by using a signal-slot mechanism. A signal is emitted when a particular event occurs, and a slot is a function that is called in response to the signal. In PySide6, you can connect a signal to a slot using the `connect` method of the signal object. 

<hr>


## Creating a slot function

First, let's create a slot function that will change the text of the label when the button is clicked. We will define a function called `change_label_text` that takes a label widget as an argument and changes its text to "Hello, PySide6!".

```python
@Slot()
def change_label_text(label):
    label.setText("Hello, PySide6!")

```

In the code above, we use the `@Slot()` decorator to indicate that the function is a slot. 

<hr>

## Connecting the slot function to a widget

Now we can connect this slot function to the signal of a widget. Some relevant signals of `QWidgets` are mentioned in the [API reference](../QtWidgets). We can connect the `clicked` signal of a [`QPushButton`](../../QtWidgets/QPushButton)  to the `change_label_text` slot function as follows: 

```python

button.clicked.connect(lambda: change_label_text(label))

```
