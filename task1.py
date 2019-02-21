#!/usr/bin/python

if __name__ == '__main__':
    n = int(input())
    s = input()
    arr = list([int(i) for i in s.split()])
    arr.sort()
    for i in arr[::-1]:
        if i < arr[n-1]:
            print(i)
            break