import sys
import turtle


def pentagon():
    turtle.goto(0, 0)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.done()


def main():
    pentagon()
    return 0


if __name__ == "__main__":
    sys.exit(main())
