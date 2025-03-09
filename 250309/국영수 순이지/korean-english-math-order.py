import sys

class student:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    kor,eng,math = int(kor), int(eng),int(math)
    l.append(student(name,kor,eng,math))

l.sort(key = lambda x: (-x.kor,-x.eng,-x.math))

for i in range(n):
    print(l[i].name,l[i].kor,l[i].eng,l[i].math)