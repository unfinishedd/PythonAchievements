import os

isRunning = True
antwoord = ""

playerSprite = "@"

positiveX = 0


print("Press ENTER to start the game.")

while ( isRunning == True ) :

    # REGISTREER INPUT:
    antwoord = input()

    #UPDATE DE GAME:
    if (antwoord == "quit"):
        isRunning = False
        break;

    if (antwoord == "rechts"):
        positiveX += 1
    elif(antwoord == "links"):
        positiveX -= 1

    os.system("cls")

    # TEKEN DE HUIDIGE STAAT VAN DATA:
    for x in range(positiveX):
        print(" ", end="")
    else:
        print(playerSprite)

    print("-----------------------------------------------------------")
    
