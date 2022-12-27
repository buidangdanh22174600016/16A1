a=int(input("nhap a "))
b=int(input("nhap b "))
if a>=b:
     c=a
else :
     c=b
if (a==b)or(a%b==0)or(b%a==0):
     print(a,"la boi chung nho nhat")
while (c%a!=0)or(c%b!=0):
     c+=1
     if (c%a==0)and(c%b==0):
         print(c,"la boi chung nho nhat")
         break
