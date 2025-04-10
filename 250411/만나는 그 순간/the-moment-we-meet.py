import sys

n,m = map(int,sys.stdin.readline().split())

max_r = 1000

l_a = [0 for _ in range(max_r)]
l_b = [0 for _ in range(max_r)]

print(l)

segments_a = [
    tuple(sys.stdin.readline().split())
    for _ in range(n)
]

segments_b = [
    tuple(sys.stdin.readline().split())
    for _ in range(m)
]

for d,i in segments_a:
    i = int(i)
    if d=='R':
        for x in range(1,i):
            l_a[x] = l_a[x-1] + 1
            
    if d=='L':
        for x in range(1,i):
            l_a[x] = l_a[x-1] - 1

for d,i in segments_b:
    i = int(i)
    if d=='R':
        for x in range(1,i):
            l_b[x] = l_b[x-1] + 1
            
    if d=='L':
        for x in range(1,i):
            l_b[x] = l_b[x-1] - 1

print(l_a)
print(l_b)




    
