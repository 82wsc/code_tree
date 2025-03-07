import sys

n = int(sys.stdin.readline())
a=[]
for i in range(n):
    a.append(sys.stdin.readline().strip())

a.sort()

for i in range(n):
    print(a[i])