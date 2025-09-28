import sys
import numpy as np

def main():

    # Create two 2x2 arrays
    A = np.array([[1, 2],[3, 4]])
    B = np.array([[5, 6],[7, 8]])

    sum_result = A + B
    mul_result = A * B
    mat_result = A @ B  # or np.matmul(A, B
    print(f"Array A: {A}")
    print(f"Array B: {B}")
    print(f"Elementwise Addition: {sum_result}" )
    print(f"Elementwise Multiplication: {mul_result}")
    print(f"Matrix Product : {mat_result}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
