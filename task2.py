#!/usr/bin/python

a, b, c, d = [int(i) for i in input().split()]
roots = set()
for i in range(-100, 101):
    if(a * i ** 3 + b * i ** 2 + c * i + d == 0):
        roots.add(i)
roots_sorted = list(roots)
roots_sorted.sort()
print(" ".join([str(i) for i in roots_sorted]))
