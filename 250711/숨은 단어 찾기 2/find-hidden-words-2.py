import sys

n,m = map(int,sys.stdin.readline().split())

l = [
    list(sys.stdin.readline().strip())
    for _ in range(n)
]

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

cnt = 0

for i in range(n):
    for j in range(m):
        if l[i][j] == 'L':
            for k in range(8):
                x1 = i + dx[k]
                y1 = j + dy[k]
                x2 = x1 + dx[k]
                y2 = y1 + dy[k]
                if 0 <= x1 < n and 0 <= y1 < m and 0 <= x2 < n and 0 <= y2 < m and l[x1][y1] == 'E' and l[x2][y2] == 'E':
                    cnt += 1

print(cnt)