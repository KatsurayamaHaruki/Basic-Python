ch = [0 for i in range(26)]
while True:
    try:
        s = input()
        for i in s:
            if ord(i.lower()) >= 97 and ord(i.lower()) <= 122:
                ch[ord(i.lower())-97] += 1
    except EOFError:
        break

for i in range(26):
    print(f"{chr(i+97)} : {ch[i]}")
