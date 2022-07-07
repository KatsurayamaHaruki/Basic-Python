a, b, c = map(int, input().split())

m1 = min(a, b, c)
m3 = max(a, b, c)

if (m1 == a or m3 == a) and (m1 == b or m3 == b):
    m2 = c
elif(m1 == a or m3 == a) and (m1 == c or m3 == c):
    m2 = b
else:
    m2 = a

print(m1, m2, m3)
