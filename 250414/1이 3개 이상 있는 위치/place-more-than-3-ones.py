import sys

n = int(sys.stdin.readline())
dxs, dys = [0,1,0,-1],[1,0,-1,0]

l= list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def find_cnt(x,y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and l[nx][ny] == 1:
            cnt += 1
    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        if find_cnt(i,j) >=3:
            ans += 1

print(ans)