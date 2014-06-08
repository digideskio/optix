from jinx import View

class RowView(View):

    def __init__(self, left, top, cells, sizes=None, padding=1, seperator='|', align='center'):
        self.left = left
        self.top = top
        self.padding = padding
        self.seperator = seperator
        self.sizes = sizes or [len(cell) for cell in cells]
        self.align = align
        self.cells = self._correct_padding(cells, sizes)

    def _correct_padding(self, cells, sizes):
        return [self.alignment_func(cell)(sizes[i]) for i, cell in enumerate(cells)]

    def draw(self):
        cells = self._correct_padding(self.cells, self.sizes)
        pad = self.padding * ' '
        gap = pad + self.seperator + pad
        row = gap.join(self.cells)
        self.draw_text(self.left, self.top, row)

    def alignment_func(self, cell):
        alignments = {
            'center': cell.center,
            'left': cell.ljust,
            'right': cell.rjust,
        }
        return alignments.get(self.align, cell.center)

class GridView(View):

    def __init__(self, left, top, rows, sizes=None, padding=1, seperator='|', align='center'):
        self.left = left
        self.top = top
        self.rows = rows
        self.sizes = sizes or self.calculate_sizes(self.rows)
        self.padding = padding
        self.seperator = seperator
        self.align = align

    def draw(self):
        for i, row in enumerate(self.rows):
            new_row = RowView(self.top + i, self.left, row, self.sizes, self.padding, self.seperator, self.align)
            new_row.screen = self.screen
            new_row.draw()

    def calculate_sizes(self, rows):
        return [len(max(elements)) for elements in zip(*rows[::-1])]

