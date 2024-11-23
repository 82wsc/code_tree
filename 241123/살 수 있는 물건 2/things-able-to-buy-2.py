import sys

n = int(sys.stdin.readline())

if n<500:
    print('no')
elif n<1000:
    print('pen')
elif n<3000:
    print('mask')
else:
    print('book')