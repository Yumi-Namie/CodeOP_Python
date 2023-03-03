def maximumGuests(wboard, wlegs):
    """Return the number of people that will be able to sit around the tables,
    once the furniture is assembled. For someone to be able to sit around a table,
    there has to be a chair for them to sit on, and a space in the table for them to sit in front of.
    Here's what you need to know about the furniture:

    To assemble a table, you will need four wooden boards and four wooden legs.
    Each table is big enough to seat four people around them.
    To assemble a chair, you will need one wooden board and three wooden legs.
    Each chair can sit one person, provided there's space for them in a table."""
    
    totalboards = wboard
    totallegs = wlegs
    totalmesa = 0
    totalsilla = 0
    totalguests = 0
    
    #At least one guest: one table and one chair
    if totalboards >=5 and totallegs>=7:
        #table: boards and legs enough
        while totalboards >=4 and totallegs>=4:
            #Table
            totalboards = totalboards -4
            totallegs = totallegs -4
            totalmesa +=1
            
            #Chair
            while totalsilla < totalmesa*4:
                if totalboards >=1 and totallegs >=3:
                    totalboards = totalboards -1 
                    totallegs= totallegs-3
                    totalsilla +=1
                else:
                    break
            totalguests = totalsilla
                          
    return totalguests 

print(maximumGuests(0,0))
print(maximumGuests(6,10))
print(maximumGuests(8,32))
print(maximumGuests(10,32))
print(maximumGuests(32,32))

                
        
                
                
            
            
        
    
    
    

