import random
import os
import time

def secret_word():
    global lalinea
    randomice = open("data.txt", "r", encoding ="utf-8").read().splitlines()
    lalinea = random.choice(randomice)


def run():
    my_os = os.name
    print("Hi ! Your operative system is detected as: ...")
    time.sleep(2)
    print (" ", my_os)
    print ("")
    time.sleep(2)
    print (" Your secret word is: .. ")
    time.sleep(1)
    secret_word()
    longitud = len(lalinea)
    print ("..wait a minute..")
    time.sleep(1)
    print ("but i can assure you its a word with ", longitud, " characters ;)")
    time.sleep(1)
    print (" ok the word is : ", lalinea)
    
if __name__ == "__main__":
    run()