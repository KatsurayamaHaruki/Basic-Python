cards = [[0 for i in range(13)] for j in range(4)]
pattern = ["S", "H", "C", "D"]

n = int(input())
for i in range(n):
    ch, rank = map(str, input().split())
    rank = int(rank)
    cards[pattern.index(ch)][rank-1] = 1

for i in range(4):
    for j in range(13):
        if cards[i][j] == 0:
            print(pattern[i], j+1)
