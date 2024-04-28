from typing import Tuple
import sympy as sp

x = sp.symbols('x')
a_v = sp.symbols('a')
b_v = sp.symbols('b')


def calc_indefinate_integral(function, x):
    return sp.integrate(function, x)

def calc_definate_integral(function, 
                      values: Tuple[float,float, float]):
    """Takes in a function e.g. x^2
        values: x, a, b
        returns integral value as float
    """
    res = sp.integrate(function, (values))
    return res.evalf()

if __name__ == "__main__":
    function = (95000 * 2 * x * sp.pi) / (x**2 + 10 * x + 16)

    print("Indefinite Integral:", calc_indefinate_integral(function, x))

    # a = a_v
    # b = b_v 
    # definite_integral = sp.integrate(function, (x, a, b))
    # print("Definite Integral from", a, "to", b, ":", definite_integral)

    a = 0  
    b = 1 
    definite_integral = sp.integrate(function, (x, a, b))
    print("Definite Integral from", a, "to", b, ":", definite_integral)

    # To get a floating-point number if necessary
    numeric_result = definite_integral.evalf()
    print("Numerical result:", numeric_result)

    a = 4  
    b = 6 
    definite_integral = sp.integrate(function, (x, a, b))
    print("Definite Integral from", a, "to", b, ":", definite_integral.evalf())

    a = 9  
    b = 10 
    definite_integral = sp.integrate(function, (x, a, b))
    print("Definite Integral from", a, "to", b, ":", definite_integral.evalf())

    # To get a floating-point number if necessary
    numeric_result = definite_integral.evalf()
    print("Numerical result:", numeric_result)
