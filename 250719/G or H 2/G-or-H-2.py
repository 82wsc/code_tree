import sys

n = int(sys.stdin.readline())

arr = ['' for _ in range(101)]

for _ in range(n):
    x,y = sys.stdin.readline().split()

    arr[int(x)] = y

max_len = 0
for i in range(101):
    for j in range(i+1,101):
        if arr[i]=='' or arr[j]=='':
            continue

        cnt_g = 0
        cnt_h = 0

        for k in range(i,j+1):
            if arr[k] == 'G':
                cnt_g += 1
            if arr[k] == 'H':
                cnt_h += 1
            
        if cnt_g == 0 or cnt_h ==0 or cnt_g == cnt_h:
            leng = j-i
            max_len = max(max_len,leng)

print(max_len)