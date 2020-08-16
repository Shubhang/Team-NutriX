# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 16:18:05 2020

@author: Pluem
"""
from pandas import read_csv
import pandas as pd
import csv
new_member=[]
#This part for NEW-ingredientsv1 dataset
with open("data/NEW-ingredientsv1.csv",encoding="utf8") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
       if(i==0):
           new = row.copy()
       else:
           if(row[15]!='NONE'):
               new = row.copy()
           else:
               i+=1
               continue
       new_member.append(new)
       i+=1
           
with open('NEW-ingredientsv1-none-removed.csv','w',encoding="utf8",newline='') as file:
    writer = csv.writer(file)
    for i in new_member:
        writer.writerow(i)
"""
#This part for NEW-data_recipe.csv
with open("data/NEW-data_recipe.csv",encoding="utf8") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
       if(i==0):
           new = row.copy()
       else:
           if(row[3]!='NONE'):
               new = row.copy()
           else:
               i+=1
               continue
       new_member.append(new)
       i+=1
            
with open('NEW-data_recipe-none-removed.csv','w',encoding="utf8",newline='') as file:
    writer = csv.writer(file)
    for i in new_member:
        writer.writerow(i)
"""