import sys

class forecast:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(sys.stdin.readline())

a = []
for _ in range(n):
    date, day, weather = sys.stdin.readline().split()
    a.append(forecast(date,day,weather))

min_cnt=0

temp=[]
for i in range(n):
    if a[i].weather == 'Rain':
        temp.append(a[i])
        
for i in range(len(temp)):
    if temp[min_cnt].date > temp[i].date:
        min_cnt=i

print(temp[min_cnt].date, temp[min_cnt].day, temp[min_cnt].weather)