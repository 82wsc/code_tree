import sys

n = int(sys.stdin.readline())

l = [
    list(map(int,sys.stdin.readline().split()))
    for _ in range(n)
]

max_sum = -sys.maxsize

for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for x in range(n-2):
                if i == k:
                    if j <= x <= j + 2 or x <= j <= x + 2:
                        continue
                max_sum = max(max_sum,sum(l[i][j:j+3])+sum(l[k][x:x+3]))

print(max_sum)        