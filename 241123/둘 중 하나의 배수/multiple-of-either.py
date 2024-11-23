import sys

a = int(sys.stdin.readline())

if a%3==0 or a%5==0:
    print(1)
else:
    print(0)