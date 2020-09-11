import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("converting w into coords")

#!-----------------------Maze Layout----------------------!

#Table used to create the level, where W = wall
level = [
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

#Draw the wall rects as shown in the table above
x = y = 0
for row in level:
    for column in row:
        if column == "W":
            print(str(x) + "   " + str(y))
            
        x += 16
    y += 16
    x = 0


