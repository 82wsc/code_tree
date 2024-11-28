import sys

l = []
s=0
for i in range(4):
    l.append(list(map(int,sys.stdin.readline().split())))

for i in range(len(l)+1):
    for j in range(i):
        s+=l[i-1][j]

print(s)