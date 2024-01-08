from abc import ABC, abstractmethod


# Abstract factory for Shapes
class ShapeFactory(ABC):
    @abstractmethod
    def create_circle(self):
        pass

    @abstractmethod
    def create_rectangle(self):
        pass


# Concrete factory for Shapes
class SimpleShapeFactory(ShapeFactory):
    def create_circle(self):
        return Circle()

    def create_rectangle(self):
        return Rectangle()


# Abstract factory for Colors
class ColorFactory(ABC):
    @abstractmethod
    def create_red(self):
        pass

    @abstractmethod
    def create_blue(self):
        pass


# Concrete factory for Colors
class SimpleColorFactory(ColorFactory):
    def create_red(self):
        return Red()

    def create_blue(self):
        return Blue()


# Abstract product: Shape
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


# Concrete products: Circle and Rectangle
class Circle(Shape):
    def draw(self):
        return "Drawing Circle"


class Rectangle(Shape):
    def draw(self):
        return "Drawing Rectangle"


# abstract product: color
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass


# concrete products: red and blue
class Red(Color):
    def fill(self):
        return "Filling with Red Color"


class Blue(Color):
    def fill(self):
        return "Filling with Blue Color"


shape_factory = SimpleShapeFactory()
circle = shape_factory.create_circle()
rectangle = shape_factory.create_rectangle()

color_factory = SimpleColorFactory()
red = color_factory.create_red()
blue = color_factory.create_blue()

print(circle.draw())
print(rectangle.draw())

print(red.fill())
print(blue.fill())
