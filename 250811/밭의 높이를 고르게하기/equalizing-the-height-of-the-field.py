import sys

n, h, t = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

cnt = 0
for i in range(n-t+1):
    sum_arr = []
    for j in range(i,i+t):
        sum_arr.append(arr[j])
    if sum(sum_arr) == (h*t):
        for i in range(len(sum_arr)):
            if sum_arr[i]!=h:
                cnt += abs(h-sum_arr[i])

print(cnt)