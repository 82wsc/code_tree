import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

min_sum = sys.maxsize

for i in range(n):
    
    sum_diff = 0
    
    for j in range(n):
        sum_diff += a[j] * abs(j-i)

    min_sum = min(min_sum, sum_diff)

print(min_sum)