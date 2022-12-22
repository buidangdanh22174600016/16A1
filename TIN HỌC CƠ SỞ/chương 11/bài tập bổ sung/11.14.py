# dictionary of Danh Bạ
Danh_Bạ={
    'Minh':'0989741258',
    'Hạnh':'0903852147',
    'Bình':'0913753951',
    'An':'0933753654'
}
print("chào mừng các bạn đến từ điền danh bạ. chúng tôi biết Danh Bạ của: ")
for name in Danh_Bạ:
    print(name)
    print('bạn muốn biết danh bạ của ai:')
name=input()
if name in Danh_Bạ:
    print(f'{name}\'s Danh Bạ của {Danh_Bạ[name]}')
else:
    print(f'sadly,we don\'t have {name}\'s danh bạ')    





