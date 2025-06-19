import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

def lcm_list(x):
    if len(x)==1:
        return x[0]
    else:
        return lcm(x[0],lcm_list(x[1:]))

print(lcm_list(A))