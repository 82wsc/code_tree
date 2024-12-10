import sys

def math(x,y):
    if x>y:
        x*=2
        y+=10
    else:
        x+=10
        y*=2
    
    print(x,y)

a,b = map(int,sys.stdin.readline().split())

math(a,b)