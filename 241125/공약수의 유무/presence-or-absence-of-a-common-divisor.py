#정수 a, b가 주어지면, a이상 b이하의 수 중에서 
# 1,920과 2,880의 공약수가 존재하는지 판단해보는 프로그램을 작성해보세요.

import sys

a,b = map(int,sys.stdin.readline().split())

r=False
for i in range(a,b+1):
    while 1920%i==0 and 2880%i==0:
        r=True
        break

if r ==True:
    print(1)

else:
    print(0)
    