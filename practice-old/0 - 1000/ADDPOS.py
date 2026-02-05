import math

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    S = sum(A)
    
    if S >= 0:
        print(0)
    else:
        print(math.ceil(-S / N))
