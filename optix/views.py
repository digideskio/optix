from optix import View


class RowView(View):
    """ A RowView is used to organize a series of items on
    one line

    So:
        RowView(x, y, ['one', 'two', 'three', 'four'])
    would draw:
        one | two | three | four
    """

    padding = 1
    separator = '|'
    align = 'center'

    def __init__(self, left, top, cells, sizes=None):
        self.left = left
        self.top = top
        self.sizes = sizes or [len(cell) for cell in cells]
        self.cells = cells

    def pad_cells(self, cells, sizes):
        """ Pad cells based on size and alignment properties """
        return [self.align_cell(cell, size) for cell, size in zip(cells, sizes)]

    def draw(self):
        cells = self.pad_cells(self.cells, self.sizes)
        pad = self.padding * ' '
        gap = pad + self.separator + pad
        row = gap.join(cells)
        self.draw_text(self.left, self.top, row)

    def align_cell(self, cell, size):
        """ Given a size, align the cell based on align property """
        alignments = {
            'center': cell.center,
            'left': cell.ljust,
            'right': cell.rjust,
        }
        return alignments.get(self.align, cell.center)(size)


class GridView(View):
    """ A GridView is used to draw and format a series of RowViews

    So:
        grid = [['one', 'two', 'three'], [1, 2, 3]]
        GridView(0, 0, grid)
    would draw:
        one | two | three
         1  |  2  |   3
    """

    padding = 1
    separator = '|'
    align = 'center'

    def __init__(self, left, top, rows, sizes=None):
        self.left = left
        self.top = top
        self.rows = rows
        self.sizes = sizes or self.calculate_sizes(self.rows)

    def draw(self):
        for i, row in enumerate(self.rows):
            new_row = RowView(self.top + i, self.left, row, self.sizes)
            new_row.padding = self.padding
            new_row.separator = self.separator
            new_row.align = self.align
            new_row.screen = self.screen
            new_row.draw()

    def calculate_sizes(self, rows):
        """ Calculate the size for each column based on max cell width """
        return [len(max(elements)) for elements in zip(*rows[::-1])]


class BorderedView(View):
    """ A BorderedView is used to essentially draw
    bordered boxes.

    So:
        v = BorderedView(0, 0)
        v.width = 3
        v.height = 3
    would draw:
        +-+
        | |
        +-+
    """

    width = 20
    height = 10

    def __init__(self, left, top):
        self.left = left
        self.top = top

    def draw(self):
        horizontal_middle = (self.width - 2)
        top = bottom = '+' + ('-' * horizontal_middle) + '+'
        middle = '|' + (' ' * horizontal_middle) + '|'
        self.draw_text(self.top, self.left, top)
        for y in xrange(self.height - 1):
            self.draw_text(self.top + y + 1, self.left, middle)
        self.draw_text(self.top + self.height - 1, self.left, bottom)


class MenuChoice(RowView):
    """ A MenuChoice contains a prompt and a series of options.

    Toggling a MenuChoice causes it to switch the currently shown
    option. Options can have colors associated with them.
    """

    def __init__(self, prompt, options):
        self.prompt = prompt
        self.options = options
        self.selected = 0
        self.keys = options.keys()

        key = self.keys[0]

    def toggle(self):
        if self.selected == len(self.keys):
            self.selected = 0
        else:
            self.selected += 1

    @property
    def cells(self):
        key = self.keys[self.selected]
        return [self.prompt, key, self.options[key]]

    @property
    def sizes(self):
        return [len(cell) for cell in self.cells]


class MenuView(View):
    """ A MenuView is used to draw a menu.

    It is different from a GridView in that it provides a few
    more convenience features for creating an interactive menu.

    So:
        gender = MenuChoice('Gender', {'Male': optix.Red, 'Female': optix.Green})
        sports = MenuChoice('Like Sports?', {'Yes': optix.Red, 'No': optix.Green})
        MenuView(0, 0, [gender, sports])
    would draw:
        +---------------------+
        | Gender       | Male |
        | Like Sports? | No   |
        +---------------------+
    """

    def __init__(self, left, top, menu):
        self.left = left
        self.top = top
        self.menu = menu

    def draw(self):
        pass
