#IMPORT MODULES
import pygame
import random

#INITIALISE PYGAME 
pygame.init()

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

#ASSIGN COLOURS
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)

#ASSIGN PLAYER COLOURS
player1Colour = green
player2Colour = blue
playerThickness = 40

#ASSIGN PLAYER VARIABLES
gravity = 1
playerSpeed = 4



#DEFINE FUNCTIONS
#draw left and right walls
def drawSideWalls(colour):
    pygame.draw.rect(gameDisplay,colour,[0,0,sideWallThickness,roomHeight])                                #draw left side wall
    pygame.draw.rect(gameDisplay,colour,[roomWidth-sideWallThickness,0,sideWallThickness,roomHeight])      #draw right side wall

#Fill the screen with black
def clearScreen(colour):
    gameDisplay.fill(colour)

def drawPlatform(x,y,x2,y2,colour):
    pygame.draw.rect(gameDisplay,colour,[x,y,x2-x,y2-y])

def applyGravity(objectList):
    for el in objectList:        
        el += gravity #WRONG     
        

def drawPlayer1(x,y):
    pygame.draw.rect(gameDisplay,player1Colour,[x-playerThickness,y-playerThickness,playerThickness,playerThickness])


def drawPlayer2(x,y):
    pygame.draw.rect(gameDisplay,player2Colour,[x-playerThickness,y-playerThickness,playerThickness,playerThickness])
    



#---------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------START GAME------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------
#SPAWN PLAYERS
player1x = 100
player1y = 100

player2x =roomWidth - 100
player2y = 100

while True:
    clearScreen(black)      #Always clear screen first, only needed if no background
    #apply gravity player one
    player1y += gravity
    player2y += gravity
    
    drawSideWalls(red)      #Draw side walls
    drawPlatform(sideWallThickness,2 * roomHeight/3,roomWidth-sideWallThickness, 2*(roomHeight/3) - 60,white)
    drawPlayer1(player1x,player1y)
    drawPlayer2(player2x,player2y)
    
    
    pygame.display.update()
    clock.tick(FPS)


