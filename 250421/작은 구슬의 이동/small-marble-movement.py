import sys

n, t = map(int,sys.stdin.readline().split())

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

x,y,o = sys.stdin.readline().split()
x, y = int(x)-1, int(y)-1

d = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3 
}

dir_idx = d[o]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

def keep_moving(x,y,dir_idx):
    nx, ny = x + dxs[dir_idx], y + dys[dir_idx]
    if not in_range(nx,ny):
        dir_idx = 3- dir_idx
    
    x,y = x+dxs[dir_idx], y+dys[dir_idx]
    return x, y, dir_idx

for _ in range(1,t):
    x, y, dir_idx = keep_moving(x, y, dir_idx)

print(x+1,y+1)