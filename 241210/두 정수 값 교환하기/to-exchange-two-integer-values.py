import sys

n,m = map(int,sys.stdin.readline().split())

def swap(a,b):
    a,b = b,a
    print(a, b) 

swap(n,m)