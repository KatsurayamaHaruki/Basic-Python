a, op, b = map(str, input().split())

while (op != '?'):
    if(op == '+'):
        print(int(a)+int(b))
    elif(op == '-'):
        print(int(a)-int(b))
    elif(op == '*'):
        print(int(a)*int(b))
    else:
        print(int(a)//int(b))
    a, op, b = map(str, input().split())
