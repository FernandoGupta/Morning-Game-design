# fernando gupta
#How to find grid:
#Using for loop, to find grid section it would be the width/3*2 
#To represent the gird we create 3 lists 
#X=1
#O=-1
#To change player in the loop mult by -1 
#How to check if someone wins:
#If a row or collum is = to 3 or -3 someone has one, so you must add all the rows and add all teh column before continuing on with the game
#If = 3 then X won, if -3 then O won 
#ALSO: when checking for winning, you must create a check that looks if cell (0,0) (1,1) (2,2) have teh same values or if position (0,2) (1,1) and (3,1) have teh same values, -1 or 1
#functions: draw_grid() and zero_grid() check_winner() draw_marker() game_end() \
from ctypes.wintypes import SIZE
from tkinter import Widget
import pygame
import os
pygame.init()
import sys
os.system("cls")


WIDTH = 600
HEIGHT = 600

#TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
#MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tic tac toe")


colors= {"grey":(96,96,96), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
markers=[]#controls the cells 
MxMy=(0,0)#clics 
Size=3
lineWidth=10 #thickness of the line drawing 
cellx=0
crcClr=colors.get("red")#circle color 
xClr=colors.get("yellow")#xcolor
rad=WIDTH//6-25 
winner=0  #save winner ether 1 or -1, zero means tie 
player=1#to change players 1 and -1
Game=True#controls game 
GameOver=False#check game is over 
bgClr=colors.get("pink")

#function to zero grid/array 
def zero_grid():
    for x in range(Size):
        row=[0]*Size #this will create 3 zero
        markers.append(row)
        print(row)

def checkWinner():
    print()
    # add all ROWS if markers[0][]+markers[0][]+markers[0][]==3 Or markers[1][]+markers[1][]+markers[1][]==3 OR
    #winner =1

def draw_grid():
    bgClr=colors.get("pink")
    lineClr=colors.get("blue")
    for x in range(1,Size):
        pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth) #horizontal line 
        pygame.draw.line(screen,lineClr,(WIDTH//3*x,0),(WIDTH//3*x,HEIGHT),lineWidth)
    pygame.time.delay(100)
    
def draw_Markers():
    xValue=0
    for x in markers:   # getting a rw
        yValue=0
        for y in x:  #each elem fthe rw
            if y ==1:
                pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
            if y==-1:
                pygame.draw.circle(screen,crcClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
            yValue +=1
        xValue +=1

def checkWinner():
    global GameOver, winner
    x_pos=0
    for x in markers:
        if sum(x)==3:
            winner= 1
            GameOver=True
        if sum (x)==-3:
            winner=-1
            GameOver=True 
        if markers[0][x_pos]+markers[1][x_pos]+markers[2][x_pos]==3:
            winner=1
            GameOver=True 
        if markers[0][x_pos]+markers[1][x_pos]+markers[2][x_pos]==-3:
            winner=-1
            GameOver=True 
        x_pos +=1
         #to chek diagonals 
    if markers[0][0]+markers[1][1]+markers[2][2]==3 or markers[2][0]+markers[1][1]+markers[0][2]==3:
        winner=1
        GameOver=True
    if markers[0][0]+markers[1][1]+markers[2][2]==-3 or markers[2][0]+markers[1][1]+markers[0][2]==-3:
        winner=-1
        GameOver=True 
    if GameOver == False:
        tie = True
        for ROW in markers:
            for COL in ROW:
                if COL==0:
                    tie = False 
     #lets make winner 0 if it is  tie
        if tie: #in a boolean variable dont need== if tie == true 
           GameOver=True
           winner=0
    


def Game_end():
    global Game
    print("do u want to play again")
    zero_grid()
zero_grid()
Game=True
while Game:
    screen.fill(bgClr)
    draw_grid()
    draw_Markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            MxMy = pygame.mouse.get_pos()
            cellx=MxMy[0]//(WIDTH//3)
            celly=MxMy[1]//(HEIGHT//3)
            print(cellx, celly)
            if markers[cellx][celly]==0:
                markers[cellx][celly]=player
                player *=-1
                checkWinner()
                print(winner)
    pygame.time.delay(50)
    pygame.display.update()

