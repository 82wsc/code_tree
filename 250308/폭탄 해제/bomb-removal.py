import sys

class bomb_kit:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second

code, color, second = sys.stdin.readline().split()
second = int(second)

bomb_kit1 = bomb_kit(code,color,second)

print(f"code : {bomb_kit1.code}")
print(f"color : {bomb_kit1.color}")
print(f"second : {bomb_kit1.second}")