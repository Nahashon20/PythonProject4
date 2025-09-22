import sys
import math

def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    x = -b + math.sqrt(b ** 2 - 4 * a * c) // 2 * a
    y = -b + math.sqrt(b ** 2 -4 * a * c) // 2 * a

    print(f"{x ,y}")





    return 0

if __name__ == "__main__":
    sys.exit(main())
