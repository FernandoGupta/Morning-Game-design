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
platform2=pygame.image.load("pygamefiles\\basicplatform1.png")
platform3=pygame.image.load("pygamefiles\\basicplatform1.png")
platform4=pygame.image.load("pygamefiles\\basicplatform1.png")
platform5=pygame.image.load("pygamefiles\\basicplatform1.png")
platform6=pygame.image.load("pygamefiles\\basicplatform1.png")
platform7=pygame.image.load("pygamefiles\\basicplatform1.png")
platform8=pygame.image.load("pygamefiles\\basicplatform1.png")
platform1=pygame.transform.scale(platform1,(100,100))
platform2=pygame.transform.scale(platform1,(100,100))
platform3=pygame.transform.scale(platform1,(100,100))
platform4=pygame.transform.scale(platform1,(100,100))
platform5=pygame.transform.scale(platform1,(100,100))
platform6=pygame.transform.scale(platform1,(100,100))
platform7=pygame.transform.scale(platform1,(100,100))
platform8=pygame.transform.scale(platform1,(100,100))
screen = pygame.display.set_mode((WIDTH, HEIGHT))

hitboxrec=pygame.Rect(50,600,40,64)
platformrec=pygame.Rect(105,570,80,20)
platformrec2=pygame.Rect(205,457,80,20)

pygame.display.set_caption("finalgame1") 

#going to start with code for game here
class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0
        self.hitbox= (self.x+17, self.y+11,29,52)

    def draw(self,screen):
        if self.walkCount + 1 >=27:
            self.walkCount=0

        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1 
        else:
            screen.blit(char, (self.x,self.y))
        self.hitbox= (self.x+17, self.y+11,29,52)
        pygame.draw.rect(screen,(255,0,0),self.hitbox)
    

def redrawGameWindow():
    global walkCount 
 
    screen.blit(bg1,(0,0))
    screen.blit(platform1,(350,350))
    screen.blit(platform2,(100,550))
    screen.blit(platform3,(200,450))
    screen.blit(platform4,(100,350))
    screen.blit(platform5,(450,250))
    screen.blit(platform6,(600,150))
    screen.blit(platform7,(450,100))
    screen.blit(platform8,(300,100))
    man.draw(screen)
    pygame.draw.rect(screen,(0,0,0),platformrec)
    pygame.draw.rect(screen,(0,0,0),platformrec2)
    
    pygame.display.update()
    

#mainloop
man=player(300,410,64,64)
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        hitboxrec.x-=man.vel
    if keys[pygame.K_RIGHT] and man.x < 700 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        hitboxrec.x+=man.vel
    
    else:
        man.right = False
        man.left = False
        man.walkCount = 0
    
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -12:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            hitboxrec.y-=(man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 12
    if hitboxrec.colliderect(platformrec):
       print("9")
            
   
            
        

    redrawGameWindow()