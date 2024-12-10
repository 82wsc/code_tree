import sys

def other_alpha(s):
    if set(s)==1:
        print('No')
    else:
        print('Yes')

a = sys.stdin.readline().strip()

other_alpha(a)