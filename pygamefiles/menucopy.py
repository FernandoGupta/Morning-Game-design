# this is the copy of the menu for later use in the final project 


import pygame, time,os,random, math, sys,datetime
pygame.init()

#screen dimentions


WIDTH = 700
HEIGHT = 700
Bx=WIDTH//3

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
WINNER_FONT = pygame.font.SysFont('comicsans', 2000)

os.system('cls')

#buttons ofr menu
Bx=WIDTH//3
Button_menu=pygame.Rect(Bx,150,WIDTH//4,40)
Button_instruct=pygame.Rect(Bx,150,WIDTH//4,40)
Button_settings=pygame.Rect(Bx,200,WIDTH//4,40)
Button_Game1=pygame.Rect(Bx,250,WIDTH//4,40)
Button_Game2=pygame.Rect(Bx,300,WIDTH//4,40)
Button_score=pygame.Rect(Bx,350,WIDTH//4,40)
Button_exit=pygame.Rect(Bx,400,WIDTH//4,40)
Button_colors=pygame.Rect(Bx,150,WIDTH//4,40)
Button_size=pygame.Rect(Bx,200,WIDTH//4,40)
Button_sound=pygame.Rect(Bx,300,WIDTH//4,40)
Button_SmalSize=pygame.Rect(Bx,250,WIDTH//4,40)
name_box = pygame.Rect(Bx,250,WIDTH//4,40)



#colors
colors = {"white":(255,255,255),"grey":(96,96,96), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")
messageMenu=['instructions','settings','game 1','game 2','scoreboard','exit']
messageSettings=["Background Color","Screen Size bigger","Screen Size smaller","sound on/off"]
titleMain="circle eat square menu"

clock=pygame.time.Clock()
#create a display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("main menu") # title of the window
#images
nameClr=colors.get("red")
bxrClr=colors.get("blue")
user_name=""
bg = colors.get("grey")
char = pygame.image.load("pygamefiles\game\PixelArtTutorial.png")
char = pygame.transform.scale(char, (50,50))
user_name=''
nameclr=(0,105,105)

cnt=0
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#circle var
cx = 350
cy = 350
rad = 25

#square var
hb = 50
wb = 50
xb = 325
yb = 325
square = pygame.Rect(xb,yb,wb,hb) #create the object to draw

#char var
charx = xb
chary = yb

#inscribed square
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)
insSquare=pygame.Rect(xig,yig,ibox,ibox)

#bounce
mountainSquare = pygame.Rect(250, 320, 180, 250)
insSquare=pygame.Rect(xig,yig,ibox,ibox)

mx=0
my=0


run= True
speed = 1  
    
square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("pink")
#keep running create a lp
mountainSquare=pygame.Rect(250,320,180,250)
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
Game = False

def Name_enter():
    global user_name, cnt
    Name=TITLE_FONT.render("Enter name",1,colors.get("blue"))
    screen.fill(colors.get("white"))
    screen.blit(Name,(100,50))
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu, True)
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                print() 
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    print(user_name)
                    Menu(titleMain,messageMenu, True)
                if event.key==pygame.K_BACKSPACE:
                    user_name=user_name[:-1]
                else:
                    user_name+=event.unicode
            pygame.draw.rect(screen,bxrClr,name_box)
        text_surface=MENU_FONT.render(user_name,True,nameClr)
        screen.blit(text_surface,(name_box.x+5,name_box.y+5))
        
        pygame.display.flip()
        cnt+=1


def Menu(Title, message,MENU):
    textTitle = TITLE_FONT.render(Title, 1, colors.get("blue"))
    screen.fill(colors.get('white'))
    xd = WIDTH//2 - (textTitle.get_width()//2)
    screen.blit(textTitle, (xd, 50))
    yMenu=150
    clslist=list(colors.keys())
    for item in message:
        colorRand=random.choice(clslist)
        if colorRand == "blue":
            colorRand=random.choice(clslist)

        Button_menu=pygame.Rect(Bx, yMenu, WIDTH//3, 40)
        text=MENU_FONT.render(item, 1, colors.get("blue"))
        pygame.draw.rect(screen, colors.get(colorRand), Button_menu)
        screen.blit(text, (Bx, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                textTitle = TITLE_FONT.render("Finished", 1, colors.get("blue"))
                screen.fill(colors.get('white'))
                xd = WIDTH//2 - (textTitle.get_width()//2)
                yd = HEIGHT//2- 40
                screen.blit(textTitle, (xd, yd))
                pygame.display.update()
                pygame.time.delay(500)
                pygame.quit()
                sys.exit()

                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                print(mx,my)
                if Button_instruct.collidepoint((mx, my)):
                    scoreInt("Instructions","pygamefiles\instructions.txt")
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx,my)):
                    print()
                if Button_Game2.collidepoint((mx,my)):
                    print()
                if Button_score.collidepoint((mx,my)):
                    scoreInt("ScoreBoard", "pygamefiles\scoreboard.txt")
                if Button_exit.collidepoint((mx,my)):
                    textTitle = TITLE_FONT.render("Finished", 1, colors.get("blue"))
                    name="fernando"
                    sce=374
                    date=datetime.datetime.now()
                    scrLine=str(sce)+"      "+name + "      "+date.strftime("%m-%d-%Y")+ "\n"
                    myFile = open("pygamefiles\scoreboard.txt", 'a')
                    myFile.write(scrLine)
                    myFile.close()
                    screen.fill(colors.get('white'))
                    xd = WIDTH//2 - (textTitle.get_width()//2)
                    yd = HEIGHT//2- 40
                    screen.blit(textTitle, (xd, yd))
                    pygame.display.update()
                    pygame.time.delay(500)
                    pygame.quit()
                    sys.exit()
                    
           
def scoreInt(titleF,fileN):
    
    #fills screen with white
    screen.fill(colors.get("white"))
    #rendering text objects
    Title = TITLE_FONT.render(titleF, 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    text1 = MENU_FONT.render("Yes", 1, colors.get("blue"))
    text2 = MENU_FONT.render("No", 1, colors.get("blue"))

    #creating button options
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    # pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    # pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)

    #ReAd files Instructions and scre
    myFile = open(fileN, "r")
    content = myFile.readlines()
    myFile.close()
    #var to controll change of line
    yi = 150
    for line in content:
        Item = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Item, (40, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+= 40

    #renderig fonts to the screen

    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu, True)
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    Menu(titleMain,messageMenu, True) 
                # if Button_2.collidepoint((mx, my)):
                #     return False

def settings():
    global WIDTH
    global HEIGHT
    global message
    global screen

    WIDTH=700
    HEIGHT=700
    Menu("Settings",messageSettings, False)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu,True)
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_colors.collidepoint((mx, my)):
                    print("Change colors")
                if Button_size.collidepoint((mx, my)) and WIDTH <1100 and HEIGHT <1100:
                    WIDTH+=100
                    HEIGHT+=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                    print("Change size")
                if Button_SmalSize.collidepoint((mx,my)) and WIDTH>500 and HEIGHT>500:
                    WIDTH-=100
                    HEIGHT-=100
                    screen=pygame.display.set_mode((WIDTH,HEIGHT))
                    print("Change size small")
                if Button_sound.collidepoint((mx, my)):
                    print("Change sounds")
               
                # if Button_2.collidepoint((mx, my)):
                #     return False