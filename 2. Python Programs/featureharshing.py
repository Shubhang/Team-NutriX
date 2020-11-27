# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 00:23:18 2020

@author: Pluem
"""

from sklearn.feature_extraction import FeatureHasher
from pandas import read_csv
import csv

dataset = read_csv("data/NEW-data_recipe.csv")
#create dictionary
array = dataset.values
name= array[:,1]
ingredients = array[:,2]
D={}
length=len(name)
for i in range(length):
    D[name[i]]=ingredients[i]
h = FeatureHasher(n_features=10,input_type="string")
f = h.transform(D)
f.toarray()
print(type(f))