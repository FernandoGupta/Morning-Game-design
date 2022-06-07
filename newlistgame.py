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
list2 = ["mango", "papaya", "orange","mandarin","clemintine","peach","apricot","nectarine","kumquat","bannana"]
list3 = ["motherboard","CPU","GPU","RAM","SSD","HDD","ROM"]
theword1=random.choice(list1)
theword2=random.choice(list2)
theword3=random.choice(list3)
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
    if cnt ==1:    
        print("|**************************************|")
        print("|       Here is your final hint        |")
        print("|  These creatures almost never move   |")
        print("|**************************************|")
    if cnt ==2:
        print("wrong, no more hints, go till you get it right")
    if cnt ==3:
        print("wrong, no more hints, go till you get it right")
    if cnt ==4:
        print("wrong, no more hints, go till you get it right")
    if cnt ==5:
        print("wrong, no more hints, go till you get it right")
    if cnt ==6:
        print("this fruit is normaly on the sweeter side")
    elif cnt ==7:
        print("this fruit is typicaly very popular")
    if cnt ==8:
        print("wrong, no more hints, go till you get it right")
    if cnt ==9:
        print("wrong, no more hints, go till you get it right")
    if cnt ==10:
        print("wrong, no more hints, go till you get it right")
    if cnt ==11:
        print("wrong, no more hints, go till you get it right")
    if cnt ==12:
        print("these components are all inside the computer")
    if cnt ==13:
        print("these components are all very nescescary for the computer to run")
    if cnt ==14:
        print("wrong, no more hints, go till you get it right")
    if cnt ==15:
        print("wrong, no more hints, go till you get it right")
    if cnt ==16:
        print("wrong, no more hints, go till you get it right")

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
    print("this animal loves the water")
    check=True 
    while check and cnt <5 and choice == 1:
        guess=input("plese put your guess here: ")
        print()
        if guess == theword1:
            print("Congrats, You got it")
            check=False 
        else:
            hint()
        cnt+=1
    os.system('cls') 
    cnt=6
    print("these fruits are very orange")
    while check and cnt>5 and cnt<11 and choice == 2:
        guess=input("plese put your guess here: ")
        print()
        if guess == theword2:
            print("Congrats, You got it")
            check=False 
        else:
            hint()
        cnt+=1   
    os.system('cls')
    cnt=12
    print("these components are all conected")
    while check and cnt>11 and cnt<17 and choice == 3:
        guess=input("plese put your guess here: ")
        print()
        if guess == theword3:
            print("Congrats, You got it")
            check=False 
        else:
            hint()
        cnt+=1      
    print('<><><><><><><><><><><><>')
    answer=input("do you want to play again")
    if ('n'or 'N') in answer:
        Game=False 
        print("Thank you for playing my game")


