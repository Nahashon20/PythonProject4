import sys
import math
import turtle




class Rectangle:
    units = 'cm'

    def __init__(self , width,height,position=(0,0)):
        self.width = width
        self.height = height
        self.position = position
        self.area = self.width*self.height
        self.perimeter = self.width +self.height + self.width +self.height


    def __str__(self):
        return f"I'm a rectangle of size {self.width} {self.height} {self.area} {self.perimeter} {self.units}"

def area(rectangle):
    return rectangle.width * rectangle.height
def perimeter(rectangle):
    return rectangle.width +rectangle.height + rectangle.width +rectangle.height

def bounding_box(rectangle):
    xmin = rectangle.position[0] - rectangle.width
    xmax = rectangle.position[0] + rectangle.width
    ymin = rectangle.position[1] - rectangle.height
    ymax = rectangle.position[1] + rectangle.height
    return xmin, ymin, xmax, ymax

def diagonal(rectangle):
    x = math.sqrt(rectangle.height**2 + rectangle.width**2)
    return  x

class Square:
    def __innit__ (self,width,fill="white", stroke= "black" , position= (0,0)):
            self.width = width
            self.fill = fill
            self.stroke =stroke
            self.position = position

    def area(self):
            return self.width ** 2
    def __str__(self):
            return f"Square: {self.width} * {self.width}"



class Canvas(turtle.TurtleScreen):
    def __init__(self, width: int = 1200, height: int = 750, bg: str = "white"):
        self.width = width
        self.height = height
        self.canvas = turtle.getcanvas()
        super().__init__(self.canvas)
        # fixed: the canvas is a turtle.TurtleScreen subclass so we can set the screensize on self
        self.screensize(width, height, bg)
        self.pen = turtle.RawPen(self.canvas)

    def mystery_method(self):
        self.pen.up()
        self.pen.goto(0, self.height / 2)  # what does this do
        self.pen.down()
        self.pen.goto(0, -self.height / 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.down()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()

def main():
    rectangle = Rectangle(height = 5, width= 5)
    print(rectangle)
    rectangle.height = 100
    rectangle.width = 50
    print(rectangle)
    print(f" Is my height {rectangle.height}")
    print(rectangle)
    print(f"Is the area of the rectangle {area(rectangle)}")
    print(f"Is the perimeter of the rectangle {perimeter(rectangle)}")
    print(f"{bounding_box(rectangle) = }")
    print(f"This is the diagonal of the rectangle {diagonal(rectangle) = }")




    #canvas
    canvas = Canvas()
    canvas.mystery_method()
    return 0



if __name__ == "__main__":
    sys.exit(main())
