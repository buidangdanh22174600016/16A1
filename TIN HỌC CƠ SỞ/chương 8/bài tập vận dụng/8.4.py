import math

a = int(input("canh thu nhat "))
b = int(input("canh thu hai "))
c = int(input("canh thu ba "))
p=(a+b+c)/2
h=math.sqrt(p*(p-a)*(p-c)*(p-b))
print("dien tich tam giac la",h)
