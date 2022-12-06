from scipy.constants import *
from math import log, sqrt


ni = 10 ** 10
epsilon_s = 12 / 100 * epsilon_0
C_ox = 50 * 10 ** -8  # C_ox / A = 50 * 10 ** -12 / 10 ** -4 = 50 * 10 ** -8
initial = 1
initial_factor = 1
unit = 10 ** 17
smaller_flag = True
larger_flag = False
phi_B = lambda x: 0.026 * log(x / ni)


def equation(x):
    return phi_B(x) + sqrt(e * epsilon_s * x * phi_B(x)) / C_ox - .75


value = equation(initial * unit)
while -0.00001 >= value or value >= 0.00001:
    if value < 0:
        if larger_flag:
            initial_factor *= -.5
            smaller_flag = True
            larger_flag = False
    elif value > 0:
        if smaller_flag:
            initial_factor *= -.5
            smaller_flag = False
            larger_flag = True
    else:
        break
    print(f"current value: {value}")
    print(f'current Na: {initial}e17')
    initial += initial_factor
    value = equation(initial * unit)

print(initial)
