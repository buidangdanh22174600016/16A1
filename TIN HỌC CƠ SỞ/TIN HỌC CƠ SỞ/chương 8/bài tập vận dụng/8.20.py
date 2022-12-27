a=int(input("nhap e mu x "))
i=1
k=1
t=0
x=1
d=0
while i<=1000:
     k=k*a
     while t<=i:
         t+=1
         x=x*t
         if (t == i):
                 t=0
                 l=x
                 x=1
                 break
     m=k/l
     d=d+m   
     i+=1
print("e mu x=",d+1)



     

   
