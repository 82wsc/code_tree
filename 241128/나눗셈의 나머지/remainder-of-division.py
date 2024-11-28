import sys

a,b = map(int,sys.stdin.readline().split())
cnt=[]
s=0
while a>1:
    cnt.append(a%b)
    a=a//b

for i in set(cnt):
    c=cnt.count(i)
    s+=c**2
print(s)