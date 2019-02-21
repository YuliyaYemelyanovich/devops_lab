#!/usr/bin/python

n = int(input())
numbs = [int(i) for i in input().split()]
sum = 0
mult = 1
for i in numbs:
    if i > 0:
        sum += i
a = numbs.index(min(numbs))
b = numbs.index(max(numbs))
if (a > b):
    a, b = b, a
for i in numbs[a + 1:b]:
    mult *= i
print(sum, mult, end=' ')
