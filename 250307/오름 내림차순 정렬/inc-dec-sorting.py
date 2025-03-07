import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

def f(x):
    print(*sorted(x),sep=' ')
    print(*sorted(x,reverse=True),sep=' ') 

f(A)