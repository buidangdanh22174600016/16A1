num = int(input("Nhập số phần tử của list : "))
mylist = []
for i in range(num):
   val = input('Nhập giá trị: ')
   mylist.append(val)
print(mylist)
s = sum(mylist)
print("tong:",s)