import sys

a,b,c = map(int,sys.stdin.readline().split())

def find_min(a,b,c):
    mini = 0
    if a<b:
        if a<c:
            mini=a
        else:
            mini=c
    elif a<c:
        if a<b:
            mini=a
        else:
            mini=b
    elif b<c:
        if b<a:
            mini=b
        else:
            mini=a
    return mini
print(find_min(a,b,c))
