# coding = utf-8
# @author:yingzhudashu

import csv

# 输入文件格式：csv文件（excel文件），第一行为各数据属性，第一行后为各属性相应数据
# 输出文件格式：csv文件（excel文件），每三行为一组，每组数据由“数据属性名称、数据名称、数据出现次数”
# 已给出示例数据（出自2020年大学生数学建模美赛）
f = csv.reader(open('A.csv', 'r', encoding='UTF-8'))
f0 = open("A-plus-1.csv", "w", encoding='UTF-8')
writer = csv.writer(f0)
data = []

for i in f:
    data.append(i)

length1 = len(data)
length2 = len(data[0])
li = []
name = []
number = []
for i in range(1, length2):
    f0.write(data[0][i-1])
    f0.write("\n")
    for j in range(1, length1):
        li.append(data[j][i-1])
    for k in range(0, length1-1):
        if name.count(li[k]) == 0:
            name.append(li[k])
            number.append(li.count(li[k]))
        else:
            continue
    writer.writerow(name)
    writer.writerow(number)
    li.clear()
    name.clear()
    number.clear()