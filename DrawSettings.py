import math


def parabola(x):
    return x * x


class DrawSettings(object):

    def __init__(self, range_size, color, options=None):
        self._color = color
        self._range = range(-range_size, range_size + 1)

        if options:
            self._options = options
        else:
            self._options = {'X^2': parabola,
                             'sin(x)': math.sin,
                             'cos(x)': math.cos,
                             'tan(x)': math.tan}

    def set_color(self, color):
        self._color = color

    def set_range(self, range_size):
        self._range = range_size

    def get_options(self):
        return self._options

    def get_color(self):
        return self._color

    def get_range(self):
        return self._range
