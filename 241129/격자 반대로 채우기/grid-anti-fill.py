import sys

n = int(sys.stdin.readline())
l= [[0 for _ in range(n)] for _ in range(n)]
cnt = n**2

if n%2==1:
    for i in range(n):
        if i%2==1:
            for j in range(n-1,-1,-1):
                l[j][i] = cnt
                cnt -= 1
        else:    
            for j in range(n):
                l[j][i] = cnt
                cnt -= 1        
else:
    for i in range(n):
        if i%2==1:
            for j in range(n):
                l[j][i] = cnt
                cnt -= 1
        else:    
            for j in range(n-1,-1,-1):
                l[j][i] = cnt
                cnt -= 1

for i in range(n):
    print(*l[i],sep=" ")        