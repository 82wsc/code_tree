import sys

s = list(sys.stdin.readline())

x,y = 0,0

dxs, dys = [0,1,0,-1],[1,0,-1,0]
dir_num = 0
cnt=0

for i in s:
    cnt+=1
    if i =="R":
        dir_num = (dir_num + 1) % 4

    if i =="L":
        dir_num = (dir_num - 1) % 4

    if i =="F":
        x,y = x+dxs[dir_num],y+dys[dir_num]

    if x==0 and y ==0:
        print(cnt)
        break

if x!=0 and y!=0:
    print(-1)