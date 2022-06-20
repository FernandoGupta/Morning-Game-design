#code for the first lvl of the final game 
#goals for this on google doc 
#functions: for menue def game_1() then def game_1_end() to bring u to an end screen 


import pygame, time,os,random, math, sys,datetime
pygame.init()

clock=pygame.time.Clock()

WIDTH = 700
HEIGHT = 700

#images for game
walkRight = [pygame.image.load('pygamefiles\spritewrk\R1.png'), pygame.image.load('pygamefiles\spritewrk\R2.png'), pygame.image.load('pygamefiles\spritewrk\R3.png'), pygame.image.load('pygamefiles\spritewrk\R4.png'), pygame.image.load('pygamefiles\spritewrk\R5.png'), pygame.image.load('pygamefiles\spritewrk\R6.png'), pygame.image.load('pygamefiles\spritewrk\R7.png'), pygame.image.load('pygamefiles\spritewrk\R8.png'), pygame.image.load('pygamefiles\spritewrk\R9.png')]
walkLeft = [pygame.image.load('pygamefiles\spritewrk\L1.png'), pygame.image.load('pygamefiles\spritewrk\L2.png'), pygame.image.load('pygamefiles\spritewrk\L3.png'), pygame.image.load('pygamefiles\spritewrk\L4.png'), pygame.image.load('pygamefiles\spritewrk\L5.png'), pygame.image.load('pygamefiles\spritewrk\L6.png'), pygame.image.load('pygamefiles\spritewrk\L7.png'), pygame.image.load('pygamefiles\spritewrk\L8.png'), pygame.image.load('pygamefiles\spritewrk\L9.png')]
char = pygame.image.load('pygamefiles\spritewrk\standing.png')
bg1=pygame.image.load("pygamefiles\\forestbg.png")
bg1=pygame.transform.scale(bg1, (700, 700))
platform1=pygame.image.load("pygamefiles\\basicplatform1.png")
platform1=pygame.transform.scale(platform1,(80,80))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("finalgame1") 

#going to start with code for game here

x = 50
y = 600
width = 64
height = 64
vel = 2
isJump = False
jumpCount = 7
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount 
 
    screen.blit(bg1,(0,0))
    screen.blit(platform1,(350,350))
    if walkCount + 1 >=27:
        walkCount=0

    if left:
        screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x,y))
        walkCount +=1
    else:
        screen.blit(char, (x,y))
    
    pygame.display.update()
    

#mainloop
run = True
while run:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 700 - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -7:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 7
    redrawGameWindow()