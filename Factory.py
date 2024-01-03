class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "triangle":
            return Triangle()
        else:
            raise ValueError(f"Invalid shape type: {shape_type}")


class Circle:
    def __init__(self):
        self._drawn = False

    def draw(self):
        self._drawn = True

    def erase(self):
        self._drawn = False

    def is_drawn(self):
        return self._drawn

class Rectangle:
    def __init__(self):
        self._drawn = False

    def draw(self):
        self._drawn = True

    def erase(self):
        self._drawn = False

    def is_drawn(self):
        return self._drawn

class Triangle:
    def __init__(self):
        self._drawn = False

    def draw(self):
        self._drawn = True

    def erase(self):
        self._drawn = False

    def is_drawn(self):
        return self._drawn


factory = ShapeFactory()

circle = factory.create_shape("circle")
rectangle = factory.create_shape("rectangle")
triangle = factory.create_shape("triangle")

circle.draw()
rectangle.draw()

print(f"Circle is drawn: {circle.is_drawn()}") # return true
print(f"Rectangle is drawn: {rectangle.is_drawn()}") # return true
print(f"Triangle is drawn: {triangle.is_drawn()}") # should return false

rectangle.erase()
print(f"rectangle is drawn: {rectangle.is_drawn()}") # should return false
