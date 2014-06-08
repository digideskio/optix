from jinx import View

class RowView(View):

    padding = 1
    seperator = '|'
    align = 'center'

    def __init__(self, left, top, cells, sizes=None):
        self.left = left
        self.top = top
        self.sizes = sizes or [len(cell) for cell in cells]
        self.cells = cells

    def pad_cells(self, cells, sizes):
        return [self.align_cell(cell, size) for cell, size in zip(cells, sizes)]

    def draw(self):
        cells = self.pad_cells(self.cells, self.sizes)
        pad = self.padding * ' '
        gap = pad + self.seperator + pad
        row = gap.join(cells)
        self.draw_text(self.left, self.top, row)

    def align_cell(self, cell, size):
        alignments = {
            'center': cell.center,
            'left': cell.ljust,
            'right': cell.rjust,
        }
        return alignments.get(self.align, cell.center)(size)

class GridView(View):

    padding = 1
    seperator = '|'
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
            new_row.seperator = self.seperator
            new_row.align = self.align
            new_row.screen = self.screen
            new_row.draw()

    def calculate_sizes(self, rows):
        return [len(max(elements)) for elements in zip(*rows[::-1])]


class BorderedView(View):

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
