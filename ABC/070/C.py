import fractions
from functools import reduce

def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

t = []

N = int(input())
for i in range(N):
    t.append(int(input()))

print(lcm_list(t))
