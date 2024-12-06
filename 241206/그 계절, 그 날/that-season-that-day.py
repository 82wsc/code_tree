import sys

y,m,d = map(int,sys.stdin.readline().split())

def l_year(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        return False
    return True

def exist_date(y,m,d):
    if l_year(y)==False and m==2 and d>=29:
        return -1
    if (m==4 or m==6 or m==9 or m==11) and d==31:
        return -1
    return 1

def season(m):
    if 3<=m<=5:
        return 'Spring'
    elif 6<=m<=8:
        return 'Summer'
    elif 9<=m<=11:
        return 'Fall'
    elif 1<=m<=2 or m==12:
        return 'Winter'
    
if exist_date(y,m,d)==1:
    print(season(m))
else:
    print(exist_date(y,m,d))