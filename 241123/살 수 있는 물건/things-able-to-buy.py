import sys

n = int(sys.stdin.readline())

if n<1000:
    print('no')
elif n<3000:
    print('mask')
else:
    print('book')