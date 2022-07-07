W, H, x, y, r = map(int, input().split())

if r <= x and W-r >= x and r <= y and H-r >= y:
    print("Yes")
else:
    print("No")
