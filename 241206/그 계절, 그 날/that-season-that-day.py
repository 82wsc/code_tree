import sys

y,m,d = map(int,sys.stdin.readline().split())

def l_year(x):
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        return True
    return False

def last_day_number(y,m):
    if l_year(y):
        if m == 2:
            return 29
    else:
        if m == 2:
            return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30    
    return 31

# 윤년이 아닐 때 m월 d일이 존재하는지 여부를 확인하는 함수를 작성합니다.
def judge_day(y, m, d):
    if m <= 12 and d <= last_day_number(y,m):
        return True
    return False

def season(y,m,d):
    if judge_day(y,m,d):
        if 1<=m<=2 or m==12:
            return 'Winter'
        elif 3<=m<=5:
            return 'Spring'
        elif 6<=m<=8:
            return 'Summer'
        elif 9<=m<=11:
            return 'Fall'
    else:
        return -1

print( season(y,m,d))

