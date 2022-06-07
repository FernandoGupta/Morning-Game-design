# Fernando Gupta
# create a word guess agme with 10 words
# pseudocode: get one word from a list of animals provide instructions to user, one hint about the words in the list and the amount of words in the list, get guess. If correct congratulate. if not say you missed. if missed provide another hint. if correct congatulate if inncorect say, man wrong again and then provide third hint, if correct congatulate, if innocorect say you missed again, you are really bad at this, stop providing hits and give user unlimited guesses till correct 

from ctypes.wintypes import WORD
import random
import os 

os.system ('cls')
from time import sleep
seconds=.5



list1 = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
list2 = ["mango", "papaya", "orange","mandarin","clemintine","nectarine","bannana"]
list3 = ["motherboard","CPU","GPU","RAM","SSD","HDD","ROM"]
Game=True 
cnt=0
# a function is a section of the program that we call when we need it 
def hint():
    global cnt  #allows us to modify the variable all over the program 
    if cnt ==0:
        print("|*************************************|")
        print("|         Here is a new hint          |")
        print("|These creatures all have a hard shell|")
        print("|*************************************|")
     
    # guess2 = input("plese put your new guess here: ")
    # if guess2 == theword:
    #     print("Congrats, You got it")
    # else:
    #     print("wrong again, you are pretty bad at this, try again")
    elif cnt ==1:    
        print("|**************************************|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|**************************************|")
    elif cnt ==6:
        print("this fruit is normaly on the sweeter side")
    elif cnt ==7:
        print("wrong,this fruit is typicaly very popular")
    elif cnt ==12:
        print("these components are all inside the computer")
    elif cnt ==13:
        print("wrong,these components are all very nescescary for the computer to run")
    else:
        print("wrong, no more hints, go till you get it right")
    
def selectWrd(choice): #this is a function 
    global theword 
    if choice ==1:
        theword= random.choice(list1) 
        return 
    if choice ==2:
        theword= random.choice(list2)
    if choice ==3:
        theword= random.choice(list3)
name=input("What is your name? ")
high=0 #to find the highest score 
while Game:
    print("|***************************************|")
    print("|         Guess The Thing!!!            |")
    print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
    print("|          1.animals                    |")
    print("|          2.Fruits                     |")
    print("|          3.Computer parts             |")
    print("|First we will provide you with one hint|")
    print("|***************************************|")
# user name make more persoal and will be used to keep score    
    name=input('what is your name: ')
    print(name, end=" ")
    answer=input("would you like to  play " )
    if 'n' in answer:
        break
    while True:
        choice=input ("what game would you like to play 1, 2, or 3 ")
        # preventing error we use try and except 
        try:
            choice=int(choice)
            if choice>0 and choice<4: 
                break
            else:
                 print("give me 1, 2, or 3 ")
        except:
            print("sorry")
    #call function to select the word from the right lists 
    os.system('cls')
    cnt=0
    print("you chose animals, your hint is this animal loves the water")
    check=True 
    while check and cnt <5 :
        guess=input("plese put your guess here: ")
        print()
        if guess == theword:
            print("Congrats, You got it")
            check=False 
        else:
            hint()
        cnt+=1
    os.system('cls') 
    cnt=6
    print("you chose fruits, your hint is these fruits are very orange")
    while check and cnt>5 and cnt<11 and choice == 2:
        guess=input("plese put your guess here: ")
        print()
        if guess == theword:
            print("Congrats, You got it")
            check=False 
        else:
            hint()
        cnt+=1   
    os.system('cls')
    cnt=12
    if choice == 3:
         print("you chose computer parts, your hint is, these components are all conected")
    while check and cnt>11 and cnt<17 and choice == 3:
        guess=input("plese put your guess here: ")
        print()
        if guess == theword:
            print("Congrats, You got it")
            check=False 
        else:
            hint()
        cnt+=1      
    print('<><><><><><><><><><><><>')
    answer=input("do you want to play again: ")
    if ('n'or 'N') in answer:
        Game=False 
        print("Thank you for playing my game! ")


