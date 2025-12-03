# Product Classes
class Shape:
    def draw(self):
        raise NotImplementedError("Subclasses must override draw()")


class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"


class Square(Shape):
    def draw(self):
        return "Drawing a Square"


class Rectangle(Shape):
    def draw(self):
        return "Drawing a Rectangle"


# 1. Factory using if-elif-else
class ShapeFactoryIfElse:
    @staticmethod
    def get_shape(shape_type):
        shape_type = shape_type.lower()

        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "rectangle":
            return Rectangle()
        else:
            raise ValueError("Unknown shape type!")


# 2. Factory using Dictionary Mapping
class ShapeFactoryDict:
    shapes = {"circle": Circle, "square": Square, "rectangle": Rectangle}

    @staticmethod
    def get_shape(shape_type):
        shape_type = shape_type.lower()

        if shape_type not in ShapeFactoryDict.shapes:
            raise ValueError(f"Unknown shape type: {shape_type}")

        return ShapeFactoryDict.shapes[shape_type]()  # instantiate class


if __name__ == "__main__":

    print("---- Using IF-ELIF-ELSE Factory ----")
    shape1 = ShapeFactoryIfElse.get_shape("circle")
    print(shape1.draw())

    shape2 = ShapeFactoryIfElse.get_shape("square")
    print(shape2.draw())

    shape3 = ShapeFactoryIfElse.get_shape("rectangle")
    print(shape3.draw())

    print("\n---- Using DICTIONARY Factory ----")
    shape4 = ShapeFactoryDict.get_shape("circle")
    print(shape4.draw())

    shape5 = ShapeFactoryDict.get_shape("square")
    print(shape5.draw())

    shape6 = ShapeFactoryDict.get_shape("rectangle")
    print(shape6.draw())
