x=[[12,7,3],[4,5,6],[7,8,9]]
y =[[5,8,1],[6,7,3],[4,5,9]]
sum_x_y =[[0,0,0],[0,0,0,],[0,0,0]]
# Duyệt qua từng dòng
for i in range(len(x)):
    # duyệt qua tùng cột
    for j in range(len(x[0])):
        sum_x_y[i][j]= x[i][j]+y[i][j]
        for k in sum_x_y:
            print(k)