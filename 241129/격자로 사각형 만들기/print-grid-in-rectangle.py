import sys

n = int(sys.stdin.readline())

l = [[1 for _ in range(n)] for _ in range(n)]

for i in range(1,n):
    for j in range(1,n):
        l[i][j] = l[i-1][j-1] + l[i-1][j] + l[i][j-1]

for i in range(n):
    print(*l[i], sep=' ')