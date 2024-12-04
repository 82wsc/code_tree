import sys

a,b = map(int,sys.stdin.readline().split())

def in_triple(x):
    temp=list(str(x))
    if '3' in temp or '6' in temp or '9' in temp:
        return True

def triple(x):
    if x%3==0:
        return True

cnt = 0 
for i in range(a,b+1):
    if in_triple(i) or triple(i):
        cnt+=1
print(cnt)