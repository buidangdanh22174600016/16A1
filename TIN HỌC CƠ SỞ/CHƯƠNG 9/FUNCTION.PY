print("Chương trình tính điểm trung bình của học sinh")
 
toan = 0; ly = 0; hoa = 0; van = 0; anh = 0
 
def nhap_diem():
    """Hàm yêu cầu nhập điểm và trả về giá trị trung bình"""
    # Bước 1: Nhập dữ liệu
    print("Nhập điểm môn toán: ")
    toan = float(input())
 
    print("Nhập điểm môn Lý: ")
    ly = float(input())
 
    print("Nhập điểm môn Hóa: ")
    hoa = float(input())
 
    print("Nhập điểm môn Văn: ")
    van = float(input())
 
    print("Nhập điểm môn Anh: ")
    anh = float(input())

 
    # Bước 2: Tính điểm trung bình
    trungbinh = (toan + ly + hoa + van + anh) / 5
 
    return trungbinh
 
 
def in_ket_qua(diem):
    """Hàm in kết quả lên màn hình"""
    print("Điểm trung bình là: ", trungbinh)
    if (diem < 5):
        print("Học lực yếu")
    elif (diem >= 5 and diem < 7):
        print("Học lực trung bình")
    elif (diem >= 7 and diem < 9):
        print("Học lực khá")
    elif (diem >= 9):
        print("Học lực giỏi")
 
 
# Sử dụng hàm
trungbinh = nhap_diem()
in_ket_qua(trungbinh)