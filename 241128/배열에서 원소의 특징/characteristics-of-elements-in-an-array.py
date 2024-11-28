import sys

a = list(map(int,sys.stdin.readline().split()))

for i in range(len(a)):
    if a[i]%3==0:
        print(a[i-1])
        break
