import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

def f(x):
    if x==0:
        return A[0]
    
    return max(f(x-1),A[x])
    
print(f(n-1))