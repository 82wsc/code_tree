import sys

n = int(sys.stdin.readline())

a = list(map(int,sys.stdin.readline().split()))

for i in range(len(a)-1,-1,-1):
    if a[i]%2==0:
        print(a[i],end=" ")