class Dice:
    def __init__(self, eyes):
        self.__T = eyes[0]
        self.__S = eyes[1]
        self.__E = eyes[2]
        self.__W = eyes[3]
        self.__N = eyes[4]
        self.__B = eyes[5]

    def turn(self, order):
        if order == 'E':
            self.__T, self.__E, self.__B, self.__W = self.__W, self.__T, self.__E, self.__B
        elif order == 'W':
            self.__T, self.__W, self.__B, self.__E = self.__E, self.__T, self.__W, self.__B
        elif order == 'N':
            self.__T, self.__N, self.__B, self.__S = self.__S, self.__T, self.__N, self.__B
        elif order == 'S':
            self.__T, self.__N, self.__B, self.__S = self.__N, self.__B, self.__S, self.__T

    def print_surface(self):
        eyes = [i for i in range(6)]
        eyes[0] = self.__T
        eyes[1] = self.__S
        eyes[2] = self.__E
        eyes[3] = self.__W
        eyes[4] = self.__N
        eyes[5] = self.__B
        return eyes

    def print_reverce(self):
        eyes = [i for i in range(6)]
        eyes[5] = self.__T
        eyes[1] = self.__S
        eyes[3] = self.__E
        eyes[2] = self.__W
        eyes[4] = self.__N
        eyes[0] = self.__B
        return eyes


def compare(surface, pattern):
    dice = Dice(surface)
    flag = 0

    for i in range(3):
        if pattern == dice.print_surface():
            flag = 1
        if pattern == dice.print_reverce():
            flag = 1
        for t in range(3):
            dice.turn('N')
            if pattern == dice.print_surface():
                flag = 1
            if pattern == dice.print_reverce():
                flag = 1
        dice.turn('E')
    return flag


n = int(input())
pattern = [[]*6]*n
flag = 0
for i in range(n):
    pattern[i] = list(map(int, input().split()))

for i in range(n):
    for t in range(i+1, n):
        if compare(pattern[i], pattern[t]) == 1:
            flag = 1

if flag == 0:
    print("Yes")
else:
    print("No")
