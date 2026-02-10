# cook your dish here
T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    print('yes' if (Y*10) < X else 'no')