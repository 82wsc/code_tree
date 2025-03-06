import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))

def gcd(a,b):
    while b!=0:
        a, b = b, a%b  
    return a


print(gcd(6,2))