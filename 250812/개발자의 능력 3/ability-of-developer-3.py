import sys

def get_diff(i,j,k):
    sum1 = l[i]+l[j]+l[k]
    sum2 = sum(l) - sum1
    return abs(sum1 - sum2)

l = tuple(map(int,sys.stdin.readline().split()))

min_diff = sys.maxsize

for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            min_diff = min(min_diff, get_diff(i,j,k))

print(min_diff)
