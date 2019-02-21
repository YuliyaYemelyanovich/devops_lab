#!/usr/bin/python

if __name__ == '__main__':
	a = int(input("Enter A: "))
	b = int(input("Enter B: "))
	c = int(input("Enter C: "))
	d = int(input("Enter D: "))
	roots = set()
	for i in range(-100, 101):
		if(a*i**3 + b*i**2 + c*i +d == 0):
			roots.add(i)
	print(" ".join([str(i) for i in roots]))