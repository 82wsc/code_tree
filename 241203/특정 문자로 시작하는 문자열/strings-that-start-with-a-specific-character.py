import sys

n = int(sys.stdin.readline())
s=[]
r=''
cnt=0
for _ in range(n):
    s.append(sys.stdin.readline().strip())

c=sys.stdin.readline().strip()

for i in range(len(s)):
    if s[i][0]==c:
        r+=s[i]
        cnt+=1

print(f'{cnt} {len(r)/cnt:.2f}')

