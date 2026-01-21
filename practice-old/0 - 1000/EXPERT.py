# cook your dish here
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if (b/a) * 100 < 50:
        print('NO')
    else:
        print('YES')