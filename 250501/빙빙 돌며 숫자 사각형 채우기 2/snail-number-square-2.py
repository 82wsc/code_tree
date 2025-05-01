import sys

n,m = map(int,sys.stdin.readline().split())

# 0,0 1,0 2,0 3,0 3,1 3,2 3,3 3,4 3,5 2,5 1,5 0,5 

l = [[0]*m for _ in range(n)]

x,y = 0,0

l[x][y] = 1

dx,dy =[1,0,-1,0],[0,1,0,-1]
dir_num=0

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

for i in range(2,n*m+1):
    nx,ny = x+dx[dir_num], y+dy[dir_num]
    if not in_range(nx,ny) or l[nx][ny]!=0:
        dir_num = (dir_num + 1)%4
    
    x,y = x+dx[dir_num], y+dy[dir_num]
    l[x][y] = i

for i in range(n):
    for j in range(m):
        print(l[i][j], end=" ")
    print()