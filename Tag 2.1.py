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
"W   WWWWW   W",
"W         WWW",
"WWWWWWWWWWWWW",
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
keyList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] 

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
gravityMax = 10
gravityAdd = 0.2
airResistanceSlow = 1

#Jumps
jumpsMax = 2
jumpsHeight = 5.5
jumpsRemaning = [jumpsMax,jumpsMax]

#Speed
player1Speed = 4        #[ x speed, jump height]
player2Speed = 4        #[ x speed, jump height]

#Velocity
player1PosChange = [0,0]    #float version for smooth movement
player2PosChange = [0,0]

player1ActualPosChange = [0,0] #integer version for actual moving and colliosion
player1ActualPosChange = [0,0]

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
                                     
###draw left and right walls
##def drawSideWalls(colour):
##    pygame.draw.rect(gameDisplay,colour,[0,0,sideWallThickness,roomHeight])                                #draw left side wall
##    pygame.draw.rect(gameDisplay,colour,[roomWidth-sideWallThickness,0,sideWallThickness,roomHeight])      #draw right side wall
##    return [player1PosChange[0],player1Pos[0]]

def resetVariables():
    #nothing yet
    hgfdfgfdgf = 1 

def drawWhiteBox(coords):
    #Player1 Coll
    #Vertical
    player1TopCorner = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight]
    player1_whiteSquareOffsetWithVsp = (coords[0] - (player1TopCorner[0]),coords[1] - (player1TopCorner[1] + player1ActualPosChange[1]))
    player1_whiteSquareCollideWithVsp = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetWithVsp)
    
    if player1_whiteSquareCollideWithVsp:

        #add jumps
        if player1ActualPosChange[1] > 0:
            jumpsRemaning[0] = jumpsMax

            #Move to pixel perfect location- not working
##            player1TopCorner = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight]
##            player1_whiteSquareOffsetPlusOne = (int(coords[0] - player1TopCorner[0]),int(coords[1] - (player1TopCorner[1] + 1)))
##            player1_whiteSquareCollidePlusOne = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetPlusOne)
##            while player1_whiteSquareCollidePlusOne != True:
##                player1Pos[1] += 1
##                print("e")
##                #update variables for loop
##                player1TopCorner = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight]
##                player1_whiteSquareCollideOffsetPlusOne = (int(coords[0] - player1TopCorner[0]),int(coords[1] - (player1TopCorner[1] + 1)))
##                player1_whiteSquareCollidePlusOne = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetPlusOne)
##                
##            
        
        player1ActualPosChange[1] = 0

    
    
    #Horisontal
    player1_whiteSquareOffsetWithHsp = (coords[0] - (player1TopCorner[0] + player1ActualPosChange[0]),coords[1] - player1TopCorner[1])
    player1_whiteSquareCollideWithHsp = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetWithHsp)
    if player1_whiteSquareCollideWithHsp:
        player1ActualPosChange[0] = 0


    #Player2 Coll
    #Vertical
    player2TopCorner = [player2Pos[0] - player2SpriteHalfWidth,player2Pos[1] - player2SpriteHalfHeight]
    player2_whiteSquareOffsetWithVsp = (coords[0] - player2TopCorner[0],coords[1] - (player2TopCorner[1] + player2ActualPosChange[1]))
    player2_whiteSquareCollideWithVsp = player2SpriteMask.overlap(whiteBoxSpriteMask,player2_whiteSquareOffsetWithVsp)
    
    if player2_whiteSquareCollideWithVsp:
        if player2ActualPosChange[1] > 0:
            jumpsRemaning[1] = jumpsMax
        player2ActualPosChange[1] = 0

    #Horisontal
    player2_whiteSquareOffsetWithHsp = (coords[0] - (player2TopCorner[0] + player2ActualPosChange[0]),coords[1] - player2TopCorner[1])
    player2_whiteSquareCollideWithHsp = player2SpriteMask.overlap(whiteBoxSpriteMask,player2_whiteSquareOffsetWithHsp)
    if player2_whiteSquareCollideWithHsp:
        player2ActualPosChange[0] = 0


              
    gameDisplay.blit(whiteBoxSprite,coords)
    globalVariables = [player1Pos,player1ActualPosChange,player2Pos,player2ActualPosChange]
    return globalVariables


def checkKeyboard():
    keyList[12] = false
    keyList[13] = false
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
#keyList = [keyLeft,keyRight,keyUp,keyDown,keyDot,keyForwardSlash,keyQ,keyE,keyW,keyA,keyS,keyD,keyUpPressed,keyWPressed]
            #PLAYER ONE
            if event.key == pygame.K_LEFT:      #Left
                keyList[0] = true
            if event.key == pygame.K_RIGHT:     #Right
                keyList[1] = true
            if event.key == pygame.K_UP:        #Up
                keyList[2] = true
                keyList[12] = true
            if event.key == pygame.K_DOWN:      #Down
                keyList[3] = true
            if event.key == pygame.K_PERIOD:    #Backslash
                keyList[4] = true
            if event.key == pygame.K_SLASH:     #Dot
                keyList[5] = true
                
            #PLAYER TWO
            if event.key == pygame.K_w:         #W
                keyList[8] = true
                keyList[13] = true
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

def chasingSwitch():
    #If player one was chasing, player two is chasing
    if chasing == "player1":
        chasing = "player2"

    #if player two was chasing, player one is chasing
    if chasing =="player2":
        chasing = "player1"

    #Return player chasing
    return chasing

def player1Wins():
    #Reset coordinates
    player1Pos[0] = player1SpawnPoint[0]
    player1Pos[1] = player1SpawnPoint[1]
    player2Pos[0] = player2SpawnPoint[0]
    player2Pos[1] = player2SpawnPoint[1]

    #Add one to score
    score[0] += 1

    #Switch chasing player
    chasing = chasingSwitch

    #Reset variables
    resetVariables()

    #Return variables
    globalVariables = [player1Pos,player2Pos,score,chasing]
    return globalVariables

def player2Wins():
    #Reset Coordinates
    player1Pos[0] = player1SpawnPoint[0]
    player1Pos[1] = player1SpawnPoint[1]
    player2Pos[0] = player2SpawnPoint[0]
    player2Pos[1] = player2SpawnPoint[1]

    #Add one to score
    score[1] += 1
    #Switch who's chasing
    chasing = chasingSwitch()

    #Reset variables
    resetVariables()
    
    #Return variables
    globalVariables = [player1Pos,player2Pos,score,chasing]
    return globalVariables
    

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

    #-------------------------------------------------------STEP ONE, KEYBOARD IMPUTS------------------------------------------------------------------------------
    #Establish user imputs
    checkKeyboard()



    #------------------------------------------------------STEP TWO, MOVE THE PLAYERS----------------------------------------------------------------------------
    #APPLY JUMPS TO PAYERS
    #Player two jumps
    #move up when up key is pressed
    if jumpsRemaning[0] > 0:
        if keyList[13]:
            jumpsRemaning[0] -= 1
            player1PosChange[1] =  -jumpsHeight
            
    #variable jump height
    if player2PosChange[1] < 0:
        if keyList[2] != 1:
            player2PosChange[1] = max(player2PosChange[1],-jumpsHeight/2)

    #Player one jumps
    #Move up when up key is pressed
    if jumpsRemaning[1] > 0:  
        if keyList[12]:
            jumpsRemaning[1] -= 1
            player2PosChange[1] = -jumpsHeight

    #Variable jump height
    if player1PosChange[1] < 0:
        if keyList[8] != 1:
            player1PosChange[1] = max(player1PosChange[1],-jumpsHeight/2)
            
    
            
    #APPLY GRAVITY TO PLAYERS
    #Player one gravity
    #Add gravity if not reached terminal velocity
    if player1PosChange[1] < gravityMax:
        player1PosChange[1] += gravityAdd
    else:
    #slow down if reached terminal velocity
        if player1PosChange[1] > gravityMax:
            player1PosChange[1] -= airResistanceSlow

    #Player two gravity
    #Add gravity if not reached terminal velocity
    if player2PosChange[1] < gravityMax:
        player2PosChange[1] += gravityAdd
    else:
    #slow down if reached terminal velocity
        if player2PosChange[1] > gravityMax:
            player2PosChange[1] -= airResistanceSlow

            

    #MOVE PLAYERS LEFT AND RIGHT
    player1PosChange[0] = player1Speed *(keyList[11] - keyList[9])
    player2PosChange[0] = player2Speed * (keyList[1] - keyList[0])

    


    #-----------------------------------------------STEP THREE, DRAW WALLS AND COLIDE PLAYERS WITH SAID WALLS--------------------------------------------------------
    #convert velocity into int form
    player1ActualPosChange = [int(player1PosChange[0]),int(player1PosChange[1])]
    player2ActualPosChange = [int(player2PosChange[0]),int(player2PosChange[1])]

    #run through coordinate list, draw and collide players + RETURN VALUES IF CHANGED
    for el in wallCoordList:
        player1Pos,player1ActualPosChange,player2Pos,player2ActualPosChange = drawWhiteBox(el)
        player1PosChange = player1ActualPosChange
        player2PosChange = player2ActualPosChange


     

    #---------------------------------------------STEP FOUR, MOVE PLAYERS AND DO PLAYER-PLAYER INTERACTIONS-----------------------------------------------
    #Move player coordinates
    player1Pos[0] += player1ActualPosChange[0]     #change x player 1
    player1Pos[1] += player1ActualPosChange[1]     #change y player 1
    
    player2Pos[0] += player2ActualPosChange[0]     #change x player 2
    player2Pos[1] += player2ActualPosChange[1]     #change y player 2


    #Player-player collisions
    #Player one is chasing
    if chasing == "player1" :
        #Check for collisions
        player1_player2Offset = (player1Pos[0] - player2Pos[0],player1Pos[1] - player2Pos[1])
        player1_player2Collide = player1SpriteMask.overlap(player2SpriteMask,player1_player2Offset)
        if player1_player2Collide:
            #Player one wins 
            player1Pos,player2Pos,score,chasing = player1Wins()
    else:
    #Player Two is chasing
        if chasing == "player2" :
            #Check for collisions
            player1_player2Offset = (int(player1Pos[0]) - int(player2Pos[0]),int(player1Pos[1]) - int(player2Pos[1]))
            player1_player2Collide = player1SpriteMask.overlap(player2SpriteMask,player1_player2Offset)
            if player1_player2Collide:
                player1Pos,player2Pos,score,chasing = player2Wins()

    
    #----------------------------------------------------STEP FIVE, BLIT TO SCREEN-----------------------------------------------------------------------------
    #CLEAR SCREEN
    clearScreen(black)      #Always clear screen first, only needed if no background

    #DRAW PLAYERS
    gameDisplay.blit(player1Sprite,(player1Pos[0] - player1SpriteHalfWidth, player1Pos[1] - player1SpriteHalfHeight))
    gameDisplay.blit(player2Sprite,(player2Pos[0] - player2SpriteHalfWidth, player2Pos[1] - player2SpriteHalfHeight))

    #Draw HUD
    #Draw score
    drawText(roomWidth/2 - 10,200,white,basic,22,str(score[0]))
    drawText(roomWidth/2 + 10,200,white,basic,22,str(score[1]))

    
    
    #----------------------------------------------------------STEP SIX, UPDATE----------------------------------------------------------------------
    #UPDATE DISPLAY
    pygame.display.update()
    #WAIT 
    clock.tick(FPS)


