import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

a.sort()

r=[]
for i in range(n):
    r.append(a[i]+a[2*n-(i+1)])

print(max(r))