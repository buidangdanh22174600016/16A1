b=int(input("nhap so "))
c=1
h=0
while c<b:     
     if (b%c==0):
         h=h+c
         print(h)
     c+=1
if h==b:
     print(b,"la so hoan hao")
else :
     print(b," khong phai so hoan hao")