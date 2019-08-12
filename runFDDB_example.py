#!/usr/bin/env python
# coding: utf-8

# In[1]:


# use
from FDDB import runFDDB
runFDDB(pred='./FDDB-result/result.txt', result_path=None, index=-1)


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
import numpy as np

path_ContROC = "./FDDB-result/ContROC.txt"
path_DiscROC = "./FDDB-result/DiscROC.txt"
path_imgSave = "./FDDB-result/result.png"

set_x_lim = 1000

# get data
with open(path_DiscROC, 'r') as fp:
    discROC = fp.readlines()

# get disc data x, y
discROC = [line.split() for line in discROC]
disc_x = [float(x[1]) for x in discROC]
disc_y = [float(y[0]) for y in discROC]

# get data we need to be print
count = len(discROC)

### plot data
plt.figure()

# set y limite
plt.ylim((-0.07,1))
# plt.xlim((-2,set_x_lim))
# print label
plt.xlabel('False Positive (FP)')
plt.ylabel('True Positive Rate (FPR)')

# plot data
plt.plot(disc_x,disc_y,color = '#007777', linewidth = 3.0)

# print data text
plt.title('MTCNN-Tensorflow')
plt.text(disc_x[0] - disc_x[0] / 3,disc_y[0] + 0.03,'Discrete Score: %.3f' %(disc_y[0] * 100) + '%')

# 
plt.grid()

# save img
# plt.figure(figsize=(10, 10))
plt.savefig('./FDDB-result/result.png')
plt.show()

