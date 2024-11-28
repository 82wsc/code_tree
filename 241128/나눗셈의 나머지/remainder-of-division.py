import sys

a,b = map(int,sys.stdin.readline().split())
cnt=[]
s=0
while a>1:
    cnt.append(a%b)
    a=a//b

for i in set(cnt):
    if i==0:
        c=cnt.count(i)+1
        s+=1**c
    else:
        c=cnt.count(i)    
        s+=2**c
print(s)