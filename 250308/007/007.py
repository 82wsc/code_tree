import sys



class secret:
    def __init__(self,code,place,time):
        self.code = code
        self.place = place
        self.time = time

a,b,c = sys.stdin.readline().split()
c = int(c)

secret1 = secret(a,b,c)

print('secret code :',secret1.code)
print('meeting point :',secret1.place)
print('time :',secret1.time)

