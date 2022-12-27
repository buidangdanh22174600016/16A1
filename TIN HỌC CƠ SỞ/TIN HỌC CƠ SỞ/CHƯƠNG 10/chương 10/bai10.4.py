import math
def tinh_A(x,n):
      A=(pow(pow(x,2)+x+1,n))
      B=(pow(pow(x,2)-x+1,n))
      print('A=',A+B)
x=int(input('nhập x:'))  
n=int(input('nhập n:'))
tinh_A(x,n)