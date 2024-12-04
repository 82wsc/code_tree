import sys

n = int(sys.stdin.readline())

def target_number(x):
    return x%2==0 and ((x//10)+(x%10))%5==0

cnt = 0
if target_number(n):
    print('Yes')
else:
    print('No')