import sys

a = int(sys.stdin.readline())

if a%2==1:
    a+=3

if a%3==0:
    a=a/3

print(int(a))