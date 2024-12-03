import sys

n,m = map(int,sys.stdin.readline().split())

def pprint(a,b):
    for _ in range(a):
        print('1'*b)

pprint(n,m)