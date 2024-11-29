import sys

n = int(sys.stdin.readline())
l=[]
for _ in range(n):
    l.append(sys.stdin.readline().strip())

s = sys.stdin.readline()
r=''
cnt=0
for i in l:
    if i[0]==s:
        r+=i
        cnt+=1

print(f'{cnt} {len(r)/cnt:.2f}')
