import sys
import turtle

def triangle():
        turtle .goto( 0 , 0)
        turtle.forward(200)
        turtle.left(120)
        turtle.forward(200)
        turtle.left(120)
        turtle.forward(200)
        turtle.left(0)

        turtle.done()



def main():
    triangle()
    return  0

if __name__ == "__main__":
    sys.exit(main())
