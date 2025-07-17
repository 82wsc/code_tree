import sys

n, k = map(int,sys.stdin.readline().split())

l=['' for _ in range(10000)]

for _ in range(n):
    temp = tuple(sys.stdin.readline().split())
    l[int(temp[0])] = temp[1]

high_score = -sys.maxsize
for i in range(0,len(l)-k):
    score = 0
    for j in range(i,i+k+1):
        if l[j]=='G':
            score += 1
        elif l[j]=='H':
            score += 2

    high_score = max(high_score,score)

print(high_score)