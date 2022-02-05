# coding = utf-8
# @author:yingzhudashu

file = open('A.txt', "r", encoding='UTF-8')
fi = open('A-plus-3.txt', "w", encoding='UTF-8')

li0 = []
li = []

for line in file:
    li0 = line.split(' ')
    l = len(li0)
    for i in range(l):
        if li.count(li0[i]) == 0:
            li.append(li0[i])
        else:
            continue

str0 = ' '.join(li)
fi.write(str0)

file.close()
fi.close()