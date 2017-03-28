# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:22:40 2017

@author: rmatam
"""

import numpy as np
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(sum(map(ord,"aesthetics")))

def sinplot(flip=1):
    x=np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)

sinplot()