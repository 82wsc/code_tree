import sys

n = int(sys.stdin.readline())

max_r =200
offset = 100

segments = [
    tuple(map(int,sys.stdin.readline().split()))
    for _ in range(n)
]

l = [[0 for _ in range(max_r+1)] for _ in range(max_r+1)]

for x1,y1 in segments:
    x1 += offset
    y1 += offset

    for i in range(x1,x1+8):
        for j in range(y1,y1+8):
            l[i][j] += 1

area = 0

for i in range(max_r+1):
    for j in range(max_r+1):
        if l[i][j] == 1:
            area+=1
        elif l[i][j] == 2:
            area+=1
        elif l[i][j] == 3:
            area+=1

print(area)