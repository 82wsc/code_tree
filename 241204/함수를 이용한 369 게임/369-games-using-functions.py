import sys

a,b = map(int,sys.stdin.readline().split())

def in_triple(x):
    temp=list(str(x))
    if '3' in temp or '6' in temp or '9' in temp:
        return True

def triple(x):
    return in_triple(x) or (x%3==0)

cnt = 0 
for i in range(a,b+1):
    if triple(i):
        cnt+=1
print(cnt)