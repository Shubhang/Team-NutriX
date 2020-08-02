
import csv

#dietary restrictions
dietres = {}

#lactose intolerance
dietres["lactose intolerance"] = ["milk", "cheese", "dairy"]
        
#gluten intolerance (celiac)
dietres["celiac"] = ["gluten", "wheat"]

#diabetes
dietres["diabetes"] = ["sugar", "sucrose", "fructose"]

#high blood pressure
dietres["high blood pressure"] = ["sodium", "salt"]

#various allergens 
dietres["allergens"] = ["nuts", "soy", "egg", "fish"]

#religious/cultural restrictions
#http://www.halalrc.org/images/Research%20Material/Literature/Guide%20to%20Halal%20Foods.pdf
dietres["halah"] = ["alcohol", "pork", "bacon", "vanilla"]
dietres["kosher"] = ["pork", "rabbit", "catfish", "sturgeon", "shellfish"]

#vegetarian
dietres["vegetarian"] = ["beef", "fish", "goat", "lamb", "meatball", "pork", "poultry", "chicken", "sausage", "crab", "lobster"]

#veganism
dietres["vegan"] = dietres["vegetarian"] + dietres["lactose intolerance"] + ["egg"]

new_member = []
"""
# This code for NEW-ingredientsv1
# 8 = ingredients
# 11 = name
with open("NEW-ingredientsv1.csv",encoding="utf8") as file:
    i=0
    reader = csv.reader(file)
    for row in reader:
        if i==0:
            new = row.copy()
            new.append("Allergens")
        else:
            txt = row[8].split(",")
            allergens=[]
            for j in txt:
                tocheck = j.lower()
                for k in dietres:
                    for l in dietres[k]:
                        if(l in tocheck):
                            allergens.append(k)
                            break
            txt = ""
            length = len(allergens)
            for j in range(length):
                txt+=allergens[j]
                if j+1 != length:
                    txt+=","
            new = row.copy()
            if(txt==""):
                txt="NONE"
            new.append(txt)
        i+=1
        new_member.append(new)
        
with open('NEW-ingredientsv2.csv','w',encoding="utf8",newline='') as file:
    writer = csv.writer(file)
    for i in new_member:
        writer.writerow(i)
"""
#This code below is for NEW-data_recipe.csv
with open("NEW-data_recipe.csv",encoding="utf8") as file:
    i=0
    reader = csv.reader(file)
    for row in reader:
        if i==0:
            new = row.copy()
            new.append("Allergens")
        else:
            txt = row[2].split(",")
            allergens=[]
            for j in txt:
                tocheck =j.lower()
                for k in dietres:
                    for l in dietres[k]:
                        if(l in tocheck):
                            allergens.append(k)
                            break
            txt =""
            length = len(allergens)
            for j in range(length):
                txt += allergens[j]
                if j+1 != length:
                    txt += ","
            new = row.copy()
            if(txt ==""):
                txt = "NONE"
            new.append(txt)
        i+=1
        new_member.append(new)

with open("NEW-data_recipev2.csv",'w',encoding="utf8",newline="") as file:
    writer = csv.writer(file)
    for i in new_member:
        writer.writerow(i)