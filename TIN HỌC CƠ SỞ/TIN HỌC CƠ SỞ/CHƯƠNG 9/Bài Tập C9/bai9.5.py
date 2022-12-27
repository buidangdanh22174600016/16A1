#Tính A(n,x)
def tinh_A(n,x):
      S1=(x**2+x+1)**n
      S2=(x**2-x+1)**n
      print("S=",S1+S2)
      return
x=int(input('nhập x:'))
n=int(input('nhập n:'))
tinh_A(n,x)