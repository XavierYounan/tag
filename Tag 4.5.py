
#IMPORT MODULES
import pygame
import random
import math

#INITIALISE PYGAME 
pygame.init()
if(pygame.font.init()) == 0:
    print("Error the font module hasn't initialsied properly.")





#Decode map
#!-----------------------Map Layout----------------------!

#Table used to create the level, where W = wall


level2 = [
"WWWWWWWWWWWWWWWWWWWWW",
"W 1           2     W",
"WWWW   W  WWWWWW    W",
"W                   W",
"W WWWWW  WWWWWWWW  WW",
"W                   W",
"W   WWWW      WWWWW W",
"W                   W",
"WW    WWW WWWWW   WWW",
"W                   W",
"W WWWW   WWW    WWW W",
"W  W                W",
"W WWWWWW WWWW   W   W",
"W                   W",
"WWWWWWWWWWWWWWWWWWWWW",
]

level1 = [
"WWWWWWWWWWWWWWWWWWWWW",
"W                   W",
"W                   W",
"W     1    2        W",
"W                   W",
"W                   W",
"W                   W",
"W                   W",
"W                   W",
"W                   W",
"W                   W",
"WWWWWWWWWWWWWWWWWWWWW",
]

level3 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W                  1                                      2                        W",
"W    WWWW                                                                          W",
"W    WWWW                                                                          W",
"W                        WWWWWWWWWWWWWWWWWWWW           WWWWWWW                    W",
"W             WWWW                                                                 W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W    WWWWWW                                                                        W",
"W                                                       WWWWWWWWWWWWWWW            W",
"W                                                       WWWWWWWWWWWWWWW            W",
"W                    WWWWWWWWWWWWWWWWWWWWWW             WWWWWWWWWWWWWWW            W",
"W                                                                                  W",
"W   WWWWWWWWWWW                                                                    W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W                        WWWWWWWWWWWWW                                             W",
"W                        WWWWWWWWWWWWW                                             W",
"W                                                WWWWWWWWWWWWWWWWWWWW              W",
"W                                                                                  W",
"W           WW                                                                     W",
"W           WW                                                                     W",
"W                                                                                  W",
"W                                                                                  W",
"W                             WWWWWWWWWWWWWWWWWWWWWW            WWWWWWWWWWWWWWWWWWWW",
"W                                                               WWWWWWWWWWWWWWWWWWWW",
"W                                                                                  W",
"W    WWWWWWWWWWWWWWWW                                                              W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                    WWWWWW                        W",
"W    WWWWWWWWWWWW                                    WWWWWWWWWWWWWWWWW             W",
"W    WWWWWWWWWWWW                                           WWWWWWWWWW             W",
"W    WWWW                                                                          W",
"W    WWWW                                                                          W",
"W    WWWW                   WWWWWWWWWWWWWW                                         W",
"W    WWWW                                                                          W",
"W                                                                                  W",
"W                                                                         WWWWW    W",
"W                                                                         WWWWW    W",
"W                                                                         WWWWW    W",
"W    WWWWWWWWW    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                        WWWWW    W",
"W    WWWWWWWWW    WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW                                 W",
"W                                                                                  W",
"W                                                                                  W",
"W                                                                                  W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

mapList = [level1,level2,level3]

#INITALISE DISPLAY
roomWidthStart = 800
roomHeightStart = 600
roomWidth = 800
roomHeight = 600
gameName = "TAG"
gameDisplay = pygame.display.set_mode((roomWidthStart,roomHeightStart))
pygame.display.set_caption(gameName)

#INITALISE CLOCK
clock = pygame.time.Clock()
FPS = 30                                   #Frames per seccond -------------------------------------------------------------------------------------------------------------           


#Initalise globals
state = "1st menu"
                  
#ASSIGN GLOBALS
roomWidthHalf = roomWidth/2
roomHeightHalf = roomHeight/2
sideWallThickness = 20
false = 0
true = 1

#PLAYER CHASING /HIDING
playerChasing = 1 
hiding = 2


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

#Numbers
keyListNumbers = [0,0,0,0,0,0,0,0,0,0]
#keyListNumbers = [key0,Key1,key2,key3,key4,key5,key6,key7,key8,key9]
key1 = false
key2 = false
key3 = false
key4 = false
key5 = false
key6 = false
key7 = false
key8 = false
key9 = false
key0 = false

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
whiteBoxSprite = pygame.image.load("black16x16.jpg").convert_alpha()
whiteBoxSpriteMask = pygame.mask.from_surface(whiteBoxSprite)
whiteBoxSpriteRectangle = whiteBoxSprite.get_rect()
whiteBoxSpriteHalfWidth = whiteBoxSpriteRectangle.center[0]
whiteBoxSpriteHalfHeight = whiteBoxSpriteRectangle.center[1]



#ASSIGN PLAYER VARIABLES
#Switch maps
roundsBeforeSwitch = 2
roundsUntillSwitch = roundsBeforeSwitch


#Gravity
gravityMax = 10
gravityAdd = 0.2
airResistanceSlow = 0.1

#Jumps
jumpsMax = 2
jumpsHeight = 20
jumpsRemaning = [jumpsMax,jumpsMax]
fallSpeedIncreace = 1.2 #must be bigger than 1

#Speed
BaseSpeed = 8
chasingSpeedMultiplier = 1.3
player1Speed = BaseSpeed        #[ x speed, jump height]
player2Speed = BaseSpeed        #[ x speed, jump height]

#Initilise bad countdown, never works because the code doesnt alwyas run at max speed
tagSwitchTime = 30 #in secconds
tagTimerCountdown = FPS * tagSwitchTime

#Velocity
player1PosChange = [0,0]    #float version for smooth movement
player2PosChange = [0,0]

player1ActualPosChange = [0,0] #integer version for actual moving and colliosion
player1ActualPosChange = [0,0]


#DEFINE FUNCTIONS
#Fill the screen with black
def loadMap(mapNumber):
    wallCoordList = []
    spawnPointList1 = []
    spawnPointList2 = []
    roomWidth = 0
    roomHeight = 0
    blockSize = 16

    #convert w's into coordinate list
    x = y = 0
    for row in mapList[mapNumber-1]:
        for column in row:
            if column == "W":
                wallCoordList.append((x,y))
            if column == "1":
                spawnPointList1.append((x,y))
            if column == "2":
                spawnPointList2.append((x,y))
            x += blockSize
            if x > roomWidth:
                roomWidth = x
        y += blockSize
        if y > roomHeight:
            roomHeight = y
        x = 0
        
    #SPAWN PLAYERS
    player1SpawnPoint = list(spawnPointList1[0])
    player1Pos = [player1SpawnPoint[0],player1SpawnPoint[1]]


    player2SpawnPoint = list(spawnPointList2[0])
    player2Pos = [player2SpawnPoint[0], player2SpawnPoint[1]]
    
    return wallCoordList,player1SpawnPoint,player2SpawnPoint,player1Pos,player2Pos,roomWidth,roomHeight

def clearScreen(colour):
    gameDisplay.fill(colour)

def mapCheckSwitch(roundsUntillSwitch,state):
    roundsUntillSwitch -= 1
    if roundsUntillSwitch <= 0:
        state = "1st menu"
        roundsUntillSwitch = roundsBeforeSwitch
    
    return roundsUntillSwitch,state

def intRoundUp(number):
    g = int(number) + 1
    return g

def text_objects(text,font,colour):
    textSurface = font.render(text,True,colour)
    return textSurface, textSurface.get_rect()

def drawText(x,y,colour,font,size,text):
    drawingFont = pygame.font.Font(font,size)
    textSurf,textRect = text_objects(text,drawingFont,colour)
    textRect.center = (x,y)
    gameDisplay.blit(textSurf,textRect)


def resetVariables():
    #RESET TIMER
    tagTimerCountdown = FPS * tagSwitchTime
    return tagTimerCountdown

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


##        #Move to pixel perfect location
##        player1TopCornerMinusTwo = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight + 1]
##        player1_whiteSquareOffsetMinusTwo = [coords[0] - player1TopCornerMinusTwo[0],coords[1]  - player1TopCornerMinusTwo[1]]
##        player1_whiteSquareCollideMinusTwo = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetMinusTwo)
##        while player1_whiteSquareCollideMinusTwo == None:
##            player1Pos[1] += 1
##            #update variables for loop
##            player1TopCornerMinusTwo = [player1Pos[0] - player1SpriteHalfWidth,player1Pos[1] - player1SpriteHalfHeight - 2]
##            player1_whiteSquareOffsetMinusTwo = [coords[0] - player1TopCornerMinusTwo[0],coords[1]  - player1TopCornerMinusTwo[1]]
##            player1_whiteSquareCollideMinusTwo = player1SpriteMask.overlap(whiteBoxSpriteMask,player1_whiteSquareOffsetMinusTwo)
   
        
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
                
            #Keyboard numbers  
            if event.key == pygame.K_0:         #0
                keyListNumbers[0] = true
            if event.key == pygame.K_1:         #1
                keyListNumbers[1] = true
            if event.key == pygame.K_2:         #2
                keyListNumbers[2] = true
            if event.key == pygame.K_3:         #3
                keyListNumbers[3] = true
            if event.key == pygame.K_4:         #4
                keyListNumbers[4] = true
            if event.key == pygame.K_5:         #5
                keyListNumbers[5] = true
            if event.key == pygame.K_6:         #6
                keyListNumbers[6] = true
            if event.key == pygame.K_7:         #7
                keyListNumbers[7] = true
            if event.key == pygame.K_8:         #8
                keyListNumbers[8] = true
            if event.key == pygame.K_9:         #9
                keyListNumbers[9] = true

            

                
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

              #Keyboard numbers
            if event.key == pygame.K_0:         #0
                keyListNumbers[0] = false
            if event.key == pygame.K_1:         #1
                keyListNumbers[1] = false
            if event.key == pygame.K_2:         #2
                keyListNumbers[2] = false
            if event.key == pygame.K_3:         #3
                keyListNumbers[3] = false
            if event.key == pygame.K_4:         #4
                keyListNumbers[4] = false
            if event.key == pygame.K_5:         #5
                keyListNumbers[5] = false
            if event.key == pygame.K_6:         #6
                keyListNumbers[6] = false
            if event.key == pygame.K_7:         #7
                keyListNumbers[7] = false
            if event.key == pygame.K_8:         #8
                keyListNumbers[8] = false
            if event.key == pygame.K_9:         #9
                keyListNumbers[9] = false

    
    keyboardImputs = keyList,keyListNumbers            
    return keyboardImputs


def playerChasingSwitch(playerChasing):
    #If player one was chasing, player two is chasing
    if playerChasing == 1:
        playerChasing = 2
    else:
        #if player two was chasing, player one is chasing
        if playerChasing == 2:
            playerChasing = 1

    #Return player chasing
    return playerChasing

def player1Wins(playerChasing,tagTimerCountdown):
    #Reset coordinates
    player1Pos[0] = player1SpawnPoint[0]
    player1Pos[1] = player1SpawnPoint[1]
    player2Pos[0] = player2SpawnPoint[0]
    player2Pos[1] = player2SpawnPoint[1]

    #Add one to score
    score[0] += 1

    #SWITCH CHASING PLAYER
    playerChasing = playerChasingSwitch(playerChasing)

    #Reset variables
    tagTimerCountdown = resetVariables()

    #Return variables
    globalVariables = [player1Pos,player2Pos,score,playerChasing,tagTimerCountdown]
    return globalVariables

def player2Wins(playerChasing,tagTimerCountdown):
    #Reset Coordinates
    player1Pos[0] = player1SpawnPoint[0]
    player1Pos[1] = player1SpawnPoint[1]
    player2Pos[0] = player2SpawnPoint[0]
    player2Pos[1] = player2SpawnPoint[1]

    #Add one to score
    score[1] += 1
    #Switch who's chasing
    playerChasing = playerChasingSwitch(playerChasing)

    #Reset variables
    tagTimerCountdown = resetVariables()

    
    #Return variables
    globalVariables = [player1Pos,player2Pos,score,playerChasing,tagTimerCountdown]
    return globalVariables


#---------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------START GAME------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    while state == "1st menu":       
        clearScreen(black)
        gameDisplay = pygame.display.set_mode((roomWidthStart,roomHeightStart))

        
        keyList,keyListNumbers = checkKeyboard()
        mapRange = len(mapList)
    
        for el in range (1,mapRange+1,1):
            if keyListNumbers[el]:
                mapNumber = el
                wallCoordList,player1SpawnPoint,player2SpawnPoint,player1Pos,player2Pos,roomWidth,roomHeight = loadMap(el)
                gameDisplay = pygame.display.set_mode((roomWidth,roomHeight))
                state = "playing"




            
        pygame.display.update()
        #WAIT 
        clock.tick(FPS)

        




        
    while state == "playing":

        #-------------------------------------------------------STEP ONE, KEYBOARD IMPUTS/ CLEAR SCREEN------------------------------------------------------------------------------
        #CLEAR5 SCREEN
        clearScreen(white)      #Always clear screen first, only needed if no background
        
        #Establish user imputs
        keyList,keyListNumbers = checkKeyboard()

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

        #falling fast
        if keyList[3]:
            player2PosChange[1] += fallSpeedIncreace

        #falling fast
        if keyList[10]:
            player1PosChange[1] += fallSpeedIncreace
            
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
        if playerChasing == 1:
            player1Speed = BaseSpeed * chasingSpeedMultiplier
            player2Speed = BaseSpeed
        else:
            if playerChasing == 2:
                player2Speed = BaseSpeed * chasingSpeedMultiplier
                player1Speed = BaseSpeed
                    


        player1PosChange[0] = player1Speed *(keyList[11] - keyList[9])
        player2PosChange[0] = player2Speed * (keyList[1] - keyList[0])

        


        #-----------------------------------------------STEP THREE, DRAW WALLS AND COLIDE PLAYERS WITH SAID WALLS--------------------------------------------------------
        #convert velocity into int form
        player1ActualPosChange = [int(player1PosChange[0]),intRoundUp(player1PosChange[1])]
        player2ActualPosChange = [int(player2PosChange[0]),intRoundUp(player2PosChange[1])]

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
        if playerChasing == 1 :
            #Check for collisions
            player1_player2Offset = (player1Pos[0] - player2Pos[0],player1Pos[1] - player2Pos[1])
            player1_player2Collide = player1SpriteMask.overlap(player2SpriteMask,player1_player2Offset)
            if player1_player2Collide:
                #Player one wins this round
                player1Pos,player2Pos,score,playerChasing,tagTimerCountdown = player1Wins(playerChasing,tagTimerCountdown)
                roundsUntillSwitch,state = mapCheckSwitch(roundsUntillSwitch,state)
                print(state)
        
        #Player Two is chasing
        if playerChasing == 2 :
            #Check for collisions
            player1_player2Offset = (player1Pos[0] - player2Pos[0],player1Pos[1] - player2Pos[1])
            player1_player2Collide = player1SpriteMask.overlap(player2SpriteMask,player1_player2Offset)
            if player1_player2Collide:
                #Player two wins this round
                player1Pos,player2Pos,score,playerChasing,tagTimerCountdown = player2Wins(playerChasing,tagTimerCountdown)
                roundsUntillSwitch,state = mapCheckSwitch(roundsUntillSwitch,state)

        #Timer stuff
        tagTimerCountdown -= 1
        if tagTimerCountdown == 0:
            if playerChasing == 2:
                #player 1 wins this round
                player1Pos,player2Pos,score,playerChasing,tagTimerCountdown = player1Wins(playerChasing,tagTimerCountdown)
                roundsUntillSwitch,state = mapCheckSwitch(roundsUntillSwitch,state)


            else:
                if playerChasing == 1:
                    #Player two wins this round
                    player1Pos,player2Pos,score,playerChasing,tagTimerCountdown = player2Wins(playerChasing,tagTimerCountdown)
                    roundsUntillSwitch,state = mapCheckSwitch(roundsUntillSwitch,state)

        
        #----------------------------------------------------STEP FIVE, BLIT TO SCREEN-----------------------------------------------------------------------------
        #DRAW PLAYERS
        gameDisplay.blit(player1Sprite,(player1Pos[0] - player1SpriteHalfWidth, player1Pos[1] - player1SpriteHalfHeight))
        gameDisplay.blit(player2Sprite,(player2Pos[0] - player2SpriteHalfWidth, player2Pos[1] - player2SpriteHalfHeight))
        

        #Draw HUD
        #Draw Distance
        distanceApartX = player1Pos[0] - player2Pos[0]
        distanceApartY = player1Pos[1] - player2Pos[1]
        drawText(roomWidth-200,200,black,basic,22,str(distanceApartX))
        drawText(roomWidth-250,200,black,basic,22,str(distanceApartY))
        
        #distanceApart = math.sqrt(distanceApartX^2 + distanceApartY^2)
        #drawText(roomWidth - 200,200,black,basic,22,str(distanceApart) + " Meters")
        
        
        #Draw score
        if playerChasing == 1:
            player1Colour = blue
            player2Colour = black
        if playerChasing == 2:
            player2Colour = blue
            player1Colour = black
            
        drawText(roomWidth/2 - 10,200,player1Colour,basic,22,str(score[0]))
        drawText(roomWidth/2 + 10,200,player2Colour,basic,22,str(score[1]))

        #Draw time remaning
        
        a = tagTimerCountdown 
        while(a % FPS) != 0:
            a-=1        
        tagTimerCountdownDisplay = int(a/FPS + 1)
        drawText(200,200,black,basic,22,str(tagTimerCountdownDisplay))

        
        
        #----------------------------------------------------------STEP SIX, UPDATE----------------------------------------------------------------------
        #UPDATE DISPLAY
        pygame.display.update()
        #WAIT 
        clock.tick(FPS)

