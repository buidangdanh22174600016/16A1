a=int(input("nhap n "))
k=0
while a>0:
     print("nhap so thu ",a)
     h=int(input())
     k=k+h
     a-=1
     if a==0:
         print("tong cac so bang",k)
         break