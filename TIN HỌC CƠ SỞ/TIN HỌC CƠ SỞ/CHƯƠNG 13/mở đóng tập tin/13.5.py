# ví dụ về con trỏ tậ tin
f =open("bai_tho.txt","r+")
a = f.read(12)
print("nội dung là :\n",a)
b=f.tell()
print("vị trí hiện tại")