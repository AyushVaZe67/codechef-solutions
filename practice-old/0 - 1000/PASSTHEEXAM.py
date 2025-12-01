# cook your dish here
T = int(input())
for i in range(T):
    a, b, c = map(int, input().split())
    if (a+b+c) >= 100 and (a>=10 and b>= 10 and c >= 10):
        print('PASS')
    else:
        print('FAIL')