import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

l=[]
for i in range(n+1):
    if i%2==1:
        temp = a[:i]
        temp.sort()
        l.append(temp[i//2])

print(*l,sep=' ')
