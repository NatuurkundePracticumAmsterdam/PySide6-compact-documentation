class Foo:
    """
    <hr>
    Foo is an example class, which is used to demonstrate the documentation of
    a class in the QtWidgets module.

    Args:
        x (int): Some integer argument called x.

    <hr>

    <h3>Methods</h3>
    <ul>
        <li><a href="#code.format.Foo.bar"><code>bar</code></a></li>
        <li><a href="#code.format.Foo.baz"><code>baz</code></a></li>
    </ul>

    <br>

    **Examples**
    <hr>
    ``` py
    foo = Foo(42)
    foo.bar(10, 3.14)
    foo.baz()
    ```
    This is the description of the example above. The example does absolutely nothing.

    <br>

    ``` py
    foo = Foo(5)
    foo.baz()
    ```
    This is the description of the example above. The example also does absolutely nothing.
    <hr>

    <br>
    """

    def __init__(self, x: int): ...

    def bar(self, y: int, z: float):
        """
        bar is a method that does absolutely nothing.

        Args:
            y (int): Some integer argument called y.
            z (float): Some float argument called z.

        <br>
        """

    def baz(self):
        """
        baz is a method that does absolutely nothing.

        <br>
        <br>
        """
