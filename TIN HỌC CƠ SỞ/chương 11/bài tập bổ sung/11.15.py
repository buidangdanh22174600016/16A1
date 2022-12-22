dictionary={
    'cat':'con mèo',
    'dog':'con chó',
    'ant':'con kiến',
    'bear':'con gấu'
}
for name in dictionary:
    print(name)
    print('bạn muốn tìm cái gì')
name = input()
if name in dictionary:
    print('0')
else:
    print('1')
