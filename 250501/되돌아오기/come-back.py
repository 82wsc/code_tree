import sys

n = int(sys.stdin.readline())

x,y = 0,0
dxs,dys = [0,1,-1,0],[1,0,0,-1]

d = {
    'N':0,
    'E':1,
    'W':2,
    'S':3
}

cnt=0

for _ in range(n):
    o,t = sys.stdin.readline().split()
    t = int(t)

    for i in range(t):
        cnt+=1
        x,y = x+dxs[d[o]], y+dys[d[o]]
        if x==0 and y==0:
            print(cnt)
            break
    if x==0 and y==0:
        break

if x!=0 and y!=0:
    print(-1)