#Hàm Fibonacy
def fib(n):
      if n==0 & n==1: return
      else:
            return fib(n-1)+fib(n-2)
x=int(input('Nhập giá trị x='))
print('Fibonacy (',x,') =',fib(x))