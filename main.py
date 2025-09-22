import sys

def main ():

    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    d = b ** 2 - 4 * a * c

    print(f"discriminant", d)

    return 0

if __name__ == "__main__":
    sys.exit(main())
