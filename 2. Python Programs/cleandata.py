# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 22:16:54 2020

@author: Pluem
"""

import numpy as np
import csv
import string
with np.load('data/simplified-recipes-1M.npz') as data:
    #recipes = data['recipes']
    ingredients = data['ingredients']
    
#clean ingredients v1
new_file=[]
with open("data/ingredients v1.csv",encoding="utf8") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
        new = row.copy()
        if(i==0):
            new[15]="cleaned_ingredients"
        else:
            text=""
            check_text = row[8].lower().split(',')
            fin = []
            for z in check_text:
                dummy = z.split(' ')
                for j in dummy:
                    fin.append(j)
            for k in fin:
                tocheck = k.translate(str.maketrans('','',string.punctuation))
                for j in ingredients:
                    if(j=="fl" or j=="s" or j=="st" or j=="m" or j=="a"):
                        continue
                    if(j == tocheck):
                        if(text!=""):
                            text+=','
                        text+=j
            new[15]=text
        i+=1
        new_file.append(new)

with open('cleaned_ingredientsv1.csv','w',encoding="utf8",newline='') as file:
    writer = csv.writer(file)
    for i in new_file:
        writer.writerow(i)
