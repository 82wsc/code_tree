import sys

n = int(sys.stdin.readline())

x, y= 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

segments =[
    tuple(sys.stdin.readline().split())
    for _ in range(n)
]

for d, i in segments:
    i = int(i)

    if d=='N':
        dir_num = 3
    
    elif d=='S':
        dir_num = 1

    elif d=='W':
        dir_num = 2

    elif d=='E':
        dir_num = 0

    x,y = x + dx[dir_num] * i , y+dy[dir_num] * i

print(x,y)