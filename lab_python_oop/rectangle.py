from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):

    FIGURE_TYPE = 'прямоугольник'

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, a, b, c):
        self.width = a
        self.height = b
        self.color = Color()
        self.color._color = c

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} шириной {}, высотой {} и площадью {}'.format(
            self.color._color,
            Rectangle.get_figure_type(),
            self.width,
            self.height,
            self.area()
        )
