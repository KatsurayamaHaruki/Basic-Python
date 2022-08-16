x = input()

while x != '0':
    sum = 0
    for d in x:
        sum += int(d)
    print(sum)
    x = input()
