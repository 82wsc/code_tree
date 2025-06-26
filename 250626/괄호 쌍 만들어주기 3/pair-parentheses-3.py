import sys

s = list(sys.stdin.readline())

cnt = 0
n=len(s)

for i in range(n):
    if s[i] =='(':
        for j in range(i+1,n):
            if s[j] == ')':
                cnt +=1

print(cnt)