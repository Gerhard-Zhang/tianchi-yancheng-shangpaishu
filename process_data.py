import numpy as np
import pandas as pd

# 获取全部数据
train = np.loadtxt('data/train_20171215.txt',dtype='int')
train = train.tolist()

# 根据牌子分类，并分开保存
sale_with_car_type = [[],[],[],[],[]]

for i in range(0, len(train)):
    car_type = train[i][2] - 1
    sale_with_car_type[car_type].append(train[i])

print(sale_with_car_type[0])

file_wirte = open("class_1_with_day", "w")
print(type(sale_with_car_type[0]))
output = ';'.join(sale_with_car_type[0])
file_wirte.writelines(output)
file_wirte.close()