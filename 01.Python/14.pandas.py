# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:59:06 2017

@author: rmatam
"""
import numpy as np
import pandas as pd
import os
import seaborn as sns

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])


s2=pd.Series(np.random.randn(10),index=['a','ab','abc','abcd','abcde','ax','axb','axbc','arbcd','z'])
s2

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
   'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
d
df=pd.DataFrame(d)
df1=pd.DataFrame(d,index=['b','c'])
df1


poc_train = pd.read_csv('E:\\python\\CSC_POC\\csc_poc_train.csv')
poc_train
poc_train_dataFrame=pd.DataFrame(poc_train)
poc_train_dataFrame.head()
poc_train_dataFrame.shape()
poc_train_dataFrame.info()
poc_train_dataFrame.describe()
poc_train_dataFrame['REASON ISCSCMANAGED']=poc_train_dataFrame['REASON ISCSCMANAGED'].astype('category')
poc_train_dataFrame.describe()
sns.boxplot(x= poc_train_dataFrame['ACCOUNT_NAME'],x= poc_train_dataFrame['ACCOUNT_NAME'],data=poc_train_dataFrame)
