jinx
====

Simple command line UI's.

Planned Usage
-------------

```python
import jinx

class MyView(jinx.View):

    def __init__(self, x, y, text):
        self.left = x
        self.top = y
        self.text = text
        super(MyView, self).__init__()

    def draw(self):
        self.draw_text(self.left, self.top, self.text)

# Create a controller
controller = jinx.ViewController()

# Create our custom view
my_view = MyView(10, 10, "Hello World!")

controller.push_view(my_view)
controller.present()
```

This will render the text "Hello World!" starting at row 10,
column 10 on a black screen. But, this is a simple example
which takes poor advantage of `jinx`'s layout engine.

```python
import jinx

class TextView(jinx.View):

    def __init__(self, x, y, text):
        self.left = x
        self.top = y
        self.text = text
        super(TextView, self).__init__()

    def draw(self):
        self.draw_text(self.left, self.top, self.text)

class GridView(jinx.View):
    """ Displays data in a grid. """
    pass

# Create a controller
controller = jinx.ViewController()

# Create a top-level view to house subviews
top_view = jinx.View()

# Create subviews
header = jinx.TextView(0, 0, "AWESOME APPLICATION")
subheader = jinx.TextView(2, 0, "By Doug Black")
grid = GridView(10, 0, column_headers, rows)

# Add subviews
top_view.add_subviews(header, grid)

# Push view and present controller
controller.push_view(top_view)
controller.present()
```

In this example, a generic `View` is created to house our `TextView` and
`GridView` subviews. When the generic `View` is drawn, it draws each of
its subviews in turn. This component-based architecture makes designing
interactive curses-style command line UI's easy.
