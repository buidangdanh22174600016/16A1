a=int(input("nhap a "))
b=int(input("nhap b "))
c=2
while (a%c!=0)or(b%c!=0):
     c+=1
     if (a%c==0)and(b%c==0):
         print(c,"la uoc chung nho nhat")
         break
     if c>b and c>a:
         print("ko co uoc chung nho nhat")
         break    