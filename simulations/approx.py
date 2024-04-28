import os
import numpy as np

PI = np.pi
DX = 0.00001


def f(x):
    return (95000) / (x**2 + 10 * x + 16)


def approximate_population(a, b, dx):
    total_area = 0
    x = a
    while x < b:
        rectangle_area = f(x) * 2 * PI * x * dx
        total_area += rectangle_area
        x += dx
    return total_area


def main():
    a, b = 0,1
    print(f"Test 1: {approximate_population(a, b, DX)}")

    a, b = 4, 6
    print(f"Test 2: {approximate_population(a, b, DX)}")

    a, b = 9,10
    print(f"Test 3: {approximate_population(a, b, DX)}")

    a, b = 0,5
    print(f"Q (a) 2: {approximate_population(a, b, DX)}")

    a, b = 5,10
    print(f"Q (b) 2: {approximate_population(a, b, DX)}")


if __name__ == "__main__":
    main()

# def save_tex_table(

if __name__ == "__main__":
    # Calc density for extremes
    ex_1 = 0
    ex_2 = 1
    ex_3 = 10
    print(
f"""
First at f({ex_1}) = {f(ex_1)},
Second at f({ex_2}) = {f(ex_2)},
Third at f({ex_3}) = {f(ex_3)}.
""")
    a = 0  
    b = 5
    dx = 0.00001  
    result_1 = approximate_population(a, b, dx)
    print("Problem (a) 0 - 5km radie:", result_1)

    a = 5
    b = 10
    result_2 = approximate_population(a, b, dx)
    print("Problem (b) 5 - 10km radie:", result_2)

    a = 0
    b = 10
    result_3 = approximate_population(a, b, dx)
    print("Directly from 0 - 10km", result_3)

    print("Diffrence 10 km - 5km radie: ", result_3 - result_1)

