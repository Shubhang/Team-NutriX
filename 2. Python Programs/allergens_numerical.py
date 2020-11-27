# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:29:49 2020

@author: Pluem
"""
import csv
"""
#This code is for NEW-data_recipe
new_member=[]
with open("data/NEW-data_recipe.csv",encoding="utf8") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
        new = row.copy()
        if(i==0):
            new.append("Numerical allergen")
        else:
            if(row[3]=="NONE"):
                new.append("0")
            else:
                new.append("1")
        i+=1
        new_member.append(new)
        
with open("data/NEW-data_recipe.csv",'w',encoding="utf8",newline='') as file:
    writer = csv.writer(file)
    for i in new_member:
        writer.writerow(i)
"""
# This code is for NEW-ingredientsv1
new_member=[]
with open("data/NEW-ingredientsv1.csv",encoding="utf8") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
        new = row.copy()
        if(i==0):
            new.append("Numerical allergen")
        else:
            if(row[15]=="NONE"):
                new.append("0")
            else:
                new.append("1")
        i+=1
        new_member.append(new)

with open("data/NEW-ingredientsv1.csv",'w',encoding="utf8",newline='') as file:
    writer = csv.writer(file)
    for i in new_member:
        writer.writerow(i)