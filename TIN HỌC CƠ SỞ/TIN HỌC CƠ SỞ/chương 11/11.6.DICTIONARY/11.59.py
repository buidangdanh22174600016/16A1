dic1={(1,2,3):"abc",3.1415:"abc"}
dic2={[1,2,3]:"abc"}
# dic 1 có hai phần tử với kay là 1 tuple :(1,2,3) và 1 hằng (3.1415) là hợp lệ . tuy nhiên dic 2 sử dụng 1 list[1,2,3] làm key là không hợp lệ , vì list là có thể thay đổi được , vì vậy khi thực hiện run báo lỗi
