"""
Class inheritance: base class, subclasses, super(), and polymorphism.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def area(self) -> float:
        pass

    def describe(self) -> str:
        return f"{self.name} with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


if __name__ == "__main__":
    shapes: list[Shape] = [Rectangle(3, 4), Circle(2)]
    for s in shapes:
        print(s.describe())
