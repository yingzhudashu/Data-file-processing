# coding = utf-8
# @author:yingzhudashu

f = open('A.txt', 'r', encoding='UTF-8')
f0 = open("A-plus-2.txt", "w", encoding='UTF-8')

# 设定想要去除的字符
li = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', ':',
        'v', 'w', 'x', 'y', 'z', ' ', '-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '>',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']

a = f.read(1)
while a != '':
    if a not in li:
        f0.write(a)
    a = f.read(1)