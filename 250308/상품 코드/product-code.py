import sys

class item:
    def __init__(self,name,code):
        self.name=name
        self.code=code

item1 = item('codetree',50)

i2_name, i2_code = sys.stdin.readline().split()
i2_code = int(i2_code)
item2 = item(i2_name,i2_code)

print(f"product {item1.code} is {item1.name}")
print(f"product {item2.code} is {item2.name}")