import sys

n = int(sys.stdin.readline())
idx=0

while n>=1:
    idx+=1
    n=n//idx    

print(idx)

# 8
# 8//1 = 8
# 8//2 = 4
# 4//3 = 1
# 1//4 = 1