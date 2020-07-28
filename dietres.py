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