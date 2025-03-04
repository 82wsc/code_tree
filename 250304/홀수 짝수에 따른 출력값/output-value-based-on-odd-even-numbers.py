import sys

n = int(sys.stdin.readline())

def f(x):
    if x==1:
        return 1
    if x==2:
        return 2

    return f(x-2)+x

print(f(n))