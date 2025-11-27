# cook your dish here
x, y = map(int, input().split())
if (y // x) == ( y / x):
    print(int((y/x)-1))
else:
    print(int(y // x))