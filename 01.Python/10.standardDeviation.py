# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:25:40 2016

@author: rmatam
"""

import numpy as np
from scipy import stats
 A = np.array([[10,14,11,7,9.5,15,19],[8,9,17,14.5,12,18,15.5],
               [15,7.5,11.5,10,10.5,7,11],[11.5,11,9,12,14,12,7.5]])
 B = A.T
 print B
 #a=np.median(B,axis=0)
 a=np.std(B,axis=0)
 b=np.std(B,axis=1)

 print(a,b)