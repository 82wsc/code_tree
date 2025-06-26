import sys

s = list(sys.stdin.readline())

cnt = 0
n=len(s)

for i in range(n):
        for j in range(i+1,n):
            if s[i] == '(' and s[j] == ')':
                cnt +=1

print(cnt)