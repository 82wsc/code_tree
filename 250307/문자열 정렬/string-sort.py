import sys

n = sys.stdin.readline().strip()
s = list(n)

def f(x):
    return sorted(x)

print(*f(s),sep='')