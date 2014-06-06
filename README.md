jinx
====

Simple command line UI's.

Planned Usage
-------------

```python
import jinx

class MyView(jinx.View):

    def __init__(self, x, y, message):
        self.message = message
        self.x = x
        self.y = y

    def show(self):
        self.add_str(0, 0, message)

view = MyView("Hello")
controller = jinx.Controller()
controller.push_view(0, 0, view)
controller.supervise()
```

Will render `MyView` starting in the top left corner.

You can also take advantage of some built in `View` objects:

```python
import jinx

text_view = jinx.TextView("This is some text.")
text_view.width = 50
text_view.height = 50
text_view.border = True
```

To render some text to the screen with some visual configuration.
