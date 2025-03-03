import sys

n = int(sys.stdin.readline())

def number(x):
    if x==0:
        return

    print(x,end=' ')
    number(x-1)
    print(x,end=' ')

number(n)