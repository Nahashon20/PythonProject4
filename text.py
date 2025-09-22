import sys
import turtle



def text():

    word = turtle.textinput("Input", "Enter text:")
    turtle.write(word, font=("Arial", 24, "normal"))
    turtle.done()

def main():
    text()

    return 0

if __name__ == "__main__":
    sys.exit(main())
