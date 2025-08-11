import sys

n, h, t = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

ans = sys.maxsize
for i in range(n-t+1):
    sum_arr = []
    cnt = 0
    for j in range(i,i+t):
        sum_arr.append(arr[j])
    
    for i in range(len(sum_arr)):
        cnt += abs(sum_arr[i]-h)

    ans = min(ans,cnt)


print(ans)