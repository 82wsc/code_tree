import sys

n,m = map(int,sys.stdin.readline().split())

def gcd(a,b):
    if a<b:
        while a>0:
            temp = b
            b=a
            a=temp%a
        print(b)
    else:
        while b>0:
            temp = a
            a=b
            b=temp%b
        print(a)

gcd(n,m)