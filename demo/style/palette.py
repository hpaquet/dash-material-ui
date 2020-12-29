

class ColorDict(dict):

    def __init__(self):
        super().__init__()

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Palette(ColorDict):

    def __init__(self):
        super().__init__()

        self.common = ColorDict()

        self._set_colors()

    def _set_colors(self):
        self.common.white = '#fff'
        self.common.black = '#000'


if __name__ == '__main__':
    palette = Palette()
