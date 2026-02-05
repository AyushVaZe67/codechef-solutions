X, Y, Z = map(int, input().split())

played = X + Y + Z
remaining = 4 - played

max_points = X + 0.5 * Y + remaining

if max_points > 2:
    print("YES")
else:
    print("NO")