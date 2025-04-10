import sys

segments = [
    tuple(map(int,sys.stdin.readline().split()))
    for _ in range(2)
]

max_r = 2000
offset = 1000

l = [[0 for _ in range(max_r+1)] for _ in range(max_r+1)]

for n,(x1,y1,x2,y2)  in enumerate(segments):
    x1 += offset
    y1 += offset
    x2 += offset
    y2 += offset

    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            l[i][j] = n+1

w = []
h = []
for i in range(max_r+1):
    for j in range(max_r+1):
        if l[i][j]==1:
            w.append(i)
            h.append(j)

area =(max(w)-min(w))*(max(h)-min(h)) 
print(area)        