import sys

o = list(sys.stdin.readline().strip())

nx,ny= 0,0
dx, dy = [1,-1,0,0], [0,0,1,-1]

dir_num = 2

for i in o:
    if i=='R':
        dir_num = (dir_num + 1) % 4

    if i=='L':
        dir_num = (dir_num - 1 + 4) % 4

    if i=='F':
        nx,ny = nx + dx[dir_num], ny + dy[dir_num]

print(nx,ny)