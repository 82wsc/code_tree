import sys

n = int(sys.stdin.readline())

def f(x):
    if x==1:
        return 2
    if x==2:
        return 4
    
    return (f(x-2) * f(x-1))%100

print(f(n))