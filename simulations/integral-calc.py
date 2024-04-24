import sympy as sp

x = sp.symbols('x')
a_v = sp.symbols('a')
b_v = sp.symbols('b')

function = (95000 * 2 * x * sp.pi) / (x**2 + 10 * x + 16)

indefinite_integral = sp.integrate(function, x)
print("Indefinite Integral:", indefinite_integral)

# a = a_v
# b = b_v 
# definite_integral = sp.integrate(function, (x, a, b))
# print("Definite Integral from", a, "to", b, ":", definite_integral)

a = 0  
b = 5 
definite_integral = sp.integrate(function, (x, a, b))
print("Definite Integral from", a, "to", b, ":", definite_integral)

# To get a floating-point number if necessary
numeric_result = definite_integral.evalf()
print("Numerical result:", numeric_result)

a = 5  
b = 10 
definite_integral = sp.integrate(function, (x, a, b))
print("Definite Integral from", a, "to", b, ":", definite_integral)

# To get a floating-point number if necessary
numeric_result = definite_integral.evalf()
print("Numerical result:", numeric_result)
