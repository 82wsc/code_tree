import sys

n = int(sys.stdin.readline())

max_r = 200
offset =100

l = [[0 for _ in range(max_r+1)] for _ in range(max_r+1)]

segments = [
    tuple(map(int,sys.stdin.readline().split()))
    for _ in range(n)
]

for i,(x1,y1,x2,y2) in enumerate(segments):
    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    if i%2==0:
        for x in range(x1,x2):
            for y in range(y1,y2):
                l[x][y] = 'R'
    else:
        for x in range(x1,x2):
            for y in range(y1,y2):
                l[x][y] = 'B'

area = 0

for i in range(max_r+1):
    for j in range(max_r+1):
        if l[i][j] == 'B':
            area +=1

print(area)