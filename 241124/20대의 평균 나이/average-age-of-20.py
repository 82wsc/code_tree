import sys



count=0
total=0

while True:
    n = int(sys.stdin.readline())
    if n<30:
        total+=n
        count+=1
    else:
        break
                
print(f"{total/count:.2f}")