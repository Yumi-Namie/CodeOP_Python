def makeBravas(list):
    
    """ Recive a list of sizes of portions and Return the amount of portions to make bravas

    A small potato can only be chopped into 4 potato chips.
    A medium potato can be chopped into 8 potato chips.
    A large potato can be chopped into 24 potato chips!
    To make a portion of patatas bravas, you need 20 potato chips."""
    
    portion = 0
    totalportion = 0
    
    for size in list:
        if size == "small":
            portion +=4
        if size == "medium":
            portion +=8
        if size == "large":
            portion+= 24
        totalportion = int(portion/20)
    return totalportion

print("large: ", makeBravas(["large"]), "portion")
print("2larges,1md,1sm: ", makeBravas(["large", "large", "medium", "small"]), "portion")
print("5 larges:", makeBravas(["large", "large", "large", "large", "large"]), "portions")

    
    


    
    
    
    
