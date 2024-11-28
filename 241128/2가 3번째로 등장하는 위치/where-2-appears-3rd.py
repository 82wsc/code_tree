import sys
 
n = int(sys.stdin.readline())

l = list(map(int,sys.stdin.readline().split()))
idx=0

for i in range(len(l)):
    if l[i]==2:
        idx+=1
    if idx==3:
        print(i+1)
        break
        


