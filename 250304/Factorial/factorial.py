import sys

n = int(sys.stdin.readline())

def f(x):
    if x==1:
        return 1

    return f(x-1) * x

print(f(n))