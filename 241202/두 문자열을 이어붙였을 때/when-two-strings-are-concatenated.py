import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

if (a+b) == (b+a):
    print('true')
else:
    print('false')