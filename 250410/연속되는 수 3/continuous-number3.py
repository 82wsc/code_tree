import sys

n = int(sys.stdin.readline())

l=[int(sys.stdin.readline()) for _ in range(n)]

max_c, cnt = 0, 0
for i in range(n):
    if i >= 1 and l[i]*l[i-1]>0:
        cnt +=1
    else:
        cnt =1

    max_c = max(max_c,cnt)

print(max_c)