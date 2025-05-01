import sys

n, m = map(int,sys.stdin.readline().split())

l = [
    [0] * n
    for _ in range(n)
]

dxs,dys = [0,1,0,-1],[1,0,-1,0]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n


for _ in range(m):
    r,c = map(int,sys.stdin.readline().split())
    l[r-1][c-1] += 1

    cnt = 0
    for i in range(4):
        if in_range(r-1+dxs[i],c-1+dys[i])and l[r-1+dxs[i]][c-1+dys[i]] == 1:
            cnt += 1

    if cnt==3:
        print(1)
    else:
        print(0)