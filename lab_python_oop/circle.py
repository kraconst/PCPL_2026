from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
from math import pi

class Circle(Figure):

    FIGURE_TYPE = 'круг'

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, r, c):
        self.radius = r
        self.color = Color()
        self.color._color = c

    def area(self):
        return round(pi * (self.radius ** 2), 2)

    def __repr__(self):
        return '{} {} радиусом {} и площадью {}'.format(
            self.color._color,
            Circle.get_figure_type(),
            self.radius,
            self.area()
        )
