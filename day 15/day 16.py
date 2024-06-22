class Shape:
    pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

class AreaCalculator:
    def calculate_area(self, shapes):
        total_area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):
                total_area += shape.width * shape.height
            elif isinstance(shape, Circle):
                total_area += 3.14 * (shape.radius ** 2)
        return total_area

shapes = [Rectangle(2, 3), Circle(5)]
calculator = AreaCalculator()
print(f"Total Area: {calculator.calculate_area(shapes)}")
