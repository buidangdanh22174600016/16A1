# Từ điển Anh-Việt
dic1={
"Từ Anh":"Nghĩa Việt",
"cat"  : "con mèo",
"dog"  : "con chó",
"ant"  : "con kiến",
"bear" : "con gấu"
}
# Hiển thị từ điển
for key in dic1:
    print(key,":",dic1[key])
# trong từ điển có bao nhiêu từ
print("Trong từ điển có:",len(dic1),"từ")

while True:
    print("Bạn muốn làm gì? 1: Xem từ điển, 2: Tra từ, 3: Thêm từ, 4: Xóa từ")
    a=int(input())
    if a==1:
        print("Dictionary:")
        for key in dic1:
            print(key,":",dic1[key])
# Tra từ tiếng anh trong từ điển
    if a==2:
        b=input("Nhập từ cần tra:")
        if b in dic1:
            print(b,"nghĩa là:",dic1[b])
            print("Dictionary:")
            for key in dic1:
                print(key,":",dic1[key])
            
        else:
            if b not in dic1:
                print("Không tìm thấy trong từ điển")
# Thêm từ vào từ điển 
    if a==3:
        keyy=input("Nhập từ Tiếng Anh:")
        valuee=input("Nhập nghĩa Tiếng Anh sang tiếng Việt:")
        dic1[keyy]=valuee
        print("Dictionary:")
        for key in dic1:
            print(key,":",dic1[key])
# Xóa một từ trong từ điển dựa trên key cung cấp
    if a==4:
        d=input("Nhập từ tiếng anh muốn xóa:")
        c=input("Bạn có thật sự muốn xóa không 1: có, 0:không")
        if c==1:
            del dic1[d]
            print("Đã xóa từ trong từ điển")
        else:
            if c==0:
                print("Không xóa")
        print("Dictionary:")        
        for key in dic1:
            print(key,":",dic1[key])
    n=int(input("tiếp tục lựa chọn hay không 1: có, 0: không"))
    if n==1:
        
        continue
    a=int(input("Bạn muốn làm gì? 1: Xem từ điển, 2: Tra từ, 3: Thêm từ, 4: Xóa từ"))
    if n==0:
        break
