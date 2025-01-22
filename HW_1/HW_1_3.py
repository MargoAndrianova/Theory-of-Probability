from itertools import combinations
import random

A = [random.randint(1, 20) for i in range(10)]

B = [a + b for a, b in combinations(A, 2)]

print(A)
print(B)
print(len(B))
