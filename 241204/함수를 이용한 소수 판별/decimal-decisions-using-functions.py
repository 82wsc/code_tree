import sys

a,b = map(int,sys.stdin.readline().split())

def is_prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def s_num(x,y):
    s=0
    for i in range(x,y+1):
        if is_prime(i):
            s+=i

    return s

print(s_num(a,b))