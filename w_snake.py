#PyGame Snake game, based upon https://dev.to/grapejuice/getting-started-with-pygame-making-a-snake-game-2i1g
import sys,random
import pygame 

# initialize pygame 
pygame.init()

# constants that store our screen width and height ,
# they are in pixels
WIN_X = 800
WIN_Y = 600

# setting up our game window in pygame with 
# our screen width and height constants as tuple
WIN = pygame.display.set_mode((WIN_X,WIN_Y))

# setting the caption of our game
# or more precisely the label that
# you will see on the game window

pygame.display.set_caption('snake game')

#initializing pygame.time.Clock() which controls
#The FPS or frame per second or more explicitly
#For how many times per second our game loop 
#below should run
CLOCK = pygame.time.Clock()

#our infinite game loop
while 1:
   #checking for events in pygame.event.get() which
   #returns the event that occurs like 
   #any key presses or user clicking the
   #exit , maximize , minimize button
   for event in pygame.event.get():
        #here we are checking if user has clicked the exit button
        #by checking if the event.type is pygame.QUIT 
        #which is predefined in pygame as the exit button
        if event.type == pygame.QUIT:
            #if user clicked the exit button , quit the game
            #and exit out of the program
            pygame.quit()
            sys.exit()

        #using CLOCK variable mentioned above and using
        #tick method on it passing in the fps
        #this means that this loop will run 
        #25 times per second, 
        #feel free to change the value
        CLOCK.tick(25)