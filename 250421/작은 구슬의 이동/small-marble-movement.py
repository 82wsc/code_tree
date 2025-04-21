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

move_dir = d[o]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

# simulation 진행
for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    # 범위 안에 들어온다면 그대로 진행합니다.
    if in_range(nx, ny):
        x, y = nx, ny
    # 벽에 부딪힌다면, 방향을 바꿔줍니다.
    else:
        move_dir = 3 - move_dir

print(x+1,y+1)