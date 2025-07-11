import sys

n = int(sys.stdin.readline())

l = [
    list(map(int,sys.stdin.readline().split()))
    for _ in range(n)
]

sum_max = -sys.maxsize

for i in range(n-1):
    for j in range(n-2):
        sum_max = max(sum_max,sum(l[i][j:j+3])+sum(l[i+1][j:j+3]))

print(sum_max)