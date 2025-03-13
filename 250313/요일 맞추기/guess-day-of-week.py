import sys

m1,d1,m2,d2 = map(int,sys.stdin.readline().split())

day = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
month = [31,28,31,30,31,30,31,31,30,31,30,31]

def count_date(w,x,y,z):    
    count_date = 0
    if w==y:
        count_date = z-x
    else:
        count_date = (month[w-1]-x)+sum(month[w:y-1])+z

    count_date %=7
    
    print(day[count_date])

count_date(m1,d1,m2,d2)
