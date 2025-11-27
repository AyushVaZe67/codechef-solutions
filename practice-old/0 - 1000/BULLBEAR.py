# cook your dish here
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x > y:
        print('LOSS')
    elif x < y:
        print('PROFIT')
    else:
        print('NEUTRAL')