
import csv

#dietary restrictions
dietres = {}



#lactose intolerance
dietres["lactose intolerance"] = ["milk", "cheese", "dairy"]

#gluten intolerance (celiac)
dietres["celiac"] = ["gluten", "wheat"]

#soybean allergy
dietres["soy"] = ["soybean", "soy"]

#fish allergy 
dietres["seafood and fish"] = ["crab", "shrimp", "lobster", "crawfish", "salmon", "cod", "trout", "tuna","fish" , "tilapia", "anchovie", "barracuda", "basa", "bass", "black cod", "blowfish","brill", "catfish", "eel", "flounder", "haddock", "hake", "halibut", "herring", "mackerel", "monkfish", "mullet", "pollock", "sardine", "sea bass", "shad", "swordfish", "trout", "whitefish", "caviar", "crayfish", "clam", "mussel", "octopus", "oyster", "periwinkle", "scallop", "squid", "conch" ]

#diabetes
dietres["diabetes"] = ["sugar", "sucrose", "fructose"]

#high blood pressure
dietres["high blood pressure"] = ["sodium", "salt","sugar"]

#treenuts 
dietres["treenut"] = ["filbert", "hazelnut", "almond", "brazil nut", "chestnut", "hickory", "macadamia", "pecan", "pine" , "pistachio" , "walnut"]

#nuts
dietres["nut"]= dietres["treenut"] + ["peanut", "yeheb", "beech", "oak", "cashew"]
#various allergens 
dietres["allergens"] = ["nuts",  "egg"]

#religious/cultural restrictions
#http://www.halalrc.org/images/Research%20Material/Literature/Guide%20to%20Halal%20Foods.pdf
dietres["halah"] = ["alcohol", "pork", "bacon", "vanilla"]
dietres["kosher"] = ["pork", "rabbit", "catfish", "sturgeon", "shellfish"]

#vegetarian
dietres["vegetarian"] = ["beef", "goat", "lamb", "meatball", "pork", "poultry", "chicken", "sausage","meat"]+dietres["seafood and fish"]

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
with open("data/New_3rd_data.csv",encoding="utf8") as file:
    i=0
    reader = csv.reader(file)
    for row in reader:
        if i==0:
            new = row.copy()
            #new.append("txt")
            new_member.append(new)
            i+=1
            continue
        else:
            txt = row[2].split(",")
            allergens=[]
            back=[]
            for j in txt:
                tocheck = j.lower().split()
                for k in dietres:
                    for l in dietres[k]:
                        for p in tocheck:    
                            if(l == p and k not in allergens):
                                #back.append(l)
                                #back.append(tocheck)
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
            new[5]=txt
            #new.append(back)
        i+=1
        new_member.append(new)

with open("data/New_3rd_datav2.csv",'w',encoding="utf8",newline="") as file:
    writer = csv.writer(file)
    for i in new_member:
        writer.writerow(i)