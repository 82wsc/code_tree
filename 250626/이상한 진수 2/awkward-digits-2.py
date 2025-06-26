import sys

a = list(sys.stdin.readline().strip())

n = len(a)

sum_diff = -sys.maxsize

for i in range(n):
    a_copy = a[:]
    temp = 0

    if a_copy[i]=='0':
        a_copy[i]='1'

    for j in range(n):
        temp += (2**(n-j-1))* int(a_copy[j])

    sum_diff = max(sum_diff,temp)

if sum_diff == 1:
    print(0)
else:
    print(sum_diff)