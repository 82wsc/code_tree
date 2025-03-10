import sys

a,b,c = map(int,sys.stdin.readline().split())


def count_mins(x,y,z):
    total_mins = 0
    days = x-11
    hours = y-11
    mins = z-11

    print(days*24*60+hours*60+mins)

count_mins(a,b,c)
