s = []
for i in range(10001):
    s.insert(i, int(input()))
    if s[i] == 0:
        break

for i in range(len(s)-1):
    print(f"Case {i+1}: {s[i]}")
