import sys

n = int(sys.stdin.readline())

def star(x):
    if x==0:
        return 

    star(x-1)
    print('*'*x)

star(n)