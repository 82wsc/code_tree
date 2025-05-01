import sys

n = int(sys.stdin.readline())

l = [[0]*n for _ in range(n)]

x,y=n-1, n-1
l[x][y] = n*n

dx,dy = [0,-1,0,1],[-1,0,1,0]
dir_num = 0

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

for i in range(1,n*n):
    nx,ny = x+dx[dir_num], y+dy[dir_num]
    if not in_range(nx,ny) or l[nx][ny]!=0:
        dir_num = (dir_num + 1)%4
    
    x,y = x+dx[dir_num], y+dy[dir_num]

    l[x][y] = (n*n)-i

for i in range(n):
    for j in range(n):
        print(l[i][j], end=" ")
    print()