import sys

n  = int(sys.stdin.readline())

def hello(x):
    if x==0:
        return
    
    print("HelloWorld")
    hello(x-1)

hello(n)
