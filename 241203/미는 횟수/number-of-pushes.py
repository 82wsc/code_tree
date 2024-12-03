import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

cnt=0
while a!=b:
    cnt+=1
    temp=a[-1]
    a = a[-1] + a[:-1]
    if cnt==len(a):
        print(-1)
print(cnt)