# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
dict={"Country":["Brazil","Russia","China","India","South Africa"],"Capital":["Brasilia","Maskow","Bejing","India","Pretoria"],"Area":[8.56,10.12,15.16,123.3,12.0],"Population":[200,123,1762,1356,234]}
#print dict
import pandas as pd
bricks=pd.DataFrame(dict)
print bricks
