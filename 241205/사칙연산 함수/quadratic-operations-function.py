import sys

a,o,c = map(str,sys.stdin.readline().split())

a,c = int(a), int(c)

def math(x,m,y):
    if m=='+':
        return x+y
    elif m=='-':
        return x-y
    elif m=='*':
        return x*y
    elif m=='/':
        return x//y
    else:
        return False

if math(a,o,c):
    print(a,o,c,'=',math(a,o,c))
else:
    print(math(a,o,c))