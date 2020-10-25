# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:12:12 2020

@author: Pluem
"""
import pandas as pd
#dietary restrictions
dietres = {}



#lactose intolerance 1
dietres["lactose intolerance"] = ["milk", "cheese", "dairy"]

#gluten intolerance (celiac) 1
dietres["celiac"] = ["gluten", "wheat"]

#soybean allergy
dietres["soy"] = ["soybean", "soy"]

#fish allergy 
dietres["seafood and fish"] = ["crab", "shrimp", "lobster", "crawfish", "salmon", "cod", "trout", "tuna","fish" , "tilapia", "anchovie", "barracuda", "basa", "bass", "black cod", "blowfish","brill", "catfish", "eel", "flounder", "haddock", "hake", "halibut", "herring", "mackerel", "monkfish", "mullet", "pollock", "sardine", "sea bass", "shad", "swordfish", "trout", "whitefish", "caviar", "crayfish", "clam", "mussel", "octopus", "oyster", "periwinkle", "scallop", "squid", "conch" ]

#diabetes 1
dietres["diabetes"] = ["sugar", "sucrose", "fructose"]

#high blood pressure 1
dietres["high blood pressure"] = ["sodium", "salt","sugar"]

#treenuts 
dietres["treenut"] = ["filbert", "hazelnut", "almond", "brazil nut", "chestnut", "hickory", "macadamia", "pecan", "pine" , "pistachio" , "walnut"]

#nuts
dietres["nut"]= dietres["treenut"] + ["peanut", "yeheb", "beech", "oak", "cashew"]
#various allergens  1
dietres["allergens"] = ["nuts",  "egg"]

#religious/cultural restrictions 1
#http://www.halalrc.org/images/Research%20Material/Literature/Guide%20to%20Halal%20Foods.pdf
dietres["halah"] = ["alcohol", "pork", "bacon", "vanilla"]
dietres["kosher"] = ["pork", "rabbit", "catfish", "sturgeon", "shellfish"]

#vegetarian 1
dietres["vegetarian"] = ["beef", "goat", "lamb", "meatball", "pork", "poultry", "chicken", "sausage","meat"]+dietres["seafood and fish"]

#veganism 1
dietres["vegan"] = dietres["vegetarian"] + dietres["lactose intolerance"] + ["egg"]

dataset = pd.read_json("data/recipes_with_nutritional_info.json")
allergens=[]
#print(dataset['ingredients'])
for index,row in dataset.iterrows():
    dummy_list=[]
    for i in row['ingredients']:
        txt = i['text'].split(',')
        #print(txt)
        for j in txt:
            #print(j)
            for k in dietres:
                for l in dietres[k]:
                    if(j == l and k not in dummy_list):
                        dummy_list.append(k)
    if(dummy_list==[]):
        dummy_list.append('NaN')
    allergens.append(dummy_list)

dataset['allergens']=allergens
dataset.to_json("data/dummy.json",orient='records')
        