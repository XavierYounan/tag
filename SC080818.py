#IMPORT MODULES
import pygame
import random

#INITIALISE PYGAME 
pygame.init()
if(pygame.font.init()) == 0:
    print("Error the font module hasnt initialsied properrly.")

#INITALISE DISPLAY
roomWidth = 832
roomHeight = 640
gameName = "TAG"
gameDisplay = pygame.display.set_mode((roomWidth,roomHeight))
pygame.display.set_caption(gameName)

#INITALISE CLOCK
clock = pygame.time.Clock()
FPS = 60                                   #Frames per seccond -------------------------------------------------------------------------------------------------------------           

#Decode map
#!-----------------------Map Layout----------------------!

#Table used to create the level, where W = wall
level1 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                       W                        W",
"W                       W     W                  W",
"W    WWWW   WWWWW   WWWWW     W      WWWWWWWWWW  W",
"W    W          W       W     W           W      W",
"W    W                  W   WWWWWWW       W      W",
"W    W   WW                    W          W      W",
"W    W    W     WWWW           W          W      W",
"W    WWW  W     W  W           W  W   WWWWW      W",
"W         W                    W  W              W",
"WWWW      WWWWWWWWWWWWWWWWWWWWWW                 W",
"W  W     WW                    W                 W",
"W       WW                     W WWWWWWWWWWWWWWWWW",
"W             WWW              W                 W",
"W   WW               WW  WWW   W                 W",
"W    W  WWW          WWWWWWW   WWWWWWWWWWWWWWWW  W",
"W    W    W   WWW       WW         W          W  W",
"W    WW   W                            W      W  W",
"W     W   W          WWWWWWWWWWWWWWWWWWWWWWWW W  W",
"WWWW      WWWWW      WW  WWW                  W  W",
"W  W      W                W  WWWWWWWWWWWWWWWWW  W",
"W  W   WWWW     W  W       W     W               W",
"W      W           W  WWW  W            W        W",
"W      WWWW        W  W    WWWWWWWWWWWWWWWWWWWWWWW",
"W  WW     W   WWW  W  W                          W",
"W   W     W        W  W                          W",
"W   W   WWW           W    WWW                   W",
"W  WWW       WWWWWWWWWW      WWWW                W",
"W    W       W                  WWWWWWW    W     W",
"WW   W    WWWW        WWWWWW          WWWW WWWW  W",
"W    W                   W            W    W     W",
"W     W        WWW           WWWWW    W    W  WWWW",
"WWW   W        W      W               W WWWW     W",
"W W       WWWWWW   WWWW               W    W     W",
"W WWW     W        W         WWWWW    WWWW WWWWW W",
"W       WWW        W     W               W       W",
"W       W                W               W       W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

level2 = [
"WWWWWWWWWWWWW",
"W           W",
"WWWWW       W",
"W      WWWWWW",
"WW          W",
"W   WWWW    W",
"W         WWW",
"WWW         W",
"W           W",
"WWWWWWWWWWWWW",



]

wallCoordList = []
#convert w's into coordinate list
x = y = 0
for row in level2:
    for column in row:
        if column == "W":
            wallCoordList.append((x,y))
        x += 64
    y += 64
    x = 0

                  
#ASSIGN GLOBALS
roomWidthHalf = roomWidth/2
roomHeightHalf = roomHeight/2
sideWallThickness = 20
false = 0
true = 1
chasing = "player1" #111111111111111111111111111111111111111111111111-----FIX LATER WHEN CHANGING WHOS CHASING
hiding = "player2"

#SCORING
score = [0,0]           #First int is player x score seccond int is player y score

#ASSIGN COLOURS
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)

#ASSIGN FONTS
basic = "freesansbold.ttf"

#DEFINE KEYS
#keyList = [keyLeft,keyRight,keyUp,keyDown,keyDot,keyForwardSlash,keyQ,keyE,keyW,keyA,keyS,keyD]
#keyList = [keyLeft- 0,keyRight - 1,keyUp - 2,keyDown - 3,keyDot - 4,keyForwardSlash 5 ,keyQ - 6,keyE - 7,keyW - 8,keyA - 9,keyS - 10,keyD -11]
keyList = [0,0,0,0,0,0,0,0,0,0,0,0] 

#Plyer Two
keyLeft = false
keyRight = false
keyUp = false
keyDown = false
keyDot = false
keyForwardSlash = false

#Player one
keyQ = false
keyE = false
keyW = false
keyA = false
kayS = false
keyD = false

#ASSIGN PLAYER COLOURS
player1Colour = green
player2Colour = blue

#Assign player sprites ------------------------------------------------------ basic only one no animation
#Player1
player1Sprite = pygame.image.load("tempSprite.png").convert_alpha()
player1SpriteMask = pygame.mask.from_surface(player1Sprite)
player1SpriteRectangle = player1Sprite.get_rect()
player1SpriteHalfWidth = player1SpriteRectangle.center[0]
player1SpriteHalfHeight = player1SpriteRectangle.center[1]


#player two
player2Sprite = pygame.image.load("tempSprite.png").convert_alpha()
player2SpriteMask = pygame.mask.from_surface(player2Sprite)
player2SpriteRectangle = player2Sprite.get_rect()
player2SpriteHalfWidth = player2SpriteRectangle.center[0]
player2SpriteHalfHeight = player2SpriteRectangle.center[1]

#floors
whiteBoxSprite = pygame.image.load("plainWhite.jpg").convert_alpha()
whiteBoxSpriteMask = pygame.mask.from_surface(whiteBoxSprite)
whiteBoxSpriteRectangle = whiteBoxSprite.get_rect()
whiteBoxSpriteHalfWidth = whiteBoxSpriteRectangle.center[0]
whiteBoxSpriteHalfHeight = whiteBoxSpriteRectangle.center[1]



#ASSIGN PLAYER VARIABLES
#Gravity
gravityMax = 4
gravityAdd = 1
airResistanceSlow = 1

#Speed
player1Speed = [4,6]        #[ x speed, jump height]
player2Speed = [4,6]        #[ x speed, jump height]

#Velocity
player1PosChange = [0,0]
player2PosChange = [0,0]

#SPAWN PLAYERS
player1SpawnPoint = [100,100]
player1Pos = [player1SpawnPoint[0],player1SpawnPoint[1]]


player2SpawnPoint = [roomWidth-100,100]
player2Pos = [player2SpawnPoint[0], player2SpawnPoint[1]]

#DEFINE FUNCTIONS
#Fill the screen with black
def clearScreen(colour):
    gameDisplay.fill(colour)

def text_objects(text,font,colour):
    textSurface = font.render(text,True,colour)
    return textSurface, textSurface.get_rect()

def drawText(x,y,colour,font,size,text):
    drawingFont = pygame.font.Font(font,size)
    textSurf,textRect = text_objects(text,drawingFont,colour)
    textRect.center = (x,y)
    gameDisplay.blit(textSurf,textRect)
                                     
#draw left and right walls
def drawSideWalls(colour):
    pygame.draw.rect(gameDisplay,colour,[0,0,sideWallThickness,roomHeight])                                #draw left side wall
    pygame.draw.rect(gameDisplay,colour,[roomWidth-sideWallThickness,0,sideWallThickness,roomHeight])      #draw right side wall
    return [player1PosChange[0],player1Pos[0]]

def drawWhiteBox(coords):
    #Player1 Coll
    #Vertical
    player1TopCorner = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight]
    player1_whiteSquareOffsetWithVsp = (int(coords[0] - (player1TopCorner[0])),int(coords[1] - (player1TopCorner[1] + player1PosChange[1])))
    player1_whiteSquareCollideWithVsp = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetWithVsp)
    
    if player1_whiteSquareCollideWithVsp:
        player1PosChange[1] = 0
##        player1TopCorner = [player1Pos[0] - player1SpriteHalfWidth + 1,player1Pos[1] - player1SpriteHalfHeight]             #plus one on the height so it doesnt go inside box
##        player1_whiteSquareOffset = (int(coords[0] - player1TopCorner[0]),int(coords[1] - player1TopCorner[1]))
##        player1_whiteSquareCollide = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffset)
##        while player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffset):
##            print(player1TopCorner[0] + 1 - coords[0])
##            player1Pos[1] += 1
##            player1TopCorner = [player1Pos[0] - player1SpriteHalfWidth + 1,player1Pos[1] - player1SpriteHalfHeight]
##            player1_whiteSquareOffset = (int(coords[0] - player1TopCorner[0]),int(coords[1] - player1TopCorner[1]))


    #Horisontal
    player1_whiteSquareOffsetWithHsp = (int(coords[0] - (player1TopCorner[0] + player1PosChange[0])),int(coords[1] - player1TopCorner[1]))
    player1_whiteSquareCollideWithHsp = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetWithHsp)
    if player1_whiteSquareCollideWithHsp:
        player1PosChange[0] = 0
              
    gameDisplay.blit(whiteBoxSprite,coords)
        
def drawPlatform(x,y,x2,y2,colour):
    pygame.draw.rect(gameDisplay,colour,[x,y,x2-x,y2-y])
            
    if x2 < x:
        print("ERROR YOU HAVE USED THE FUNCTION WRONG THE 1st VALUE CANNOT BE BIGGER THAT THE 3rd - X")
    if y2 < y:
        print("ERROR YOU HAVE USED THE FUNCTION WRONG THE 4TH VALUE CANNOT BE BIGGER THAT THE SECCOND - Y")
        
    platformMask = pygame.Mask((int(x2-x),int(y2-y)))
    platformMask.fill
    player1TopCorner = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight]
    player1_platformOffsetWithVsp = (int(x - (player1TopCorner[0] + player1PosChange[0])),int(y - (player1TopCorner[1] + player1PosChange[1])))    
    player1_platformCollide = platformMask.overlap(player1SpriteMask,player1_platformOffsetWithVsp)
    if player1_platformCollide:
        player1PosChange[1] = 0
        player1_platformOffset = (int(player1Pos[0] - (x2-x)/2),int(player1Pos[1] - (y2-y)/2))        #update variable
        while player1SpriteMask.overlap(platformMask,player1_platformOffset) != True :
              player1Pos[1] += 1
              player1_platformOffset = (int(player1Pos[0] - (x2-x)/2),int(player1Pos[1] - (y2-y)/2))        #update variable

              
        
            
    #if player1Pos[1] == y - playerThickness/2:
        

    if player2Pos[1] == y - playerThickness/2:
        player2PosChange[1] = 0
    return [player1PosChange[1],player2PosChange[1]]

def checkKeyboard():                                      
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
#keyList = [keyLeft,keyRight,keyUp,keyDown,keyDot,keyForwardSlash,keyQ,keyE,keyW,keyA,keyS,keyD]
            #PLAYER ONE
            if event.key == pygame.K_LEFT:      #Left
                keyList[0] = true
            if event.key == pygame.K_RIGHT:     #Right
                keyList[1] = true
            if event.key == pygame.K_UP:        #Up
                keyList[2] = true
            if event.key == pygame.K_DOWN:      #Down
                keyList[3] = true
            if event.key == pygame.K_PERIOD:    #Backslash
                keyList[4] = true
            if event.key == pygame.K_SLASH:     #Dot
                keyList[5] = true
                
            #PLAYER TWO
            if event.key == pygame.K_w:         #W
                keyList[8] = true
            if event.key == pygame.K_s:         #S
                keyList[10] = true
            if event.key == pygame.K_a:         #A
                keyList[9] = true
            if event.key == pygame.K_d:         #D
                keyList[11] = true
            if event.key == pygame.K_q:         #Q
                keyList[6] = true
            if event.key == pygame.K_e:         #E
                keyList[7] = true

                
        if event.type == pygame.KEYUP:

            #PLAYER ONE
            if event.key == pygame.K_LEFT:      #Left
                keyList[0] = false
            if event.key == pygame.K_RIGHT:     #Right
                keyList[1] = false
            if event.key == pygame.K_UP:        #Up
                keyList[2] = false
            if event.key == pygame.K_DOWN:      #Down
                keyList[3] = false
            if event.key == pygame.K_PERIOD:    #Backslash
                keyList[4] = false
            if event.key == pygame.K_SLASH:     #Dot
                keyList[5] = false
                
            #PLAYER TWO
            if event.key == pygame.K_w:         #W
                keyList[8] = false
            if event.key == pygame.K_s:         #S
                keyList[10] = false
            if event.key == pygame.K_a:         #A
                keyList[9] = false
            if event.key == pygame.K_d:         #D
                keyList[11] = false
            if event.key == pygame.K_q:         #Q
                keyList[6] = false
            if event.key == pygame.K_e:         #E
                keyList[7] = false        
    return keyList
        

##def drawPlayer1(x,y):
##    pygame.draw.rect(gameDisplay,player1Colour,[x-playerThickness/2,y-playerThickness/2,playerThickness,playerThickness])
##
##
##def drawPlayer2(x,y):
##    pygame.draw.rect(gameDisplay,player2Colour,[x-playerThickness/2,y-playerThickness/2,playerThickness,playerThickness])
##    



#---------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------START GAME------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    #ALWAYS ESTABLISH PLAYER IMPUTS FIRST
    checkKeyboard()               
    clearScreen(black)      #Always clear screen first, only needed if no background
    
    #apply gravity to players
    if player1PosChange[1] < gravityMax:
        player1PosChange[1] += gravityAdd
    else:
        if player1PosChange[1] > gravityMax:
            player1PosChange[1] -= airResistanceSlow

    if player2PosChange[1] < gravityMax:
        player2PosChange[1] += gravityAdd
    else:
        if player2PosChange[1] > gravityMax:
            player2PosChange[1] -= airResistanceSlow


#keyList = [keyLeft- 0,keyRight - 1,keyUp - 2,keyDown - 3,keyDot - 4,keyForwardSlash 5 ,keyQ - 6,keyE - 7,keyW - 8,keyA - 9,keyS - 10,keyD -11]

    #Move players left and right
    player1PosChange[0] = player1Speed[0] *(keyList[11] - keyList[9])
    player2PosChange[0] = player2Speed[0] * (keyList[1] - keyList[0])
    
    #Note collision are run when drawing walls
##    globalValuesList = drawSideWalls(red)      #Draw side walls
##    player1PosChange[0] = globalValuesList[0]
##    player1Pos[0] = globalValuesList[1]
    
##    globalValuesList = drawPlatform(sideWallThickness,2 * roomHeight/3 - 60,roomWidth-sideWallThickness, 2*(roomHeight/3) + 60,white)
##    player1PosChange[1] = globalValuesList[0]
##    player2PosChange[1] = globalValuesList[1]


    for el in wallCoordList:
        drawWhiteBox(el)

    #Move players before drawing them
    player1Pos[0] += player1PosChange[0]     #change x player 1
    player1Pos[1] += player1PosChange[1]     #change y player 1
    
    player2Pos[0] += player2PosChange[0]     #change x player 2
    player2Pos[1] += player2PosChange[1]     #change y player 2


    if chasing == "player1" :
        player1_player2Offset = (player1Pos[0] - player2Pos[0],player1Pos[1] - player2Pos[1])
        player1_player2Collide = player1SpriteMask.overlap(player2SpriteMask,player1_player2Offset)
        
        if player1_player2Collide:
            player1Pos[0] = player1SpawnPoint[0]
            player1Pos[1] = player1SpawnPoint[1]
            player2Pos[0] = player2SpawnPoint[0]
            player2Pos[1] = player2SpawnPoint[1]
            score[0] += 1

          

    #Draw players
    gameDisplay.blit(player1Sprite,(player1Pos[0] - player1SpriteHalfWidth, player1Pos[1] - player1SpriteHalfHeight))
    gameDisplay.blit(player2Sprite,(player2Pos[0] - player2SpriteHalfWidth, player2Pos[1] - player2SpriteHalfHeight))

    #Draw HUD
    #Draw score
    drawText(roomWidth/2,200,white,basic,22,str(score[0]))
    
    
    
    pygame.display.update()
    clock.tick(FPS)


