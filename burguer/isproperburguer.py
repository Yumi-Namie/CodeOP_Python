def isProperBurguer(list):
    # Condicional:Always starts and ends with bread.
    # At least one Patty 
    if list[0] != "bread" or list[-1] != "bread" or list[1] != "patty":
        return False
    # Fillings
    for i in range(1,len(list)-1):
        if list[i] == "bread":
            return False
    
    return True
    
       
print(isProperBurguer(["bread", "patty","cheese","bread", "bread"]))

        
#["bread", "patty", "cheese", "bread"] >> True
#["bread", "cheese", "patty", "bread"] >> False
