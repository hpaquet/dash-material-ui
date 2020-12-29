

class Breakpoints:

    @property
    def values(self):
        return {
            "xs": 0,
            "sm": 600,
            "md": 960,
            "lg": 1280,
            "xl": 1920
        }

    @property
    def unit(self):
        return 'px'

    def up(self, value):
        return f"(min-width: {self.values[value]}{self.unit})"

    def down(self, value):
        return f"(max-width: {self.values[value]}{self.unit})"

    def between(self, start, end):
        return f"(min-width: {self.values[start]}{self.unit}) and (max-width: {self.values[end]}{self.unit})"

    def only(self, value):
        return f"(width: {self.values[value]}{self.unit})"
