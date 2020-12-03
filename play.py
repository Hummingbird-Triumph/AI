# -*- codeing = utf-8 -*-
# @Time : 2020/12/2 9:06
# @Author : 张凯峰
# @File :play.py
# @Software: PyCharm

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import onehot

data = onehot.load_data()
new_data = onehot.convert2onehot(data)


# prepare training data
new_data = new_data.values.astype(np.float32)       # change to numpy array and float32
np.random.shuffle(new_data)
sep = int(0.7*len(new_data))
train_data = new_data[:sep]                         # training data (70%)
test_data = new_data[sep:]
