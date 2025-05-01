import sys

n,m = map(int,sys.stdin.readline().split())

l = [[0]*m for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x,y = 0,0
dir_num = 0

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

o=65

l[x][y] = chr(o)

for i in range(2,n*m+1):
    nx,ny = x+dxs[dir_num], y+dys[dir_num]

    if not in_range(nx,ny) or l[nx][ny]!=0:
        dir_num = (dir_num + 1) % 4
    
    x,y = x+dxs[dir_num], y+dys[dir_num]

    l[x][y] = chr(o+(i-1)%26)

for i in range(n):
    for j in range(m):
        print(l[i][j], end=' ')
    print()