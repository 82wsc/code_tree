import sys

def other_alpha(s):
    if len(set(s))>=2:
        print('Yes')
    else:
        print('No')

a = sys.stdin.readline().strip()

other_alpha(a)