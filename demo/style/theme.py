from .breakpoints import Breakpoints
from .shape import Shape
from .palette import Palette


class Theme:

    def __init__(self):
        self.shape = Shape()
        self.breakpoints = Breakpoints()
        self.palette = Palette()

    @property
    def h1(self):
        return "h1"

    @property
    def h2(self):
        return "h2"

    @property
    def h3(self):
        return "h3"

    @property
    def h4(self):
        return "h4"

    @property
    def h5(self):
        return "h5"

    @property
    def h6(self):
        return "h6"

    @property
    def subtitle(self):
        return "h2"

    @property
    def body(self):
        return "span"

    @property
    def default_space(self):
        return 8

    def spacing(self, *args, unit='px'):
        space = []
        for value in args:
            space += [f"{self.default_space * value}{unit}"]
        return f" ".join(space)


theme = Theme()
