import sys

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))

cnt = 0
for i in range(n):
    for j in range(i,n):
        temp = []
        for k in range(i,j+1):
            temp.append(arr[k])
        temp_sum = sum(temp)
        temp_avg = temp_sum/len(temp)
        if temp_avg in temp:
            cnt +=1

print(cnt)