# cook your dish here
T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    if (y - x) < 0:
        print('NO')
    elif (y - x) <= 200:
        print('YES')
    else:
        print('NO')   