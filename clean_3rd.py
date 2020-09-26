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
with open("data/third_datasetcombined.csv",encoding="utf8") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
        if(i==0):
            new = row.copy()
            new_member.append(new)
            i+=1
            continue
        new = row.copy()
        lis = row[2].split("'")
        string = ""
        for j in lis:
            if(j!=", " and j != "[" and j!="]"):
                dummy_str = j.replace("\"","").replace("ADVERTISEMENT","")   
                if(dummy_str==""):
                    continue
                if(string!=""):
                    string+=","
                res=""
                for k in dummy_str:
                    if(k==','):
                        continue
                    res +=k
                string=string+res
        new[2]=string
        new_member.append(new)
           
with open('data/New_3rd_data.csv','w',encoding="utf8",newline='') as file:
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