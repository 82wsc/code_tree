import sys

n, k = map(int,sys.stdin.readline().split())

l = [0]*n

for i in range(k):
    a,b = map(int,sys.stdin.readline().split())
    for j in range(a-1,b):
        l[j]+=1

print(max(l))
