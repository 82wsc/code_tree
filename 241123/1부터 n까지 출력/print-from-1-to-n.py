import sys

n = int(sys.stdin.readline())
l=[i for i in range(1,n+1)]

print(*l,sep=' ')