import sys

n = int(sys.stdin.readline())

l = list(map(int,sys.stdin.readline().split()))

cnt = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if abs(l[0]-i)>2 and abs(j-l[1])>2 and abs(k-l[2])>2:
                cnt +=1

print(n**len(l)-cnt)