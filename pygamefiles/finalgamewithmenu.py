# this is the copy of the menu for the final game, now finished 
#goals for this on google doc 
#functions: for menue def game_1() then def game_1_end() to bring u to an end screen 


# Fernando Gupta
# making the full menu


import pygame, time,os,random, math, sys,datetime
pygame.init()

#screen dimentions


WIDTH = 1000
HEIGHT = 800
screen_width = 1000
screen_height = 800

clock = pygame.time.Clock()
fps = 60

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)
WINNER_FONT = pygame.font.SysFont('comicsans', 2000)

tile_size = 50
tilesize2=100
tilesize3=30
trophysize=100
coinhit=0
trophyhit=0
coinhit2=0
trophyhit2=0

coin_group = pygame.sprite.Group()

trophy_group=pygame.sprite.Group()
#load images

bg_img = pygame.image.load('pygamefiles\\forestbg.png')
bg_img=pygame.transform.scale(bg_img, (1000, 800))
bg_img2 = pygame.image.load('pygamefiles\lavabg.png')
bg_img2=pygame.transform.scale(bg_img2, (1000, 800))

os.system('cls')

#buttons ofr menu
Bx=WIDTH//3
Button_menu=pygame.Rect(Bx,150,WIDTH//4,40)
Button_instruct=pygame.Rect(Bx,150,WIDTH//4,40)
Button_settings=pygame.Rect(Bx,200,WIDTH//4,40)
Button_Game1=pygame.Rect(Bx,250,WIDTH//4,40)
Button_Game2=pygame.Rect(Bx,300,WIDTH//4,40)
Button_Game3=pygame.Rect(Bx,350,WIDTH//4,40)
Button_score=pygame.Rect(Bx,400,WIDTH//4,40)
Button_exit=pygame.Rect(Bx,450,WIDTH//4,40)
Button_colors=pygame.Rect(Bx,150,WIDTH//4,40)
Button_size=pygame.Rect(Bx,200,WIDTH//4,40)
Button_sound=pygame.Rect(Bx,300,WIDTH//4,40)
Button_SmalSize=pygame.Rect(Bx,250,WIDTH//4,40)
name_box = pygame.Rect(Bx,250,WIDTH//4,40)
Button_again=pygame.Rect(WIDTH//4,HEIGHT//2,100,50)
Button_quit=pygame.Rect(3*WIDTH//4,HEIGHT//2,100,50)



#colors
colors = {"white":(255,255,255),"grey":(96,96,96), "red":(255,0,0), "green":(0,255,0), "blue":(0,0,255), "pink":(204,0,204), "orange":(255,128,0), "yellow":(255,255,0), "purple":(127,0,255)}
clr = colors.get("white")
messageMenu=['instructions','settings','game 1','game 2','game 3','scoreboard','exit']
messageSettings=["Background Color","Screen Size bigger","Screen Size smaller","sound on/off"]
titleMain="platformer menu"


bgcolors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51),
"RED" : (255, 0, 0),
"GREEN" : (0, 255, 0),
"BLUE" : (0, 0,255),
# SHADES,
"BLACK" : (0, 0, 0),
"DARK_GREY" : (60, 60, 60),
"DARK_SLATE_GREY" : (47, 79, 79),
"DIM_GREY" : (105, 105, 105),
"FREE_SPEECH_GREY" : (99, 86, 136),
"GREY" : (190, 190, 190),
"GREY0" : (0, 0, 0),
"GREY1" : (3, 3, 3),
"GREY2" : (5, 5, 5),
"GREY3" : (8, 8, 8),
"GREY4" : (10, 10, 10),
"GREY5" : (13, 13, 13),
"GREY6" : (15, 15, 15),
"GREY7" : (18, 18, 18),
"GREY8" : (20, 20, 20),
"GREY9" : (23, 23, 23),
"GREY10" : (26, 26, 26),
"GREY11" : (28, 28, 28),
"GREY12" : (31, 31, 31),
"GREY13" : (33, 33, 33),
"GREY14" : (36, 36, 36),
"GREY15" : (38, 38, 38),
"GREY16" : (41, 41, 41),
"GREY17" : (43, 43, 43),
"GREY18" : (46, 46, 46),
"GREY19" : (48, 48, 48),
"GREY20" : (51, 51, 51),
"GREY21" : (54, 54, 54),
"GREY22" : (56, 56, 56),
"GREY23" : (59, 59, 59),
"GREY24" : (61, 61, 61),
"GREY25" : (64, 64, 64),
"GREY26" : (66, 66, 66),
"GREY27" : (69, 69, 69),
"GREY28" : (71, 71, 71),
"GREY29" : (74, 74, 74),
"GREY30" : (77, 77, 77),
"GREY31" : (79, 79, 79),
"GREY32" : (82, 82, 82),
"GREY33" : (84, 84, 84),
"GREY34" : (87, 87, 87),
"GREY35" : (89, 89, 89),
"GREY36" : (92, 92, 92),
"GREY37" : (94, 94, 94),
"GREY38" : (97, 97, 97),
"GREY39" : (99, 99, 99),
"GREY40" : (102, 102, 102),
"GREY41" : (105, 105, 105),
"GREY42" : (107, 107, 107),
"GREY43" : (110, 110, 110),
"GREY44" : (112, 112, 112),
"GREY45" : (115, 115, 115),
"GREY46" : (117, 117, 117),
"GREY47" : (120, 120, 120),
"GREY48" : (122, 122, 122),
"GREY49" : (125, 125, 125),
"GREY50" : (127, 127, 127),
"GREY51" : (130, 130, 130),
"GREY52" : (133, 133, 133),
"GREY53" : (135, 135, 135),
"GREY54" : (138, 138, 138),
"GREY55" : (140, 140, 140),
"GREY56" : (143, 143, 143),
"GREY57" : (145, 145, 145),
"GREY58" : (148, 148, 148),
"GREY59" : (150, 150, 150),
"GREY60" : (153, 153, 153),
"GREY61" : (156, 156, 156),
"GREY62" : (158, 158, 158),
"GREY63" : (161, 161, 161),
"GREY64" : (163, 163, 163),
"GREY65" : (166, 166, 166),
"GREY66" : (168, 168, 168),
"GREY67" : (171, 171, 171),
"GREY68" : (173, 173, 173),
"GREY69" : (176, 176, 176),
"GREY70" : (179, 179, 179),
"GREY71" : (181, 181, 181),
"GREY72" : (184, 184, 184),
"GREY73" : (186, 186, 186),
"GREY74" : (189, 189, 189),
"GREY75" : (191, 191, 191),
"GREY76" : (194, 194, 194),
"GREY77" : (196, 196, 196),
"GREY78" : (199, 199, 199),
"GREY79" : (201, 201, 201),
"GREY80" : (204, 204, 204),
"GREY81" : (207, 207, 207),
"GREY82" : (209, 209, 209),
"GREY83" : (212, 212, 212),
"GREY84" : (214, 214, 214),
"GREY85" : (217, 217, 217),
"GREY86" : (219, 219, 219),
"GREY87" : (222, 222, 222),
"GREY88" : (224, 224, 224),
"GREY89" : (227, 227, 227),
"GREY90" : (229, 229, 229),
"GREY91" : (232, 232, 232),
"GREY92" : (235, 235, 235),
"GREY93" : (237, 237, 237),
"GREY94" : (240, 240, 240),
"GREY95" : (242, 242, 242),
"GREY96" : (245, 245, 245),
"GREY97" : (247, 247, 247),
"GREY98" : (250, 250, 250),
"GREY99" : (252, 252, 252),
"LIGHT_GREY" : (211, 211, 211),
"SLATE_GREY" : (112, 128, 144),
"SLATE_GREY_1" : (198, 226, 255),
"SLATE_GREY_2" : (185, 211, 238),
"SLATE_GREY_3" : (159, 182, 205),
"SLATE_GREY_4" : (108, 123, 139),
"VERY_LIGHT_GREY" : (205, 205, 205),
"WHITE" : (255, 255,255),
 
 
"ALICE_BLUE" : (240, 248, 255),
"AQUA" : (0, 255, 255),
"AQUAMARINE" : (127, 255, 212),
"AQUAMARINE_1" : (127, 255, 212),
"AQUAMARINE_2" : (118, 238, 198),
"AQUAMARINE_3" : (102, 205, 170),
"AQUAMARINE_4" : (69, 139, 116),
"AZURE" : (240, 255, 255),
"AZURE_1" : (240, 255, 255),
"AZURE_2" : (224, 238, 238),
"AZURE_3" : (193, 205, 205),
"AZURE_4" : (131, 139, 139),
"BLUE_1" : (0, 0, 255),
"BLUE_2" : (0, 0, 238),
"BLUE_3" : (0, 0, 205),
"BLUE_4" : (0, 0, 139),
"BLUE_VIOLET" : (138, 43, 226),
"CADET_BLUE" : (95, 159, 159),
"CADET_BLUE_1" : (1152, 245, 255),
"CADET_BLUE_2" : (142, 229, 238),
"CADET_BLUE_3" : (122, 197, 205),
"CADET_BLUE_4" : (83, 134, 139),
"CORN_FLOWER_BLUE" : (66, 66, 111),
"CYAN" : (0, 255, 255),
"CYAN_1" : (0, 255, 255),
"CYAN_2" : (0, 238, 238),
"CYAN_3" : (0, 205, 205),
"CYAN_4" : (0, 139, 139),
"DARK_SLATE_BLUE" : (36, 24, 130),
"DARK_TURQUOISE" : (112, 147, 219),
"DEEP_SKY_BLUE" : (0, 191, 255),
"DEEP_SKY_BLUE_1" : (0, 191, 255),
"DEEP_SKY_BLUE_2" : (0, 178, 238),
"DEEP_SKY_BLUE_3" : (0, 154, 205),
"DEEP_SKY_BLUE_4" : (0, 104, 139),
"DODGER_BLUE" : (30, 144, 255),
"DODGER_BLUE_1" : (30, 144, 255),
"DODGER_BLUE_2" : (28, 134, 238),
"DODGER_BLUE_3" : (24, 116, 205),
"DODGER_BLUE_4" : (16, 78, 139),
"FREE_SPEECH_BLUE" : (65, 86, 197),
"LIGHT_BLUE" : (173, 216, 230),
"LIGHT_BLUE_1" : (191, 239, 255),
"LIGHT_BLUE_2" : (178, 223, 238),
"LIGHT_BLUE_3" : (154, 192, 205),
"LIGHT_BLUE_4" : (104, 131, 139),
"LIGHT_CYAN" : (224, 255, 255),
"LIGHT_CYAN_1" : (224, 255, 255),
"LIGHT_CYAN_2" : (209, 238, 238),
"LIGHT_CYAN_3" : (180, 205, 205),
"LIGHT_CYAN_4" : (122, 139, 139),
"LIGHT_SKY_BLUE" : (135, 206, 250),
"LIGHT_SKY_BLUE_1" : (176, 226, 255),
"LIGHT_SKY_BLUE_2" : (164, 211, 238),
"LIGHT_SKY_BLUE_3" : (141, 182, 205),
"LIGHT_SKY_BLUE_4" : (96, 123, 139),
"LIGHT_SLATE_BLUE" : (132, 112, 255),
"LIGHT_STEEL_BLUE" : (176, 196, 222),
"LIGHT_STEEL_BLUE_1" : (202, 225, 255),
"LIGHT_STEEL_BLUE_2" : (188, 210, 238),
"LIGHT_STEEL_BLUE_3" : (162, 181, 205),
"LIGHT_STEEL_BLUE_4" : (110, 123, 139),
"MEDIUM_BLUE" : (0, 0, 205),
"MEDIUM_SLATE_BLUE" : (123, 104, 238),
"MEDIUM_TURQUOISE" : (72, 209, 204),
"MIDNIGHT_BLUE" : (25, 25, 112),
"NAVY" : (0, 0, 128),
"NAVY_BLUE" : (0, 0, 128),
"NEON_BLUE" : (77, 77, 255),
"NEW_MIDNIGHT_BLUE" : (0, 0, 156),
"PALE_TURQUOISE" : (187, 255, 255),
"PALE_TURQUOISE_1" : (187, 255, 255),
"PALE_TURQUOISE_2" : (174, 238, 238),
"PALE_TURQUOISE_3" : (150, 205, 205),
"PALE_TURQUOISE_4" : (102, 139, 139),
"POWDER_BLUE" : (176, 224, 230),
"RICH_BLUE" : (89, 89, 171),
"ROYAL_BLUE" : (65, 105, 225),
"ROYAL_BLUE_1" : (72, 118, 255),
"ROYAL_BLUE_2" : (67, 110, 238),
"ROYAL_BLUE_3" : (58, 95, 205),
"ROYAL_BLUE_4" : (39, 64, 139),
"ROYAL_BLUE_5" : (0, 34, 102),
"SKY_BLUE" : (135, 206, 235),
"SKY_BLUE_1" : (135, 206, 255),
"SKY_BLUE_2" : (126, 192, 238),
"SKY_BLUE_3" : (108, 166, 205),
"SKY_BLUE_4" : (74, 112, 139),
"SLATE_BLUE" : (131, 111, 255),
"SLATE_BLUE_1" : (122, 103, 238),
"SLATE_BLUE_2" : (122, 103, 238),
"SLATE_BLUE_3" : (105, 89, 205),
"SLATE_BLUE_4" : (71, 60, 139),
"STEEL_BLUE" : (70, 130, 180),
"STEEL_BLUE_1" : (99, 184, 255),
"STEEL_BLUE_2" : (92, 172, 238),
"STEEL_BLUE_3" : (79, 148, 205),
"STEEL_BLUE_4" : (54, 100, 139),
"SUMMER_SKY" : (56, 176, 222),
"TEAL" : (0, 128, 128),
"TRUE_IRIS_BLUE" : (3, 180, 204),
"TURQUOISE" : (64, 224, 208),
"TURQUOISE_1" : (0, 245, 255),
"TURQUOISE_2" : (0, 229, 238),
"TURQUOISE_3" : (0, 197, 205),
"TURQUOISE_4" : (0, 134,139),
 
 
"BAKERS_CHOCOLATE" : (92, 51, 23),
"BEIGE" : (245, 245, 220),
"BROWN" : (166, 42, 42),
"BROWN_1" : (255, 64, 64),
"BROWN_2" : (238, 59, 59),
"BROWN_3" : (205, 51, 51),
"BROWN_4" : (139, 35, 35),
"BURLYWOOD" : (222, 184, 135),
"BURLYWOOD_1" : (255, 211, 155),
"BURLYWOOD_2" : (238, 197, 145),
"BURLYWOOD_3" : (205, 170, 125),
"BURLYWOOD_4" : (139, 115, 85),
"CHOCOLATE" : (210, 105, 30),
"CHOCOLATE_1" : (255, 127, 36),
"CHOCOLATE_2" : (238, 118, 33),
"CHOCOLATE_3" : (205, 102, 29),
"CHOCOLATE_4" : (139, 69, 19),
"DARK_BROWN" : (92, 64, 51),
"DARK_TAN" : (151, 105, 79),
"DARK_WOOD" : (133, 94, 66),
"LIGHT_WOOD" : (133, 99, 99),
"MEDIUM_WOOD" : (166, 128, 100),
"NEW_TAN" : (235, 199, 158),
"PERU" : (205, 133, 63),
"ROSY_BROWN" : (188, 143, 143),
"ROSY_BROWN_1" : (255, 193, 193),
"ROSY_BROWN_2" : (238, 180, 180),
"ROSY_BROWN_3" : (205, 155, 155),
"ROSY_BROWN_4" : (139, 105, 105),
"SADDLE_BROWN" : (139, 69, 19),
"SANDY_BROWN" : (244, 164, 96),
"SEMI_SWEET_CHOCOLATE" : (107, 66, 38),
"SIENNA" : (142, 107, 35),
"TAN" : (219, 147, 112),
"TAN_1" : (255, 165, 79),
"TAN_2" : (238, 154, 73),
"TAN_3" : (205, 133, 63),
"TAN_4" : (139, 90, 43),
"VERY_DARK_BROWN" : (92, 64,51),
 
"CHARTREUSE" : (127, 255, 0),
"CHARTREUSE_1" : (127, 255, 0),
"CHARTREUSE_2" : (118, 238, 0),
"CHARTREUSE_3" : (102, 205, 0),
"CHARTREUSE_4" : (69, 139, 0),
"DARK_GREEN" : (47, 79, 47),
"DARK_GREEN_COPPER" : (74, 118, 110),
"DARK_KHAKI" : (189, 183, 107),
"DARK_OLIVE_GREEN" : (85, 107, 47),
"DARK_OLIVE_GREEN_1" : (202, 255, 112),
"DARK_OLIVE_GREEN_2" : (188, 238, 104),
"DARK_OLIVE_GREEN_3" : (162, 205, 90),
"DARK_OLIVE_GREEN_4" : (110, 139, 61),
"DARK_SEA_GREEN" : (143, 188, 143),
"DARK_SEA_GREEN_1" : (193, 255, 193),
"DARK_SEA_GREEN_2" : (180, 238, 180),
"DARK_SEA_GREEN_3" : (155, 205, 155),
"DARK_SEA_GREEN_4" : (105, 139, 105),
"FOREST_GREEN" : (34, 139, 34),
"FREE_SPEECH_GREEN" : (9, 249, 17),
"GREEN_1" : (0, 255, 0),
"GREEN_2" : (0, 238, 0),
"GREEN_3" : (0, 205, 0),
"GREEN_4" : (0, 139, 0),
"GREEN_YELLOW" : (173, 255, 47),
"KHAKI" : (240, 230, 140),
"KHAKI_1" : (255, 246, 143),
"KHAKI_2" : (238, 230, 133),
"KHAKI_3" : (205, 198, 115),
"KHAKI_4" : (139, 134, 78),
"LAWN_GREEN" : (124, 252, 0),
"LIGHT_SEA_GREEN" : (32, 178, 170),
"LIME" : (0, 255, 0),
"MEDIUM_SEA_GREEN" : (60, 179, 113),
"MEDIUM_SPRING_GREEN" : (0, 250, 154),
"MINT_CREAM" : (245, 255, 250),
"OLIVE" : (128, 128, 0),
"OLIVE_DRAB" : (107, 142, 35),
"OLIVE_DRAB_1" : (192, 255, 62),
"OLIVE_DRAB_2" : (179, 238, 58),
"OLIVE_DRAB_3" : (154, 205, 50),
"OLIVE_DRAB_4" : (105, 139, 34),
"PALE_GREEN" : (152, 251, 152),
"PALE_GREEN_1" : (154, 255, 154),
"PALE_GREEN_2" : (144, 238, 144),
"PALE_GREEN_3" : (124, 205, 124),
"PALE_GREEN_4" : (84, 139, 84),
"SEA_GREEN" : (46, 139, 87),
"SEA_GREEN_1" : (84, 255, 159),
"SEA_GREEN_2" : (78, 238, 148),
"SEA_GREEN_3" : (67, 205, 128),
"SEA_GREEN_4" : (46, 139, 87),
"SPRING_GREEN" : (0, 255, 127),
"SPRING_GREEN_1" : (0, 255, 127),
"SPRING_GREEN_2" : (0, 238, 118),
"SPRING_GREEN_3" : (0, 205, 102),
"SPRING_GREEN_4" : (0, 139, 69),
"YELLOW_GREEN" : (154, 205,50),
"BISQUE" : (255, 228, 196),
"BISQUE_1" : (255, 228, 196),
"BISQUE_2" : (238, 213, 183),
"BISQUE_3" : (205, 183, 158),
"BISQUE_4" : (139, 125, 107),
"CORAL" : (255, 127, 0),
"CORAL_1" : (255, 114, 86),
"CORAL_2" : (238, 106, 80),
"CORAL_3" : (205, 91, 69),
"CORAL_4" : (139, 62, 47),
"DARK_ORANGE" : (255, 140, 0),
"DARK_ORANGE_1" : (255, 127, 0),
"DARK_ORANGE_2" : (238, 118, 0),
"DARK_ORANGE_3" : (205, 102, 0),
"DARK_ORANGE_4" : (139, 69, 0),
"DARK_SALMON" : (233, 150, 122),
"HONEYDEW" : (240, 255, 240),
"HONEYDEW_1" : (240, 255, 240),
"HONEYDEW_2" : (224, 238, 224),
"HONEYDEW_3" : (193, 205, 193),
"HONEYDEW_4" : (131, 139, 131),
"LIGHT_CORAL" : (240, 128, 128),
"LIGHT_SALMON" : (255, 160, 122),
"LIGHT_SALMON_1" : (255, 160, 122),
"LIGHT_SALMON_2" : (238, 149, 114),
"LIGHT_SALMON_3" : (205, 129, 98),
"LIGHT_SALMON_4" : (139, 87, 66),
"MANDARIN_ORANGE" : (142, 35, 35),
"ORANGE" : (255, 165, 0),
"ORANGE_1" : (255, 165, 0),
"ORANGE_2" : (238, 154, 0),
"ORANGE_3" : (205, 133, 0),
"ORANGE_4" : (139, 90, 0),
"ORANGE_RED" : (255, 36, 0),
"PEACH_PUFF" : (255, 218, 185),
"PEACH_PUFF_1" : (255, 218, 185),
"PEACH_PUFF_2" : (238, 203, 173),
"PEACH_PUFF_3" : (205, 175, 149),
"PEACH_PUFF_4" : (139, 119, 101),
"SALMON" : (250, 128, 114),
"SALMON_1" : (255, 140, 105),
"SALMON_2" : (238, 130, 98),
"SALMON_3" : (205, 112, 84),
"SALMON_4" : (139, 76, 57),
"SIENNA_1" : (255, 130, 71),
"SIENNA_2" : (238, 121, 66),
"SIENNA_3" : (205, 104, 57),
"SIENNA_4" : (139, 71, 38),
"DEEP_PINK," : (255, 20, 147),
"DEEP_PINK_1" : (255, 20, 147),
"DEEP_PINK_2" : (238, 18, 137),
"DEEP_PINK_3" : (205, 16, 118),
"DEEP_PINK_4" : (139, 10, 80),
"DUSTY_ROSE" : (133, 99, 99),
"FIREBRICK" : (178, 34, 34),
"FIREBRICK_1" : (255, 48, 48),
"FIREBRICK_2" : (238, 44, 44),
"FIREBRICK_3" : (205, 38, 38),
"FIREBRICK_4" : (139, 26, 26),
"FELDSPAR" : (209, 146, 117),
"FLESH" : (245, 204, 176),
"FREE_SPEECH_MAGENTA" : (227, 91, 216),
"FREE_SPEECH_RED" : (192, 0, 0),
"HOT_PINK" : (255, 105, 180),
"HOT_PINK_1" : (255, 110, 180),
"HOT_PINK_2" : (238, 106, 167),
"HOT_PINK_3" : (205, 96, 144),
"HOT_PINK_4" : (139, 58, 98),
"INDIAN_RED" : (205, 92, 92),
"INDIAN_RED_1" : (255, 106, 106),
"INDIAN_RED_2" : (238, 99, 99),
"INDIAN_RED_3" : (205, 85, 85),
"INDIAN_RED_4" : (139, 58, 58),
"LIGHT_PINK" : (255, 182, 193),
"LIGHT_PINK_1" : (255, 174, 185),
"LIGHT_PINK_2" : (238, 162, 173),
"LIGHT_PINK_3" : (205, 140, 149),
"LIGHT_PINK_4" : (139, 95, 101),
"MEDIUM_VIOLET_RED" : (199, 21, 133),
"MISTY_ROSE" : (255, 228, 225),
"MISTY_ROSE_1" : (255, 228, 225),
"MISTY_ROSE_2" : (238, 213, 210),
"MISTY_ROSE_3" : (205, 183, 181),
"MISTY_ROSE_4" : (139, 125, 123),
"ORANGE_RED_1" : (255, 69, 0),
"ORANGE_RED_2" : (238, 64, 0),
"ORANGE_RED_3" : (205, 55, 0),
"ORANGE_RED_4" : (139, 37, 0),
"PALE_VIOLET_RED" : (219, 112, 147),
"PALE_VIOLET_RED_1" : (255, 130, 171),
"PALE_VIOLET_RED_2" : (238, 121, 159),
"PALE_VIOLET_RED_3" : (205, 104, 137),
"PALE_VIOLET_RED_4" : (139, 71, 93),
"PINK" : (255, 192, 203),
"PINK_1" : (255, 181, 197),
"PINK_2" : (238, 169, 184),
"PINK_3" : (205, 145, 158),
"PINK_4" : (139, 99, 108),
"RED_1" : (255, 0, 0),
"RED_2" : (238, 0, 0),
"RED_3" : (205, 0, 0),
"RED_4" : (139, 0, 0),
"SCARLET" : (140, 23, 23),
"SPICY_PINK" : (255, 28, 174),
"TOMATO" : (255, 99, 71),
"TOMATO_1" : (255, 99, 71),
"TOMATO_2" : (238, 92, 66),
"TOMATO_3" : (205, 79, 57),
"TOMATO_4" : (139, 54, 38),
"VIOLET_RED" : (208, 32, 144),
"VIOLET_RED_1" : (255, 62, 150),
"VIOLET_RED_2" : (238, 58, 140),
"VIOLET_RED_3" : (205, 50, 120),
"VIOLET_RED_4" : (139, 34, 82),
 
"DARK_ORCHID," : (153, 50, 204),
"DARK_ORCHID_1" : (191, 62, 255),
"DARK_ORCHID_2" : (178, 58, 238),
"DARK_ORCHID_3" : (154, 50, 205),
"DARK_ORCHID_4" : (104, 34, 139),
"DARK_PURPLE" : (135, 31, 120),
"DARK_VIOLET" : (148, 0, 211),
"FUCHSIA" : (255, 0, 255),
"LAVENDER" : (230, 230, 250),
"LAVENDER_BLUSH" : (255, 240, 245),
"LAVENDER_BLUSH_1" : (255, 240, 245),
"LAVENDER_BLUSH_2" : (238, 224, 229),
"LAVENDER_BLUSH_3" : (205, 193, 197),
"LAVENDER_BLUSH_4" : (139, 131, 134),
"MAGENTA" : (255, 0, 255),
"MAGENTA_1" : (255, 0, 255),
"MAGENTA_2" : (238, 0, 238),
"MAGENTA_3" : (205, 0, 205),
"MAGENTA_4" : (139, 0, 139),
"MAROON" : (176, 48, 96),
"MAROON_1" : (255, 52, 179),
"MAROON_2" : (238, 48, 167),
"MAROON_3" : (205, 41, 144),
"MAROON_4" : (139, 28, 98),
"MEDIUM_ORCHID" : (186, 85, 211),
"MEDIUM_ORCHID_1" : (224, 102, 255),
"MEDIUM_ORCHID_2" : (209, 95, 238),
"MEDIUM_ORCHID_3" : (180, 82, 205),
"MEDIUM_ORCHID_4" : (122, 55, 139),
"MEDIUM_PURPLE" : (147, 112, 219),
"MEDIUM_PURPLE_1" : (171, 130, 255),
"MEDIUM_PURPLE_2" : (159, 121, 238),
"MEDIUM_PURPLE_3" : (137, 104, 205),
"MEDIUM_PURPLE_4" : (93, 71, 139),
"NEON_PINK" : (255, 110, 199),
"ORCHID" : (218, 112, 214),
"ORCHID_1" : (219, 112, 219),
"ORCHID_2" : (238, 122, 233),
"ORCHID_3" : (205, 105, 201),
"ORCHID_4" : (139, 71, 137),
"PLUM" : (221, 160, 221),
"PLUM_1" : (255, 187, 255),
"PLUM_2" : (238, 174, 238),
"PLUM_3" : (205, 150, 205),
"PLUM_4" : (139, 102, 139),
"PURPLE" : (160, 32, 240),
"PURPLE_1" : (155, 48, 255),
"PURPLE_2" : (145, 44, 238),
"PURPLE_3" : (125, 38, 205),
"PURPLE_4" : (85, 26, 139),
"THISTLE" : (216, 191, 216),
"THISTLE_1" : (255, 225, 255),
"THISTLE_2" : (238, 210, 238),
"THISTLE_3" : (205, 181, 205),
"THISTLE_4" : (139, 123, 139),
"VIOLET" : (238, 130, 238),
"VIOLET_BLUE" : (159, 95, 159),
 
"BLANCHED_ALMOND," : (255, 235, 205),
"DARK_GOLDENROD" : (184, 134, 11),
"DARK_GOLDENROD_1" : (255, 185, 15),
"DARK_GOLDENROD_2" : (238, 173, 14),
"DARK_GOLDENROD_3" : (205, 149, 12),
"DARK_GOLDENROD_4" : (139, 101, 8),
"LEMON_CHIFFON" : (255, 250, 205),
"LEMON_CHIFFON_1" : (255, 250, 205),
"LEMON_CHIFFON_2" : (238, 233, 191),
"LEMON_CHIFFON_3" : (205, 201, 165),
"LEMON_CHIFFON_4" : (139, 137, 112),
"LIGHT_GOLDENROD" : (238, 221, 130),
"LIGHT_GOLDENROD_1" : (255, 236, 139),
"LIGHT_GOLDENROD_2" : (238, 220, 130),
"LIGHT_GOLDENROD_3" : (205, 190, 112),
"LIGHT_GOLDENROD_4" : (139, 129, 76),
"LIGHT_GOLDENROD_YELLOW" : (250, 250, 210),
"LIGHT_YELLOW" : (255, 255, 224),
"LIGHT_YELLOW_1" : (255, 255, 224),
"LIGHT_YELLOW_2" : (238, 238, 209),
"LIGHT_YELLOW_3" : (205, 205, 180),
"LIGHT_YELLOW_4" : (139, 139, 122),
"PALE_GOLDENROD" : (238, 232, 170),
"PAPAYA_WHIP" : (255, 239, 213),
"CORNSILK" : (255, 248, 220),
"CORNSILK_1" : (255, 248, 220),
"CORNSILK_2" : (238, 232, 205),
"CORNSILK_3" : (205, 200, 177),
"CORNSILK_4" : (139, 236, 120),
"GOLDENROD" : (218, 165, 32),
"GOLDENROD_1" : (255, 193, 37),
"GOLDENROD_2" : (238, 180, 34),
"GOLDENROD_3" : (205, 155, 29),
"GOLDENROD_4" : (139, 105, 20),
"MOCCASIN" : (255, 228, 181),
"YELLOW" : (255, 255, 0),
"YELLOW_1" : (255, 255, 0),
"YELLOW_2" : (238, 238, 0),
"YELLOW_3" : (205, 205, 0),
"YELLOW_4" : (139, 139, 0),
"GOLD" : (255, 215, 0),
"GOLD_1" : (255, 215, 0),
"GOLD_2" : (238, 201, 0),
"GOLD_3" : (205, 173, 0),
"GOLD_4" : (139, 117, 0),
"MEDIUM_GOLDENROD" : (234, 234, 174),
"ANTIQUE_WHITE" : (250, 235, 215),
"ANTIQUE_WHITE_1" : (255, 239, 219),
"ANTIQUE_WHITE_2" : (238, 223, 204),
"ANTIQUE_WHITE_3" : (205, 192, 176),
"ANTIQUE_WHITE_4" : (139, 131, 120),
"FLORAL_WHITE" : (255, 250, 240),
"GHOST_WHITE" : (248, 248, 255),
"NAVAJO_WHITE" : (255, 222, 173),
"NAVAJO_WHITE_1" : (255, 222, 173),
"NAVAJO_WHITE_2" : (238, 207, 161),
"NAVAJO_WHITE_3" : (205, 179, 139),
"NAVAJO_WHITE_4" : (139, 121, 94),
"OLD_LACE" : (253, 245, 230),
"WHITE_SMOKE" : (245, 245, 245),
"GAINSBORO" : (220, 220, 220),
"IVORY" : (255, 255, 240),
"IVORY_1" : (255, 255, 240),
"IVORY_2" : (238, 238, 224),
"IVORY_3" : (205, 205, 193),
"IVORY_4" : (139, 139, 131),
"LINEN" : (250, 240, 230),
"SEASHELL" : (255, 245, 238),
"SEASHELL_1" : (255, 245, 238),
"SEASHELL_2" : (238, 229, 222),
"SEASHELL_3" : (205, 197, 191),
"SEASHELL_4" : (139, 134, 130),
"SNOW" : (255, 250, 250),
"SNOW_1" : (255, 250, 250),
"SNOW_2" : (238, 233, 233),
"SNOW_3" : (205, 201, 201),
"SNOW_4" : (139, 137, 137),
"WHEAT" : (245, 222, 179),
"WHEAT_1" : (255, 231, 186),
"WHEAT_2" : (238, 216, 174),
"WHEAT_3" : (205, 186, 150),
"WHEAT_4" : (139, 126, 102),
"QUARTZ" : (217, 217, 243),
}
clrs=bgcolors.get("limeGreen")
white=bgcolors.get("white")
blue=bgcolors.get("blue")
red=bgcolors.get("RED")
black=bgcolors.get("BLACK")
messagetic=['Play Again','Quit']
Wintext=("the winner is")
mainTitle="Circle eats Square Menu"
#create dispay wind with any name y like

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

player=1        #change players 1 and -1
gameOver=False  #check if game is over
winner=0       #save winner either 1 or -1 zero means tie
xScore=0
mx=0
my=0
oScore=0
markers=[]      #controlcells
lineWidth=10    #thickness drawing
Game=True       #control game
MxMy=(0,0)      #clicks
print(markers)  
cirClr=bgcolors.get("blue")
xClr=bgcolors.get("BLACK")

cnt=0
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#char var


#inscribed square



mx=0
my=0


run= True
speed = 1  

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
                    Game_1()
                if Button_Game2.collidepoint((mx,my)):
                    Game_2()
                if Button_Game3.collidepoint((mx,my)):
                    Game_3()
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
           
def Game_1():#https://www.youtube.com/watch?v=ZDa-Z5JzLYM  https://www.youtube.com/watch?v=BJ-VvGyQxho This is one of the videos i used to learn about classes 


    
    class Player(): #from techwithtim video and with new code from Coding with Russ, this is mostly riped directly,https://www.youtube.com/watch?v=1aGuhUFwvXA&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=7,https://www.youtube.com/watch?v=Ongc4EVqRjo&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu,https://www.youtube.com/watch?v=UdsNBIzsmlI&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5&index=3 
        def __init__(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f'pygamefiles\spritewrk\R{num}.png') 
                img_right = pygame.transform.scale(img_right, (50, 80))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0

        def update(self,trophyhit,coinhit): #dx and dy are used as a variable to track locationa and dy is used in gravity 
           
            dx = 0
            dy = 0
            walk_cooldown = 5 #walk cooldown is used 

            #get keypresses, this is movement and programing the key inputs 
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #handle animation, combo of my own code and code from code with russ
            if self.counter > walk_cooldown:
                self.counter = 0    
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            #this is makeing gravity work, this is from code with russ 
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y
            
            #collide for player with tiles 
            for tile in world.tile_list:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
            #check for coin and trophy collison, this whs my own 
            if pygame.sprite.spritecollide(self,coin_group,False):
                coinhit += 1
                if coinhit == 1:
                    myFile = open("pygamefiles\coingrab.txt", 'a')
                    myFile.write("you got 1 coin 6/24/2022")
                    myFile.close()
                    
            if pygame.sprite.spritecollide(self,trophy_group,False):
                trophyhit=1
                if trophyhit==1: #and coinhit ==1:
                    trophy1()
                if trophyhit==1:
                    myFile = open("pygamefiles\scoreboard.txt", 'a')
                    myFile.write("you got 1 coin 6/24/2022")
                    myFile.close()
               # if trophyhit==1 and coinhit==0:
                 #   trophy0()
                    
            

                
                


        #player coord update
            self.rect.x += dx
            self.rect.y += dy

            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                dy = 0

            #draw player 
            screen.blit(self.image, self.rect)#ths is bliting the hitbox 
            #pygame.draw.rect(screen, (255, 255, 255), self.rect, 2) this was for the hitbox visual 



    class Game():# this class from code with rus and my own combo https://www.youtube.com/watch?v=Ongc4EVqRjo&list=PLjcN1EyupaQnHM1I9SmiXfbT6aG4ezUvu video where this is from 
        def __init__(self, data):
            self.tile_list = []

            #load images
            dirt_img = pygame.image.load('pygamefiles\dirt.png')
            grass_img = pygame.image.load('pygamefiles\\basicplatform1.png')
            

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:#this is teh floor ad the dirt 
                        img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:#tile to place the mossy rock/main platform 
                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect) 
                        self.tile_list.append(tile)
                    if tile == 9: #this is teh tile for placing cone 
                        coin = Coin(col_count*tile_size-20,row_count*tile_size+15)
                        coin_group.add(coin)
                    if tile == 6: #tile to place tropy 
                        trophy=Trophy(col_count*tile_size,row_count*tile_size-20)
                        trophy_group.add(trophy)
                    col_count += 1
                row_count += 1

        def draw(self):# this for the hitbox for the tiles 
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])
               # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


    class Coin(pygame.sprite.Sprite): #learned pygame.sprite,Sprite from code with russ, did the rest myself 
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            img= pygame.image.load('pygamefiles\coin.png')
            self.image=pygame.transform.scale(img,(tile_size//2,tile_size//2))
            self.rect = self.image.get_rect()
            self.rect.x= x
            self.rect.y= y 


    class Trophy(pygame.sprite.Sprite):#learned pygame.sprite,Sprite from code with russ, did the rest myself 
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            img= pygame.image.load('pygamefiles\\trophy.png')
            self.image=pygame.transform.scale(img,(trophysize,trophysize))
            self.rect = self.image.get_rect()
            self.rect.x= x
            self.rect.y= y 
        
        



    world_data = [ #made this grid myself,took the way to make it from code with russ 
    [0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0], 
    [0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 2, 2, 2, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 7, 0, 5, 0, 0, 0, 0], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0], 
    [0, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0], 
    [0, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 2, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    ]




    player = Player(100, screen_height - 130)
    world = Game(world_data)



    run = True #this is to run the game 
    while run:

        clock.tick(fps)

        screen.blit(bg_img, (0, 0))
        

        world.draw() #these are to draw all the things like teh tiles, trophys and teh player 
        coin_group.draw(screen) 
        trophy_group.draw(screen)
        player.update(screen,coinhit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

def Game_2(): #this is level 2, pretty much copy of same code from before with new image , and new tile placement, so the same comments as before, just did not repeat them on all the different sections 
    class Player():
        def __init__(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f'pygamefiles\spritewrk\R{num}.png')
                img_right = pygame.transform.scale(img_right, (50   , 80))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0

        def update(self,trophyhit2,coinhit2):
            dx = 0
            dy = 0
            walk_cooldown = 5

            #get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #handle animation
            if self.counter > walk_cooldown:
                self.counter = 0    
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            for tile in world.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    #check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
            if pygame.sprite.spritecollide(self,coin_group,False):
                coinhit2 += 1
                if coinhit2 == 1:
                    myFile = open("pygamefiles\coingrab.txt", 'w')
                    myFile.write("you got 2 coins 6/24/2022")
                    myFile.close()
            if pygame.sprite.spritecollide(self,trophy_group,False):
                trophyhit2=1
                if trophyhit2==1:
                    trophy2()
                if trophyhit==1:
                    myFile = open("pygamefiles\scoreboard.txt", 'a')
                    myFile.write("you got 2 coins 6/24/2022")
                    myFile.close()
                   
               # if trophyhit2==1 and coinhit==2:
                  #  print("cat")
                   # trophy2()



            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                dy = 0

            #draw player onto screen
            screen.blit(self.image, self.rect)
           # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)




    class Game():
        def __init__(self, data):
            self.tile_list = []

            #load images
            dirt_img = pygame.image.load('pygamefiles\\rocktile.png')
            grass_img = pygame.image.load('pygamefiles\lavatile.png')

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 9:
                        coin = Coin(col_count*tile_size,row_count*tile_size+15)
                        coin_group.add(coin)
                    if tile == 6:
                        trophy=Trophy(col_count*tile_size-21,row_count*tile_size-21)
                        trophy_group.add(trophy)
                    col_count += 1
                row_count += 1

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])
               # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

    class Coin(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            img= pygame.image.load('pygamefiles\coin.png')
            self.image=pygame.transform.scale(img,(tile_size//2,tile_size//2))
            self.rect = self.image.get_rect()
            self.rect.x= x
            self.rect.y= y 


    class Trophy(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            img= pygame.image.load('pygamefiles\\trophy.png')
            self.image=pygame.transform.scale(img,(trophysize,trophysize))
            self.rect = self.image.get_rect()
            self.rect.x= x
            self.rect.y= y 
        



    world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0], 
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0], 
    [9, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 0], 
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0], 
    [0, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 0, 0], 
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 2, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0], 
    [0, 0, 0, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0], 
    [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    ]



    player = Player(100, screen_height - 130)
    world = Game(world_data)

    run = True
    while run:

        clock.tick(fps)

        screen.blit(bg_img2, (0, 0))
        

        world.draw()
        coin_group.draw(screen)
        trophy_group.draw(screen)
        player.update(screen,coinhit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
    
def Game_3(): #this is level 2, pretty much copy of same code from before with new image , and new tile placement, so the same comments as before, just did not repeat them on all the different sections 
    class Player():
        def __init__(self, x, y):
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 5):
                img_right = pygame.image.load(f'pygamefiles\spritewrk\R{num}.png')
                img_right = pygame.transform.scale(img_right, (50   , 80))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.width = self.image.get_width()
            self.height = self.image.get_height()
            self.vel_y = 0
            self.jumped = False
            self.direction = 0

        def update(self,trophyhit2,coinhit2):
            dx = 0
            dy = 0
            walk_cooldown = 5

            #get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #handle animation
            if self.counter > walk_cooldown:
                self.counter = 0    
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            for tile in world.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    #check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
            if pygame.sprite.spritecollide(self,coin_group,False):
                coinhit2 += 1
                if coinhit2 == 1:
                    myFile = open("pygamefiles\coingrab.txt", 'w')
                    myFile.write("you got 2 coins 6/24/2022")
                    myFile.close()
            if pygame.sprite.spritecollide(self,trophy_group,False):
                trophyhit2=1
                if trophyhit2==1:
                    trophy2()
                if trophyhit==1:
                    myFile = open("pygamefiles\scoreboard.txt", 'a')
                    myFile.write("you got 2 coins 6/24/2022")
                    myFile.close()
                   
               # if trophyhit2==1 and coinhit==2:
                  #  print("cat")
                   # trophy2()



            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

            if self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
                dy = 0

            #draw player onto screen
            screen.blit(self.image, self.rect)
           # pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)




    class Game():
        def __init__(self, data):
            self.tile_list = []

            #load images
            dirt_img = pygame.image.load('pygamefiles\\rocktile.png')
            grass_img = pygame.image.load('pygamefiles\lavatile.png')

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1:
                        img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 2:
                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)
                    if tile == 9:
                        coin = Coin(col_count*tile_size,row_count*tile_size+15)
                        coin_group.add(coin)
                    if tile == 6:
                        trophy=Trophy(col_count*tile_size-21,row_count*tile_size-21)
                        trophy_group.add(trophy)
                    col_count += 1
                row_count += 1

        def draw(self):
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])
               # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)

    class Coin(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            img= pygame.image.load('pygamefiles\coin.png')
            self.image=pygame.transform.scale(img,(tile_size//2,tile_size//2))
            self.rect = self.image.get_rect()
            self.rect.x= x
            self.rect.y= y 


    class Trophy(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            img= pygame.image.load('pygamefiles\\trophy.png')
            self.image=pygame.transform.scale(img,(trophysize,trophysize))
            self.rect = self.image.get_rect()
            self.rect.x= x
            self.rect.y= y 
        



    world_data = [
    [0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 2, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0], 
    [2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 5, 0, 0, 0, 0], 
    [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 9, 0, 0, 2, 0, 2, 0, 0, 2], 
    [0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0], 
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0], 
    [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 7, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    ]



    player = Player(100, screen_height - 130)
    world = Game(world_data)

    run = True
    while run:

        clock.tick(fps)

        screen.blit(bg_img2, (0, 0))
        

        world.draw()
        coin_group.draw(screen)
        trophy_group.draw(screen)
        player.update(screen,coinhit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
def trophy1(): #this is pretty much the score function from earlyer in the menu, just reused with new files and words to show the coins you got 
    #fills screen with white
    screen.fill(colors.get("white"))
    #rendering text objects
    Title = TITLE_FONT.render("You Won", 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))


    #
    # pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    # pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)

    #ReAd files Instructions and scre
    myFile = open("pygamefiles\coingrab.txt", "r")
    content = myFile.readlines()
    myFile.close()
    #var to controll change of line
    yi = 150
    for line in content:
        Item = MENU_FONT.render(line[0:14], 1, colors.get("blue"))
        screen.blit(Item, (50, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+= 40

    #renderig fonts to the screen

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Menu(titleMain,messageMenu, True)
                print("You quit")
                myFile= open('coingrab.txt', 'w')
                myFile.truncate(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1] 

def trophy2(): #this is pretty much the score function from earlyer in the menu, just reused with new files and words to show the coins you got, this is specificaly for the second trophy or lvl 2 victory, as it uses a different file 
    #fills screen with white
    screen.fill(colors.get("white"))
    #rendering text objects
    Title = TITLE_FONT.render("You Won", 1, colors.get("blue"))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))


    #
    # pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    # pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)

    #ReAd files Instructions and scre
    myFile = open("pygamefiles\coingrab2.txt", "r")
    content = myFile.readlines()
    myFile.close()
    #var to controll change of line
    yi = 150
    for line in content:
        Item = MENU_FONT.render(line[0:15], 1, colors.get("blue"))
        screen.blit(Item, (50, yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+= 40

    #renderig fonts to the screen

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

 
        
Name_enter()



