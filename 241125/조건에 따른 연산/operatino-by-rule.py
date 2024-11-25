import sys

n = int(sys.stdin.readline())
cnt=0

while n<1000:
    
    if n%2==0:
        n = n*3+1
    else:
        n = n*2+2
    cnt+=1
print(cnt)

# n이 짝수일 때, n에 3을 곱하고 1을 더합니다.

# n이 홀수일 때, n에 2를 곱하고 2를 더합니다.