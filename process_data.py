import numpy as np

NUM_CAR_TYPE = 5

# 获取全部数据
train = np.loadtxt('data/train_20171215.txt',dtype='int')
train = train.tolist()

# 根据车型分类，并分开保存
sale_with_car_type = [[],[],[],[],[]]

for i in range(0, len(train)):
    car_type = train[i][2] - 1
    sale_with_car_type[car_type].append(train[i])

# 把上面的数据保存到文件中
path = 'processed_data/'

for i in range(0, NUM_CAR_TYPE):
    file_name = path + "class_" + str(i+1) + "_with_day"

    output = np.delete(sale_with_car_type[i],2,axis=1)
    np.savetxt(file_name, output, fmt='%d', delimiter='\t')

for i in range(0, NUM_CAR_TYPE):
    file_name = path + "class_" + str(i+1)

    output = np.delete(sale_with_car_type[i],2,axis=1)
    output = np.delete(output, 1, axis=1)
    np.savetxt(file_name, output, fmt='%d', delimiter='\t')

