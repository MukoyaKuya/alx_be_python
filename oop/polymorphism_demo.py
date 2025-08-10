# polymorphism_demo.py
import math
from typing import Union

Number = Union[int, float]

class Shape:
    """Base class for shapes. Subclasses must override area()."""
    def area(self) -> Number:
        raise NotImplementedError("Subclasses must implement the area() method.")


class Rectangle(Shape):
    """Rectangle shape with length and width."""
    def __init__(self, length: Number, width: Number):
        self.length = length
        self.width = width

    def area(self) -> Number:
        """Return area = length * width"""
        return self.length * self.width


class Circle(Shape):
    """Circle shape with radius."""
    def __init__(self, radius: Number):
        self.radius = radius

    def area(self) -> float:
        """Return area = pi * r^2"""
        return math.pi * (self.radius ** 2)
