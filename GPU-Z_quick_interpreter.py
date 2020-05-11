# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:09:09 2020

@author: denis
"""

import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# data = input('Please give the file name you wish to use: ')
# data = 'GPUZSensorLog2.txt' # development data set
file_name = input('Please give the file name you wish to use: ')
workload = input('Please outline use case: ')


f = open(file_name + '.txt','r+')
data = f.read()
# data.encode('utf-8').strip()
# f.write(data)


d3 = data.encode("ascii", "ignore")
data2 = d3.decode()

f2 = open('work.txt','w')
f2.write(data2)
f2.close()

df = pd.read_csv('work.txt')
# sb.lineplot(df.index,df[])
# sb.lineplot(df.index,[df[' GPU Temperature [C] '],df[' CPU Temperature [C] ']])
df[[' GPU Temperature [C] ',' CPU Temperature [C] ']].plot()
plt.ylabel('Hardware temperature')
plt.title(f'{workload}')
plt.legend()
sb.jointplot(df[' GPU Temperature [C] '],df[' CPU Temperature [C] '],kind='hex')
sb.jointplot(df[' GPU Load [%] '],df[' GPU Temperature [C] '],kind='hex')
sb.jointplot(df[' GPU Load [%] '],df[' Power Consumption (W) [W] '],kind='hex')
