import sys

n = int(sys.stdin.readline())


for _ in range(n):
    s=0
    a,b = map(int,sys.stdin.readline().split())
    for i in range(a,b+1):
        if i%2==0:
            s+=i
    print(s)