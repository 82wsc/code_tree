import sys

n,m = map(int,sys.stdin.readline().split())

l = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())    
    l[a-1][b-1] = a*b

for i in range(n):
    print(*l[i],sep=' ')
