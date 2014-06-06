import curses


class ViewController(object):

    def __init__(self):
        self.views = []

    def initialize(self, screen):
        self.screen = self.initialize_screen(screen)
        self.present(self.screen)

    def present(self, screen=None):
        if screen:
            self.screen = screen
        self.screen.erase()
        self.active_view.screen = self.screen
        self.active_view.display(self.screen)

    def supervise(self):
        curses.wrapper(self.initialize)

    def push_view(self, view):
        view.controller = self
        self.views.append(view)

    def pop_view(self, *args, **kwargs):
        del self.views[-1]

    @property
    def active_view(self):
        return self.views[len(self.views) - 1]

    def initialize_screen(self, screen):
        curses.noecho()
        curses.curs_set(0)
        curses.cbreak()
        screen.keypad(1)
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)
        curses.init_pair(2, curses.COLOR_RED, -1)
        curses.init_pair(3, curses.COLOR_CYAN, -1)
        curses.init_pair(4, curses.COLOR_YELLOW, -1)
        curses.init_pair(5, curses.COLOR_WHITE, -1)

        return screen


class View(object):
    screen = None

    def draw_str(self, x, y, message, *args, **kwargs):
        self.screen.addstr(x, y, message)

    def refresh(self):
        self.screen.refresh()
