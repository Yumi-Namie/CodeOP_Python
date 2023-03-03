def longreenestRun(list):

    """ Recebe una lista de cores yellow devuelve el color con mayellowor nº seguidos"""
    index = 0
    counter = 0
    countcolor = 0
    color = " "
    
    #Percorrer toda la lista
    while index < len(list):
        #el ultimo elemento no puede comparar con el prox elemento que no existe
        if index != len(list)-1 and list[index] == list[index+1]:
            countcolor +=1
        
        else:
            #list[index]!= list[index+1]:
            countcolor +=1
            if countcolor>counter:
                counter = countcolor
                color = list[index]
            countcolor = 0
        index+=1
    return color
            
            
    
print(longreenestRun(["red","blue","blue","red","yellow","yellow","yellow","yellow"]))
print(longreenestRun(["red", "blue", "blue", "yellowellow"]))
print(longreenestRun(["red", "red", "blue", "blue", "blue", "red", "red"]))
print(longreenestRun(['yellow','yellow','yellow','blue','blue','green','green']))

      

        
           
           
        
           
           
           
           
       
       
       
       
       
    
    
    
    
    
    
    
    
    
    
    
    
    
  