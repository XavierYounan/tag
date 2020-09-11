#IMPORT MODULES
import pygame
import random

#INITIALISE PYGAME 
pygame.init()
if(pygame.font.init()) == 0:
    print("Error the font module hasnt initialsied properrly.")

#INITALISE DISPLAY
roomWidth = 1000
roomHeight = 600
gameName = "TAG"
gameDisplay = pygame.display.set_mode((roomWidth,roomHeight))
pygame.display.set_caption(gameName)

#INITALISE CLOCK
clock = pygame.time.Clock()
FPS = 60                        #Frames per seccond -------------------------------------------------------------------------------------------------------------           

#ASSIGN GLOBALS
roomWidthHalf = roomWidth/2
roomHeightHalf = roomHeight/2
sideWallThickness = 20
false = 0
true = 1
chasing = "player1" #111111111111111111111111111111111111111111111111-----FIX LATER WHEN CHANGING WHOS CHASING

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

#ASSIGN PLAYER VARIABLES
gravity = 1
player1Speed = [4,6]        #[ x speed, jump height]
player2Speed = [4,6]        #[ x speed, jump height]
playerThickness = 40
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
    if player1Pos[0] == sideWallThickness - playerThickness/2 - player1PosChange[0]:
        player1PosChange[0] = 0
        player1Pos[0] = sideWallThickness - playerThickness/2
    return [player1PosChange[0],player1Pos[0]]
            
        
def drawPlatform(x,y,x2,y2,colour):
    pygame.draw.rect(gameDisplay,colour,[x,y,x2-x,y2-y])
    if x2 < x:
        print("ERROR YOU HAVE USED THE FUNCTION WRONG THE 1st VALUE CANNOT BE BIGGER THAT THE 3rd - X")
    if y2 < y:
        print("ERROR YOU HAVE USED THE FUNCTION WRONG THE 4TH VALUE CANNOT BE BIGGER THAT THE SECCOND - Y")
        
    if player1Pos[1] == y - playerThickness/2:
        player1PosChange[1] = 0

    if player2Pos[1] == y - playerThickness/2:
        player2PosChange[1] = 0
    return [player1PosChange[1],player2PosChange[1]]

def checkKeyboard():                                        #--------------------------- why doesnt this work
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            #PLAYER ONE
            if event.key == pygame.K_LEFT:      #Left
                keyLeft = true
            if event.key == pygame.K_RIGHT:     #Right
                keyRight = true
            if event.key == pygame.K_UP:        #Up
                keyRight = true
            if event.key == pygame.K_DOWN:      #Down
                keyRight = true
            if event.key == pygame.K_PERIOD:    #Backslash
                keyDot = true
            if event.key == pygame.K_SLASH:     #Dot
                keyForwardSlash = true
                
            #PLAYER TWO
            if event.key == pygame.K_w:         #W
                keyW = true
            if event.key == pygame.K_s:         #S
                keyS = true
            if event.key == pygame.K_a:         #A
                keyA = true
            if event == pygame.K_d:             #D
                keyD = true
            if event.key == pygame.K_q:         #Q
                keyQ = true
            if event.key == pygame.K_e:         #E
                keyE = true
                print(keyE)
                
        if event.type == pygame.KEYUP:

            #PLAYER ONE
            if event.key == pygame.K_LEFT:      #Left
                keyLeft = false
                a = 1
            if event.key == pygame.K_RIGHT:     #Right
                keyRight = false
            if event.key == pygame.K_UP:        #Up
                keyRight = false
            if event.key == pygame.K_DOWN:      #Down
                keyRight = false
            if event.key == pygame.K_PERIOD:    #Dot
                keyDot = false
            if event.key == pygame.K_SLASH:     #Backslash
                keyForwardSlash = false
                
            #PLAYER TWO
            if event.key == pygame.K_w:         #W
                keyW = false
            if event.key == pygame.K_s:         #S
                keyS = false
            if event.key == pygame.K_a:         #A
                keyA = false
            if event == pygame.K_d:             #D
                keyD = false
            if event.key == pygame.K_q:         #Q
                keyQ = false
            if event.key == pygame.K_e:         #E
                keyE = false

        

def drawPlayer1(x,y):
    pygame.draw.rect(gameDisplay,player1Colour,[x-playerThickness/2,y-playerThickness/2,playerThickness,playerThickness])


def drawPlayer2(x,y):
    pygame.draw.rect(gameDisplay,player2Colour,[x-playerThickness/2,y-playerThickness/2,playerThickness,playerThickness])
    



#---------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------START GAME------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------

while True:
    #ALWAYS ESTABLISH PLAYER IMPUTS FIRST
    #checkKeyboard()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            #PLAYER ONE
            if event.key == pygame.K_LEFT:      #Left
                keyLeft = true
            if event.key == pygame.K_RIGHT:     #Right
                keyRight = true
            if event.key == pygame.K_UP:        #Up
                keyRight = true
            if event.key == pygame.K_DOWN:      #Down
                keyRight = true
            if event.key == pygame.K_PERIOD:    #Backslash
                keyDot = true
            if event.key == pygame.K_SLASH:     #Dot
                keyForwardSlash = true
                
            #PLAYER TWO
            if event.key == pygame.K_w:         #W
                keyW = true
            if event.key == pygame.K_s:         #S
                keyS = true
            if event.key == pygame.K_a:         #A
                keyA = true
            if event.key == pygame.K_d:         #D
                keyD = true
            if event.key == pygame.K_q:         #Q
                keyQ = true
            if event.key == pygame.K_e:         #E
                keyE = true

                
        if event.type == pygame.KEYUP:

            #PLAYER ONE
            if event.key == pygame.K_LEFT:      #Left
                keyLeft = false
            if event.key == pygame.K_RIGHT:     #Right
                keyRight = false
            if event.key == pygame.K_UP:        #Up
                keyRight = false
            if event.key == pygame.K_DOWN:      #Down
                keyRight = false
            if event.key == pygame.K_PERIOD:    #Dot
                keyDot = false
            if event.key == pygame.K_SLASH:     #Backslash
                keyForwardSlash = false
                
            #PLAYER TWO
            if event.key == pygame.K_w:         #W
                keyW = false
            if event.key == pygame.K_s:         #S
                keyS = false
            if event.key == pygame.K_a:         #A
                keyA = false
            if event.key == pygame.K_d:         #D
                keyD = false
            if event.key == pygame.K_q:         #Q
                keyQ = false
            if event.key == pygame.K_e:         #E
                keyE = false
                
    clearScreen(black)      #Always clear screen first, only needed if no background
    
    #apply gravity to players
    player1PosChange[1] = gravity
    player2PosChange[1] = gravity

    #Move players left and right
    player1PosChange[0] = player1Speed[0] *(keyD - keyA)
    player2PosChange[0] = player2Speed[0] * (keyRight - keyLeft)
    
    #Note collision are run when drawing walls
    globalValuesList = drawSideWalls(red)      #Draw side walls
    player1PosChange[0] = globalValuesList[0]
    player1Pos[0] = globalValuesList[1]
    
    globalValuesList = drawPlatform(sideWallThickness,2 * roomHeight/3 - 60,roomWidth-sideWallThickness, 2*(roomHeight/3) + 60,white)
    player1PosChange[1] = globalValuesList[0]
    player2PosChange[1] = globalValuesList[1]

    #Move players before drawing them
    player1Pos[0] += player1PosChange[0]     #change x player 1
    player1Pos[1] += player1PosChange[1]     #change y player 1
    
    player2Pos[0] += player2PosChange[0]     #change x player 2
    player2Pos[1] += player2PosChange[1]     #change y player 2

    if chasing == "player1" :
        if player1Pos[0] in range (int(player2Pos[0]- playerThickness),int(player2Pos[0] + playerThickness + 1)):      #The reason why there are two player thickness is becasue you have both thicknesses to account for
            player1Pos[0] = player1SpawnPoint[0]
            player1Pos[1] = player1SpawnPoint[1]
            player2Pos[0] = player2SpawnPoint[0]
            player2Pos[1] = player2SpawnPoint[1]
            score[0] += 1
                     

    #Draw players
    drawPlayer1(player1Pos[0],player1Pos[1])
    drawPlayer2(player2Pos[0],player2Pos[1])

    #Draw HUD
    #Draw score
    drawText(roomWidth/2,200,white,basic,22,str(score[0]))
    
    
    
    pygame.display.update()
    clock.tick(FPS)


