import os
import time

factory = ["Playstation 5", "PS3", "PS4"]
distribution = []
shop = []

def factory_to_distribution():
    distribution.append(factory.pop())
    


def distribution_to_shop():
    shop.extend(distribution)
    distribution.pop(0)

def printlist():
        print("factory = " + str(factory))
        print("distribution = "+ str(distribution))
        print("shop = "+ str(shop))
    
def nextprint():
    time.sleep(2.1)
    os.system('cls')

printlist()
factory_to_distribution()
nextprint()
printlist()
distribution_to_shop()
nextprint()
printlist()
