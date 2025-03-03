text = input()
pattern = input()

# Please write your code here.
def word_check(x,y):
    if y in x:
        print(x.index(y))
    else:
        print(-1)

word_check(text,pattern)