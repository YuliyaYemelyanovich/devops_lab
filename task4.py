

def find_sum(numbs):
    sum = 0
    for i in numbs:
        if i > 0:
            sum += i
    return sum


def find_mult(numbs):
    mult = 1
    a = numbs.index(min(numbs))
    b = numbs.index(max(numbs))
    if (a > b):
        a, b = b, a
    for i in numbs[a + 1:b]:
        mult *= i
    return mult


if __name__ == '__main__':
    numbs = [int(i) for i in input().split()]
    print(find_sum(numbs), find_mult(numbs))
