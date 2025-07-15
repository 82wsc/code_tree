import sys

r, c = map(int, sys.stdin.readline().split())

arr = [
    list(sys.stdin.readline().split())
    for _ in range(r)
]

count = 0

for i in range(1, r - 1):       
    for j in range(1, c - 1):
        if arr[i][j] == arr[0][0]:
            continue
        for k in range(i + 1, r-1):     
            for l in range(j + 1, c-1): 
                if arr[k][l] == arr[i][j]:
                    continue
                if arr[k][l] == arr[r - 1][c - 1]:
                    continue
                count += 1
                
print(count)
