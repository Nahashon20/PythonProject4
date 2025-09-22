import sys
import math



class Square:
    units = 'cm'

    def __init__(self , width,height,position=(0,0)):
        self.width = width
        self.height = height
        self.position = position
        self.area = self.width*self.height
        self.perimeter = self.width +self.height + self.width +self.height


    def __str__(self):
        return f"I'm a square of size {self.width} {self.height} {self.area} {self.perimeter} {self.units}"

def area(square):
    return square.width * square.height
def perimeter(square):
    return square.width +square.height + square.width +square.height

def bounding_box(square):
    xmin = square.position[0] - square.width
    xmax = square.position[0] + square.width
    ymin = square.position[1] - square.height
    ymax = square.position[1] + square.height
    return xmin, ymin, xmax, ymax

def diagonal(square):
    x = math.sqrt(square.height**2 + square.width**2)
    return  x



def main():
    square = Square(height = 5, width= 5)
    print(square)
    square.height = 100
    square.width = 100
    print(square)
    print(f" Is my height {square.height}")
    print(square)
    print(f"Is the area of the square {area(square)}")
    print(f"Is the perimeter of the square {perimeter(square)}")
    print(f"{bounding_box(square) = }")
    print(f"This is the diagonal of the square {diagonal(square) = }")
    return 0


if __name__ == "__main__":
    sys.exit(main())
