import sys

n, k = map(int,sys.stdin.readline().split())

arr = [0 for _ in range(100)]

for i in range(n):
    y,x = map(int,sys.stdin.readline().split())

    arr[x-1] = y

ans = -sys.maxsize
for i in range(100-(k*2)):
    sum_arr = 0
    for j in range(i,i+(2*k)+1):
        sum_arr += arr[j]
    
    ans = max(ans,sum_arr)

print(ans)

