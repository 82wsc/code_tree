import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a = int(sys.stdin.readline())
    if a%2==1 and a%3==0:
        print(a)
    