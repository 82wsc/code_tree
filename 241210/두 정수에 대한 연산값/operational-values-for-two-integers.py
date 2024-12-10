import sys

def math(x,y):
    if x>y:
        x+=25
        y*=2
    else:
        y+=25
        x*=2
    
    print(x,y)

a,b = map(int,sys.stdin.readline().split())

math(a,b)