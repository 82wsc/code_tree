import sys

n, k = map(int,sys.stdin.readline().split())

l = list(map(int, sys.stdin.readline().split()))

max_sum = -sys.maxsize

for i in range(n-k+1):
    max_sum = max(max_sum,sum(l[i:i+k]))

print(max_sum)