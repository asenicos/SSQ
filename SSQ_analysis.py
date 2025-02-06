# -*- coding: utf-8 -*-

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#read SSQ results
exp='ssq_example.csv'
path='d:\\my_scripts\\py'
os.chdir(path)
df=pd.read_csv(exp, sep=";", index_col=0, header=None)


def calculate_total_ssq(df,d):
    #SSQ defined by Kennedy et al., 1993
    n_columns = [0, 5, 6, 7, 8, 14, 15]
    o_columns = [0, 1, 2, 3, 4, 8, 10]
    d_columns = [4, 7, 9, 10, 11, 12, 13]

    # Calculate sum for each specified set of columns
    n_val = df.iloc[n_columns, d].sum()
    o_val = df.iloc[o_columns, d].sum()
    d_val = df.iloc[d_columns, d].sum()

    return n_val, o_val, d_val
 
xaxis=[]
dyn=[]
for j in range(len(df.columns)):
    n_val,o_val,d_val = calculate_total_ssq(df, j)
    total_ssq = (n_val+o_val+d_val) * 3.74
    n=n_val*9.54
    o=o_val*7.58
    d=d_val*13.92
    print("day ",j,": total ssq=",total_ssq)
    dyn.append(total_ssq)
    xaxis.append(j+1)
plt.plot(xaxis,dyn)    
plt.xticks(xaxis)
