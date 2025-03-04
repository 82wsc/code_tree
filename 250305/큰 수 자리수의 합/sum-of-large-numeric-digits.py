import sys

a,b,c = map(int,sys.stdin.readline().split())

r = a * b * c
def f(x):
    if x<10:
        return x

    return f(x//10)+ (x%10)

print(f(r))