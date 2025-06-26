import sys

n = int(sys.stdin.readline())

h = list(map(int,sys.stdin.readline().split()))

cnt = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if h[i]<=h[j]<=h[k]:
                cnt+=1

print(cnt)