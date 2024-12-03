import sys

n = int(sys.stdin.readline())

def square(a):
    cnt=0    
    for i in range(a):
        for j in range(a):
            cnt+=1
            print(cnt,end=' ')
            if cnt>8:
                cnt=0
        print('')

square(n)