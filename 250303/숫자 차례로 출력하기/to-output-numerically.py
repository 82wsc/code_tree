import sys

n = int(sys.stdin.readline())

def number_a(x):
    if x==0:
        return

    number_a(x-1)
    print(x, end=' ')

def number_d(x):
    if x==0:
        return

    print(x, end=' ')
    number_d(x-1)
    
number_a(n)
print()
number_d(n)