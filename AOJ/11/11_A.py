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

    def show_top(self):
        return self.__T


surface = list(map(int, input().split()))
moves = list(input())
dice = Dice(surface)

for i in moves:
    dice.turn(i)

print(dice.show_top())
