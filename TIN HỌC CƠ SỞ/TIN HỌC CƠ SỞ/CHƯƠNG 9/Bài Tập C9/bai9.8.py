# kiem tra số hoàn hảo
def kiemtra_so_hoan_hao(x):
      tong=0
      for i in range(1,x):
            if x%i == 0:
                  tong+= i
      if tong==x:
            print(x,'là số hoàn hảo')
      else:
            print(x,'không phải là số hoàn hảo')
x=int(input('nhập x='))
kiemtra_so_hoan_hao(x)
