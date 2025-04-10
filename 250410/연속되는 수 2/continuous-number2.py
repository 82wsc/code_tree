import sys

n = int(sys.stdin.readline())

l=[int(sys.stdin.readline()) for _ in range(n)]

cnt =0
for i in range(n):
    if i==0 or l[i] != l[i-1]:
        cnt+=1

print(cnt)