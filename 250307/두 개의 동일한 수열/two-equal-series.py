import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))

a.sort()
b.sort()

def same(x,y):
    if x==y:
        print('Yes')
    else:
        print('No')

same(a,b)