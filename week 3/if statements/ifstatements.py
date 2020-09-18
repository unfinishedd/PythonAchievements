
varA = 5
varB = 10
if ( varA == 5 ):
    print("varA staat gelijk aan 5")
else : 
    print("varA staat niet gelijk aan 5")


if ( varA == varB ) :
    print("varA staat gelijk aan var B")
elif ( varA < varB ) :
    print("varA is kleiner dan varB")
elif ( varA == 50 ) :
    pass #Doe niks
else :
    print("Dan is varA groter dan varB")


if ( False ):
    print("Doe dit")

varW = False
varX = True
varY = True
varZ = True

#  ( varW == True and varX == True or varY == True and varZ == True )
#  ( (varW and varX) or (varY and varZ) )
if ( varW and varX or varY and varZ ):
    print("Print dit!")

#  ( False and (True or True) and  True
#  ( False  and    True      and  True
if ( varW and (varX or varY) and varZ ):
    print("Print mij ook!")

print("Einde programma")
