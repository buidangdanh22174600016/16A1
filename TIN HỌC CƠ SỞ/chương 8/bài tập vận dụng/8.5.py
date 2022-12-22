a= int(input("nhap nam "))
if ((a%4==0)and(a%100!=0))or(a%400==0):
     print(a,"la nam nhuan")
else:
     print(a,"ko phai nam nhuan")