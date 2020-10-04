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

# https://www.fda.gov/food/buy-store-serve-safe-food/what-you-need-know-about-food-allergies
#https://www.betterhealth.vic.gov.au/health/ConditionsAndTreatments/nut-allergies 
# peanuts, tree nuts