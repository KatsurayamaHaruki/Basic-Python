x=int(input())

s = x%60
x-=s
x/=60
m=x%60
x-=m
x/=60
x+=1

print(int(x),":",int(m),":",s)
