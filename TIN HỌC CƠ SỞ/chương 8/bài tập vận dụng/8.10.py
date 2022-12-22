a=int(input("nhap n "))
b=int(input("nhap x "))
t=(b*b+1)
i=1
h=1
while i<=a:
     h=h*t
     i+=1
print("S=(x*x+1)^n=",h)