import math

class Shape:
    """Базовый класс для всех фигур."""
    def area(self):
        raise NotImplementedError("Каждая фигура должна реализовать метод area().")

class Circle(Shape):
    """Класс для представления круга."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Вычислить площадь круга."""
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    """Класс для представления треугольника."""

    def __init__(self, a: float, b: float, c: float):
        if not self.is_valid_triangle(a, b, c):
            raise ValueError("Стороны не образуют треугольник.")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Вычислить площадь треугольника по формуле Герона."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        """Вычислить периметр треугольника."""
        return self.a + self.b + self.c

    def is_right_angle(self) -> bool:
        """Проверить, является ли треугольник прямоугольным."""
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

    @staticmethod
    def is_valid_triangle(a: float, b: float, c: float) -> bool:
        """Проверить, может ли существовать треугольник с заданными сторонами."""
        return a + b > c and a + c > b and b + c > a

def calculate_area(shape: Shape) -> float:
    """Вычислить площадь фигуры без знания типа фигуры на этапе компиляции."""
    return shape.area()
