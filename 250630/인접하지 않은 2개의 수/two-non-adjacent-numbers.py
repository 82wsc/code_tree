import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))

max_sum = 0
for i in range(len(l)):
    for j in range(i+2,len(l)):
        max_sum = max(max_sum,l[i]+l[j])

print(max_sum)