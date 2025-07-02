import sys

n = int(sys.stdin.readline())

l=[
    int(sys.stdin.readline())
    for _ in range(n)
]

min_dis = sys.maxsize

for i in range(n):
    temp = []
    temp = l[i+1:] + l[:i+1]
    dis = 0
    for j in range(n):
        dis += temp[j]*j
    min_dis = min(dis,min_dis)

print(min_dis)