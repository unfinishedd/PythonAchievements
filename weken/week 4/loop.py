
import random

isRunning = True

while ( isRunning ) :

    print("HERHAAL DIT!")

    num = random.randrange(5)
    if (num == 4) :
        isRunning = False

else:

    print("Einde eerste while-loop")


lijstA = ["kaas", 11, True, '#', 4.22, "nog wat meer kaas"]
lijstB = ["Dit", "is", "een", "lijst", "van", "tekst"]

print( lijstA )
print( lijstA[1] )

lijstA[1] = 23
print( lijstA )

print("-----------------------------------------------------------")

for waarde in lijstA :
    print("Dit is waarde:", waarde)
else: #Dit is optioneel
    print("klaar met de for loop")

print("-----------------------------------------------------------")


print( lijstB )

for waarde in lijstB :
    waarde = "leuk"
    print(waarde)

print( lijstB )

print("-----------------------------------------------------------")

print( "Lengte van lijstB is:", len(lijstB) )

for getal in range(5) :
    print("Herhaal dit 5 keer, dit is een iteratie:", getal)

print("-----------------------------------------------------------")


print( lijstB )

range(2, 10 , 2)
resultaat = range( len( lijstB ) )
print( resultaat )

#            range(     6         )
for index in range( len( lijstB ) )
    print( "Dit is index", index, "wat waarde", lijstB[index], "is" )

    if ( lijstB[index] == "een" ):
        lijstB[index] = "VERANDERD!"

print( lijstB )        
        
print("-----------------------------------------------------------")

# Continue gaat verder met de volgende iteratie.
for waarde in lijstB :
    if (waarde == "VERANDERD"):
        continue;

    print(waarde)

print("-----------------------------------------------------------")

# Break stopt de loop volledig


