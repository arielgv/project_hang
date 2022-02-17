import random 
import os
import time


def run():
    os.system("cls")
    
    print(" .........................  ")
    print(" Please hold, loading the word.. ")
    time.sleep(2)
    randomice = open("data.txt", "r", encoding ="utf-8").read().splitlines()
    lalinea = random.choice(randomice)
    longitud = len(lalinea)
    print (" Ready ! your word has been picked ! it has ", longitud, " letters ;)")
    time.sleep(1)
    print( " Lets Begin! ")
    time.sleep(2)
    subrayado = "_ "
    subrayado = subrayado * longitud
    print (subrayado)
    


    

if __name__ == "__main__":
    run()