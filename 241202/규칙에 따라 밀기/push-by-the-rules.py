import sys

a = sys.stdin.readline().strip()

o = sys.stdin.readline().strip()

for i in o:
    if i=='L':
        temp = a[0]
        a = a[1:]+temp
     
    else:  
        temp = a[-1]
        a = temp + a[:-1]

print(a)