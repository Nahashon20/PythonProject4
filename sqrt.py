import sys
import cmath

def main():
    #cmath.sqrt  helps in finding the square root in complex numbers
    #math.sqrt is the normal square root
    x= float(input(f"x:"))
    print(f"square root of the number {cmath.sqrt(x)}")


    return 0

if __name__ ==  "__main__":
    sys.exit(main())
