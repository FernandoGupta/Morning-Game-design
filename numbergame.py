# Fernando Guota
# Number Guessing game
    # pseudocode. make menu, give option to input number for each option in menu.
    # each will be guided by a function, ex: if choice == 1 print rules or smthn like that
    # for the actual game make lists of numbers and have function to bring player to it, let the player have 25 guesses max(thats is a lot may chaneg later)
    # for soreboard, make file and desplay that when they go to view score, will do top 10 high score displayed
    # to exit game will program so when input 6 code simply stops running 
#steps: 1.instructions 2.level1 num 1-25 3.level2 num 1-50 4.level3 num 1-100 5.prt score 6.exit



from ast import Num
from itertools import count
import random
import os, datetime
import os
date=datetime.datetime.now()




os.system('cls')
        


Game=True
cnt=0
high=0
name=input("What is your name? ")
def Menu(choice):
    if choice ==1:
        print("In this game your goal is to guess a number. There are 3 different lvls, numbers 1-25, 1-50 and 1-100")
        print("you have 5 guesses")
        input("press enter to return to menu")
    global num
    global high
    global cscore
    bcnt=0
    if choice ==2:
        num = random.randint(1,25)+1
        bcnt=+1
    if choice ==3:
        num = random.randint(1,50)+1
        bcnt=+1
    if choice ==4:
        num = random.randint(1,100)+1
        bcnt=+1
    if choice ==5:
        f=open("scores.txt","r+")
        numbers = sorted(list(map(int, f.readlines())))
        print (numbers[5:])
    if choice ==6:
        print("thanks for playing, your total score is " + str(score))
        input("press enter to play again")

        
        
myFile=open("scores.txt",'a') #this opens the file to write 
myFile.write (str(high) + "\t"+name+"\t"+ date.strftime("%m/%d/%Y")) 
myFile.close()




high=0


while Game:
    print("|****************************************|")
    print("|         NUMBER GUESSING GAME           |")
    print("|            1.Instructions              |")
    print("|              2.Level 1                 |")
    print("|              3.Level 2                 |")
    print("|              4.Level 3                 |")
    print("|            5.Score Board               |")
    print("|                6.EXIT                  |")
    print("|****************************************|")

    print(name, end=", ")
    choice= input("what would you like to do. imput number here: ")
    choice=int(choice)
    choice = Menu(choice)



    check=True
    while check and cnt <5:
        guess=input("plese put your guess here: ")
        print()
        if guess == num:
            print("Congrats, You got it")
            check=False
        cnt+=1   
        if cnt ==5:
            print("sorry! Thats the max guesses")
            input("press enter to return to menu")
        cscore=2000-cnt*100
        score=cscore+bcnt*200
        if score > high:
            high=score  
    
myFile=open("scores.txt",'a') #this opens the file to write 
myFile.write (str(high) + "\t"+name+"\t"+ date.strftime("%m/%d/%Y")) 
myFile.close()
myFile = open("scores.txt",'r')
stuff=myFile.readlines()
sorted= stuff.sort(reverse=True)
myFile.close()
for line in sorted:
    print (line)