import sys

a,b,c = map(int,sys.stdin.readline().split())


def count_mins(x,y,z):
    total_mins = 0
    if (x,y,z)<(11,11,11):
        total_mins=-1

    else:
        start_mins = 11*24*60+11*60+11
        end_mins = x*24*60+y*60+z
        total_mins = end_mins-start_mins
    print(total_mins)

count_mins(a,b,c)
