from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):

    FIGURE_TYPE = 'квадрат'

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return '{} {} стороной {} и площадью {}'.format(
            self.color._color,
            Square.get_figure_type(),
            self.width,
            self.area()
        )
