import sys

n = int(sys.stdin.readline())
cnt = 0
def f(x):
    global cnt
    if x==1:
        return cnt
    
    if x%2==0:
        cnt+=1
        return f(x//2)
    else:
        cnt+=1
        return f(x//3)

print(f(n))