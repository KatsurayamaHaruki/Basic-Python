n, x = map(int, input().split())

while n != 0 or x != 0:
    count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+1, n+1):
                if i+j+k == x:
                    count += 1
    print(count)
    n, x = map(int, input().split())
