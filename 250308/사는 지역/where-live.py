import sys

class address:
    def __init__(self,name,addr,city):
        self.name = name
        self.addr = addr
        self.city = city

n = int(sys.stdin.readline())

info=[]
for _ in range(n):
    name, addr, city = sys.stdin.readline().split()
    info.append(address(name,addr,city))

max_idx = 0
for i in range(n):
    if info[max_idx].name<info[i].name:
        max_idx = i

print(f"name {info[max_idx].name}")
print(f"addr {info[max_idx].addr}")
print(f"city {info[max_idx].city}")