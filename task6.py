#!/usr/bin/bash

n, x = [int(i) for i in input().split()]
scores = []
for i in range(x):
    scores += [[float(i) for i in input().split()]]
scores = zip(*scores)
for i in scores:
    print(sum(i) / x)
