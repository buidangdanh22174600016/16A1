#Tính chỉ số BMI
import math
def ham_tinh_bmi(x,y):
      BMI = x/pow(y,2)
      return BMI
x=float(input('Nhập cân nặng(kg):'))
y=float(input('Nhập chiều cao(m):'))
def ham_danh_gia_bmi(BMI):      
      if BMI < 18.5:
            print('Chỉ số BMI của bạn là %f'%BMI,'Bạn thiếu cân!!!')
      elif BMI > 25:
            print('Chỉ số BMI của bạn là %f'%BMI,'Bạn thừa cân!!!')
      else:
            print('Chỉ số BMI của bạn là %f'%BMI,'Bạn bình thường!!')
BMI=ham_tinh_bmi(x,y)
ham_danh_gia_bmi(BMI)

