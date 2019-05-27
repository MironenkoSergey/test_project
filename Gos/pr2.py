from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_squre(self):
        return None


class Circle(Shape):
    def __init__(self, name, r):
        super().__init__(name)
        self.radius = r

    def calculate_squre(self):
        return pi * self.radius ** 2


class Foursquare(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def calculate_squre(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, name, a, h):
        super().__init__(name)
        self.side = a
        self.height = h

    def calculate_squre(self):
        return 0.5 * self.side * self.height


if __name__ == '__main__':
    circle = Circle('Круг', 2)
    foursq = Foursquare('Квадрат', 2)
    triangle = Triangle('Треугольник', 5, 2)
    shapes_list = [circle, foursq, triangle]
    for shape in shapes_list:
        print("Площадь " + shape.name + "а: ", shape.calculate_squre())
