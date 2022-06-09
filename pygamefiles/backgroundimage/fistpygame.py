# Fernando Gupta 
# 6/9/2022
# learning basic pygame functions,
# creating screens, clrs and shapes 
import os
import pygame, time
pygame.init()# this initialize the pygame package 
os.system("cls")

WIDTH=700 #like constant 
HEIGHT=700 #this are also the parameters of teh screen/display 
#create display window with any name you like 
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("my first game")#this change the title of the pygame screen 
#pygame.time.delay(2000)#this maes the screen stay for the amount of time you define 
redClr=(255,0,0)#sets a color value 
#screen.fill(redClr)#command to fill teh screen 
#pygame.display.update()#must update every time u change the display 
#pygame.time.delay(2000)
greenClr=(0,255,0)
purpleClr=(125,0,125)
#screen.fill(greenClr)
#pygame.display.update()
#pygame.time.delay(2000)
#to keep this running u must create a loop 
hb=50
wb=50
xb=100
yb=300
square=(xb,yb,wb,hb) #creates the object t draw 
backgrnd=greenClr
run = True
while run:
    screen.fill(backgrnd)
    for event in pygame.event.get(): #will create a reaction for everything that happens with mouse or keybord
        if event.type==pygame.QUIT:
            run=False 
            print("y quit da game ")
    pygame.draw.rect(screen,redClr,square) #to make the rectange you need teh surface, the color and the shape
    #circle (surface color center radius)
    pygame.draw.circle(screen,purpleClr,(350,350),25)
    pygame.display.update()

