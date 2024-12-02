import sys

a = sys.stdin.readline().strip()

if chr(ord(a))=='a':
    print('z')
else:
    print(chr(ord(a)-1))