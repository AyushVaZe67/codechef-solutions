# cook your dish here
T = int(input())
y = []

for _ in range(T):
    count = 0
    n, x = map(int, input().split())
    y = list(map(int, input().split()))
    for i in range(n):
        if y[i] >= x:
            count += 1
            
    # print(n ,x)
    # print(y)
    print(count)