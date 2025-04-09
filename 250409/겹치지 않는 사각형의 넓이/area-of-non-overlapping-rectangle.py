import sys

n = 3

segments =[
    tuple(map(int,sys.stdin.readline().split()))
    for _ in range(3)
]


max_r = 2000
offset = 1000

l = [[0 for _ in range(max_r+1)] for _ in range(max_r+1)]

for x1,y1,x2,y2 in segments[:2]:
    for i in range(offset+x1,offset+x2):
        for j in range(offset+y1,offset+y2):
            l[i][j]+=1

area = 0

for i in range(max_r+1):
    for j in range(max_r+1):
        if l[i][j]==1:
            area +=1

area_m =0

x1, y1, x2, y2 = segments[2]
for i in range(offset+x1,offset+x2):
    for j in range(offset+y1,offset+y2):
        l[i][j]+=1

for i in range(max_r+1):
    for j in range(max_r+1):
        if l[i][j]==2:
            area_m +=1

print(area-area_m)