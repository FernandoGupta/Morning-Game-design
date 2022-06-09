# Fernando Gupta
# create a word guess agme with 10 words
# pseudocode: get one word from a list of animals provide instructions to user, one hint about the words in the list and the amount of words in the list, get guess. If correct congratulate. if not say you missed. if missed provide another hint. if correct congatulate if inncorect say, man wrong again and then provide third hint, if correct congatulate, if innocorect say you missed again, you are really bad at this, stop providing hits and give user unlimited guesses till correct 

from ctypes.wintypes import WORD
import random
import os 

os.system ('cls')
from time import sleep
seconds=.5



list = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
theword=random.choice(list)
Game=True 
cnt=0
# a function is a section of the program that we call when we need it 
def hint():
    global cnt  #allows us to modify the variable all over the program 
    if cnt ==0:
        print("|*************************************|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|        only 2 shells in fact        |")
        print("|*************************************|")
     
    # guess2 = input("plese put your new guess here: ")
    # if guess2 == theword:
    #     print("Congrats, You got it")
    # else:
    #     print("wrong again, you are pretty bad at this, try again")
    elif cnt == 1:    
        print("|**************************************|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|**************************************|")
    else:
        print("You are horrible at guessing, no more hints, go till you get it right")
    cnt+=1 # cnt= cnt + 1

while Game:
    print("|***************************************|")
    print("|         Guess The Animal!!!           |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("|          1.Instructions               |")
    print("|   There are 10 animals in this game   |")
    print("|     You must guess one of them        |")
    print("|First we will provide you with one hint|")
    print("|           !Your Hint Is!              |")
    print("|  These animals are big fans of water  |")
    print("|***************************************|")
# user name make more persoal and will be used to keep score    
    name=input('what is your name: ')
    print(name, end=" ")
    answer=input("would you like to  play " )
    if 'n' in answer:
        break
    os.system('cls')
    check=True 
    while check and cnt <5:
        guess=input("plese put your guess here: ")
        print()
        if guess == theword:
            print("Congrats, You got it")
            check=False 
        else:
            hint()
        cnt+=1
    os.system('cls')
    print('<><><><><><><><><><><><>')
    answer=input("do you want to play again")
    if ('n'or 'N') in answer:
        Game=False 
        print("Thank you for playing my game")


