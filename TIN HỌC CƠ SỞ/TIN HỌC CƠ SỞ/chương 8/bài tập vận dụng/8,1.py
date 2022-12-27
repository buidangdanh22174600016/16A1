a=int(input("so a "))
b=int(input("so b"))
c = int (input ("so c " ))
d = int (input ("so d " ))
g = 0
h = 0
while (g < a) or (g < b) or (g < c) or (g < d):
     g +=1
h = g     
while (h > a) or (h > b) or (h > c) or (h > d):
     h -=1
     print("max :", g)
     print("min :", h)


