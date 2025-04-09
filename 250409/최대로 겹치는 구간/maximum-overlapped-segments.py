import sys

n = int(sys.stdin.readline())

l = [0]*201
offset = 100

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())

    for j in range(a,b):
        l[offset+j]+=1

print(max(l))
