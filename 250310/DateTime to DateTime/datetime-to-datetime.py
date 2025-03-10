import sys

a,b,c = map(int,sys.stdin.readline().split())


def count_mins(x,y,z):
    total_mins = 0
    if x<=11 and y<=11 and z<11:
        total_mins=-1

    else:
        days = x-11
        hours = y-11
        mins = z-11

        total_mins=days*24*60+hours*60+mins
    print(total_mins)

count_mins(a,b,c)
