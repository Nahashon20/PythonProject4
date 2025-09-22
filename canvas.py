import sys
import turtle


def draw_canvas():
    turtle .goto( 0 , 0)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    word = turtle.textinput("Input", "Enter your  name")
    turtle.write(word, font=("Arial", 24, "italic"))
    turtle.done()

def main():
    draw_canvas()

    return 0

if __name__ == "__main__":
    sys.exit(main())
