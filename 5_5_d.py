from scipy.constants import *
from math import log, sqrt


ni = 10 ** 10
epsilon_s = 12 / 100 * epsilon_0
C_ox = 4 * 10 ** -7
initial = 1
initial_factor = 1
smaller_flag = True
larger_flag = False
Na = 3.03466796875 * 10 ** 16


def equation(x):
    return x + sqrt(2 * e * epsilon_s * Na * x) / C_ox - .5


value = equation(initial)
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
    print(f'current phi_s: {initial} V')
    initial += initial_factor
    value = equation(initial)
print(f"current value: {value}")
print(f'current phi_s: {initial} V')
print(f'\nSolution: {initial} V')
