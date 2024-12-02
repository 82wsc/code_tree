import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

idx = 0

# 뭔가 b 길이 재서 그만큼만 비교하면서 넘어가면 될 거 같은데?
for i in range(len(a)-1):
    if a[i:i+2]==b:
        idx+=1
print(idx)