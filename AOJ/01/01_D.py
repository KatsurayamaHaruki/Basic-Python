x = int(input())

s = x % 60
m = ((x-s)//60) % 60
h = ((x-s-60*m)//3600) % 60

print(str(h)+":"+str(m)+":"+str(s))
