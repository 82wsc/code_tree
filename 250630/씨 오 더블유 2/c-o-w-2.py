import sys

n = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())

cnt = 0
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            if s[i]=='C' and s[j]=='O' and s[k]=='W':
                cnt+=1
print(cnt)
