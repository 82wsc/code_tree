import sys

a,b = map(int,sys.stdin.readline().split())

l = [i for i in range(a,b-1,-2) if i%2==1]
print(*l,sep=' ')