__author__ = 'wolfram'

import numpy as np
import matplotlib.pyplot as plt
import pickle

def lin_reg(x, y):
    matrixA = np.array([[1 for i in range(0, len(x))], [j for j in x]]).transpose()
    # print(matrixA)
    b = np.dot(matrixA.transpose(), matrixA)
    b = np.linalg.inv(b)
    b = np.dot(b, matrixA.transpose())
    b = np.dot(b, y)
    ystar = np.dot(matrixA, b)
    sse = np.dot((y - ystar).transpose(), y - ystar)
    return b, sse

fig = plt.figure()

ax1 = fig.add_subplot(311)
ax1.set_title(u'dataset_1')
f = open('task2_dataset_1.txt', 'rb')
x, y = pickle.load(f, encoding='ISO-8859-1')
ax1.scatter(x, y)
b = [i for i in lin_reg(x, y)[0]]
y = [b[0] + b[1]*i for i in x]
ax1.plot(x, y)

ax2 = fig.add_subplot(312)
ax2.set_title(u'dataset_2')
f = open('task2_dataset_2.txt', 'rb')
x, y = pickle.load(f, encoding='ISO-8859-1')
ax2.scatter(x, y)
b = [i for i in lin_reg(x, y)[0]]
y = [b[0] + b[1]*i for i in x]
ax2.plot(x, y)

ax3 = fig.add_subplot(313)
ax3.set_title(u'dataset_3')
f = open('task2_dataset_3.txt', 'rb')
x, y = pickle.load(f, encoding='ISO-8859-1')
ax3.scatter(x, y)
b = [i for i in lin_reg(x, y)[0]]
y = [b[0] + b[1]*i for i in x]
ax3.plot(x, y)

plt.tight_layout(h_pad = 1)


plt.show()

print(b)