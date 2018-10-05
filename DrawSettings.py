import math


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
                             'tan(x)': math.tan,
                             'e^x': math.exp}

    def set_color(self, color):
        self._color = color

    def set_range(self, end, start=0):
        self._range = range(start, end+1)

    def get_options(self):
        return self._options

    def get_color(self):
        return self._color

    def get_range(self):
        return self._range


def parabola(x):
    return x * x


def calculate(x, func, draw_set: DrawSettings):
    if func == parabola:
        draw_set.set_range(start=-150, end=150)
        y = func(x) / 120
    else:
        draw_set.set_range(start=-150, end=150)
        y = func(x / 20) * 20
    return y
