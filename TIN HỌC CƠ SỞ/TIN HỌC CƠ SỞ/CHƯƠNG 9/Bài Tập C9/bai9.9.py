#tính diện tích ,chu vi
import math
r=float(input('Nhập bán kính :'))
a=float(input('Nhập chiều dài:'))
b=float(input('Nhập chiều rộng:'))

def dientich_hcn(a,b):
      S= lambda a,b:a*b
      return S(a,b)

def chuvi_hcn(a,b):
      CV= lambda a,b:(a+b)*2
      return CV(a,b)

def dientich_ht(r):
      S= lambda r:math.pi*pow(r,2)
      return S(r)

def chuvi_ht(r):
      CV= lambda r:math.pi*r*2
      return CV(r)

print('Diện tích hình chữ nhật với chiều dài ',a,'chiều rộng',b,'là: %0.2f'%dientich_hcn(a,b))
print('Chu vi hình chữ nhật với chiều dài ',a,'chiều rộng',b,'là: %0.2f'%chuvi_hcn(a,b))
print('Diện tích hình tròn với bán kính',r,'là: %0.2f'%dientich_ht(r))
print('Chu vi hình tròn với bán kính',r,'là: %0.2f'%chuvi_ht(r))