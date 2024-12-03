import sys

n = int(sys.stdin.readline())

def n_sum(x):
    s=x*(x+1)//2
    s= s//10
    return s

print(n_sum(n))