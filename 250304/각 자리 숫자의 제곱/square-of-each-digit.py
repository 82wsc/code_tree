import sys

n = int(sys.stdin.readline())

def f(x):
    if x<10:
        return x**2
    
    return f(x//10) + (x%10)**2

print(f(n))