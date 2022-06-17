import pygame, time,os,random, math, sys,datetime
pygame.init()
import os
#screen dimentions


WIDTH = 700
HEIGHT = 700

name_box = pygame.Rect(Bx,250,WIDTH//4,40)

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)

colors = {"white":(255,255,255),"grey":(96,96,96), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")
messageMenu=['instructions','settings','game 1','game 2','scoreboard','exit']
messageSettings=["Background Color","Screen Size bigger","Screen Size smaller","sound on/off"]
titleMain="circle eat square menu"
nameClr=colors.get("red")
clock=pygame.time.Clock()
bxrClr=colors.get("blue")
user_name=""
#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("main menu") # title of the window
#images
bg = colors.get("grey")
run=True
Name=TITLE_FONT.render("Enter name",1,colors.get("blue"))
screen.fill(colors.get("white"))
screen.blit(Name,(100,50))
pygame.display.update()
   
    #make the box 
    
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
               print() 
            
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                print(user_name)
                pygame.quit()
                sys.exit()
            if event.key==pygame.K_BACKSPACE:
                user_name=user_name[:-1]
            else:
                user_name+=event.unicode
        pygame.draw.rect(screen,bxrClr,name_box)



    text_surface=MENU_FONT.render(user_name,True,nameClr)
    screen.blit(text_surface,(name_box.x+5,name_box.y+5))

    pygame.display.flip()