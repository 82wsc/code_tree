import sys

n,m = map(int,sys.stdin.readline().split())
a,b = [],[]
r = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    b.append(list(map(int,sys.stdin.readline().split())))
    
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            r[i][j]=0
        else:
            r[i][j]=1

for i in range(len(r)):
    print(*r[i],sep=' ')