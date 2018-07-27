import fractions
from functools import reduce

def lcm(x, y):
    return (x * y) // fractions._gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

print(lcm_list([2,3,4]))
