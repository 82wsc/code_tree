import sys

n, m, k = map(int,sys.stdin.readline().split())

l = [0 for _ in range(n)]


ans = -1
for _ in range(m):
    idx = int(sys.stdin.readline())
    l[idx-1] += 1

    if max(l)>=k:
        ans = l.index(max(l))+1
        break
        
print(ans)