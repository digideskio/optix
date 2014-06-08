import curses
from time import sleep


class ViewController(object):
    """ A ViewController is essentially the entry point
    to the UI. It is responsible for initializing the screen,
    moving between main views, and waiting in the main
    event loop. """

    def __init__(self, views=None):
        """ Create a new ViewController.

        :param list View views: a view stack to initialize with. """
        self.views = views or []
        self.initialized = False

    def _present(self, screen=None):
        if screen:
            screen = self.initialize_screen(screen)
        self.screen = screen or self.screen
        self.screen.erase()
        self.active_view.screen = self.screen
        self.active_view.draw()
        self.active_view.refresh()

        # Begin the main event loop
        self.event_loop()

    def present(self):
        """ Take control of the terminal, initialize the
        curses screen, and render views. """

        if not self.initialized:
            curses.wrapper(self._present)
            self.initalized = True
        else:
            self._present()

    def event_loop(self):
        """ The main event loop. When a keypress is received,
        the key is sent to the active view. It is up to the active
        view to forward this signal to any subviews that require
        notification of this event. """

        while True:
            key = self.screen.getch()
            self.active_view.key_pressed(key)
            self.refresh()

    def push_view(self, view):
        """ Push a view to the top of the controller's view stack.
        After pushing, calling present() will render the new view.

        :param View view: the view to add to top of view stack """

        view.controller = self
        self.views.append(view)

    def pop_view(self, *args, **kwargs):
        """ Pop a view from the top of the controller's view stack.
        After poping, calling present() will render view on the
        stack underneath the one that was just popped. """

        del self.views[-1]

    @property
    def active_view(self):
        """ Returns view at the top of the stack. This *generally*
        corresponds to the currently displayed view. """

        return self.views[len(self.views) - 1]

    def initialize_screen(self, screen):
        """ Initialize the curses screen. This method defines
        a sensible set of defaults. To customize, override this
        method in a subclass. """

        curses.noecho()
        curses.curs_set(0)
        curses.cbreak()
        screen.keypad(1)
        curses.start_color()
        curses.use_default_colors()

        return screen


class View(object):
    """ Views are objects that know how
    to draw themselves on the screen. """

    screen = None
    subviews = []

    def draw_text(self, x, y, message, *args, **kwargs):
        """ Writes the given message at row x, column y. """

        self.screen.addstr(x, y, message)

    def refresh(self):
        """ Refresh the screen to pick up any changes since the

        last time the screen has been refreshed. """
        self.screen.refresh()

    def add_subview(self, view):
        """ Add a subview to this view. Subviews are views
        that are rendered when this view's draw() method is
        invoked. """

        view.parent = self
        self.subviews.append(view)

    def add_subviews(self, *views):
        """ Same as add_subview, except it accepts multiple
        view objects. """

        for view in views:
            view.parent = self
            view.screen = self.screen
            self.subviews.append(view)

    def draw(self):
        """ Render this view. By default, this method just
        calls draw() on each of its subviews. Override this
        method to customized behavior. """

        for view in self.subviews:
            view.screen = self.screen
            view.draw()

    def key_pressed(self, key):
        """ This is a callback that is invoked by this view's
        controller when a keydown event happens. """

        pass
