import sys

n = int(sys.stdin.readline())

l = [
    list(map(int,sys.stdin.readline().split()))
    for _ in range(n)
]

min_dis = sys.maxsize 
for i in range(1,n-1):
    temp = l[0:i] + l[i+1:]
    dis = 0
    for j in range(len(temp)-1):
        x1, y1 = temp[j]
        x2, y2 = temp[j + 1]
        distance = abs(x1 - x2) + abs(y1 - y2)
        dis += distance

    min_dis = min(min_dis,dis)
    
print(min_dis)
    


