import sys

n = int(sys.stdin.readline())

l = list(map(int,sys.stdin.readline().split()))
m=[]
for i in range(n-1,0,-1):
    key=l[i]
    for j in range(i):
        m.append(key-l[j])
print(min(m))
