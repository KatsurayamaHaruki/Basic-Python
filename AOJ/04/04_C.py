s = list(input().split())

while (s[1] != '?'):
    if(s[1] == '+'):
        print(int(s[0])+int(s[2]))
    elif(s[1] == '-'):
        print(int(s[0])-int(s[2]))
    elif(s[1] == '*'):
        print(int(s[0])*int(s[2]))
    else:
        print(int(s[0])//int(s[2]))
    s = list(input().split())
