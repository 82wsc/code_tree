import sys

n, t = map(int,sys.stdin.readline().split())

l = list(map(int,sys.stdin.readline().split()))

ans , cnt = 0,0
for i in range(n):
    if i>=1 and (l[i]>t and l[i-1]>t):
        cnt += 1
    else:
        cnt = 1

    ans = max(ans,cnt)

print(ans)