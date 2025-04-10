import sys

n = int(sys.stdin.readline())

l=[int(sys.stdin.readline()) for _ in range(n)]

max_c = 0
for i in range(n):
    if i==0 or l[i] != l[i-1]:
        cnt=1
        for j in range(i,n-1):
            if l[j]==l[j+1]:
                cnt+=1
            else:
                break
    
    max_c = max(max_c,cnt)

print(max_c)