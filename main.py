from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

import numpy as np


def main():
    n = 14
    rect = Rectangle(n, n, 'Синий')
    circle = Circle(n, 'Зеленый')
    square = Square(n, 'Красный')

    print(rect)
    print(circle)
    print(square)

    data = [17, 43, 90, -8, 6, 29, 12, 55, 0, 1]
    arr = np.array(data)
    mean_val = np.mean(arr)
    print(mean_val)

if __name__ == "__main__":
    main()
