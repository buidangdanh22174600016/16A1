# xây dựng module my_module.py có chứa hàm tính_bmi(cân nặng, chiều cao)
import math
def tinh_bmi(cân_nặng , chiều_cao):
    bmi=cân_nặng/math.pow(chiều_cao,2)
    return bmi