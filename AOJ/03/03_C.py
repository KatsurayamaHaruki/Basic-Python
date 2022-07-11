for i in range(3000):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    print(min(x, y), max(x, y))
