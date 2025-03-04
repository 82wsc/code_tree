import sys

n = int(sys.stdin.readline())

cnt=0
def f(x):
    global cnt
    while x!=1:
        cnt+=1
        if x%2==0:
            return f(x//2)
        else:
            return f(x*3+1)
    
    return cnt

print(f(n))