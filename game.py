import pygame, os
from pygame.locals import *
from sys import exit
import time

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("None",48)

class Snake(pygame.sprite.Sprite):
    def __init__(self,init_x,init_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = init_x
        self.y = init_y
        self.image = pygame.image.load('pics/SnakeN.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.x,self.y)
        self.alive = True
        
        self.timeOfDeath = 0
        self.timeUntilBackAlive = 0

    def update(self,x,y):
        self.rect.move_ip(x,y)
        self.x += x
        self.y += y
        
            

    def blit(self):

        if self.alive == True:
            screen.blit(self.image,(self.x,self.y))
        


class Picogirl(pygame.sprite.Sprite):
    def __init__(self,init_x,init_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = init_x
        self.y = init_y
        self.image = pygame.image.load('pics/Picowhip.png')
        self.rect = self.image.get_rect()
        self.rect.move_ip(self.x,self.y)
        

    def update(self,x,y):
        self.rect.move_ip(x,y)
        self.x += x
        self.y += y

    def blit(self):
        screen.blit(self.image,(self.x,self.y))

#tests for collision between two objects
def testForCollision( ob1, ob2 ):
    if ob1.rect.colliderect( ob2.rect ) == True:
        return True
    else:
        return False



mysnake = Snake(400,520)
picogirl = Picogirl(100,550)

timeUntilBackAlive = 0


bg_image_filename = 'pics/background.png'

screen = pygame.display.set_mode((948,748),0,32)
bg = pygame.image.load(bg_image_filename).convert()


pygame.display.flip()

#music
intro = pygame.mixer.Sound('sounds/fanfare10.ogg')
punch = pygame.mixer.Sound('sounds/hit_p07.ogg')
appear = pygame.mixer.Sound('sounds/blah.ogg')


#counter to save movement coordinates for Picogirl
move_x = 0
#counter to save movement coordinates for the snake
move_x1 = 0

text = "Help PicoGirl defeat Python the Snake"

imageOfText = font.render(text,False,(0,0,0))
screen.blit(bg,(0,0))
screen.blit(imageOfText,(200,50))
pygame.display.update()
time.sleep(2)



pygame.mixer.Sound.play(intro)
#starting game loop
while True:
    

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

#movement for PicoGirl
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            
                
            elif event.key == K_RIGHT:
                move_x = +1
                pygame.mixer.Sound.play(punch)
                
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0 
                
            elif event.key == K_RIGHT:
                move_x = 0

#movement for Python the snake                
        if event.type == KEYDOWN:
             if event.key == K_a:
                move_x1 = -1
             elif event.key == K_s:
                move_x1 = +1
            
        elif event.type == KEYUP:
            if event.key == K_a:
                move_x1 = 0 
            elif event.key == K_s:
                move_x1 = 0

        
    mysnake.update(move_x1,0)
    picogirl.update(move_x,0)

    if testForCollision( picogirl, mysnake ) == True:
        mysnake.alive = False
        timeUntilBackAlive = time.time() + 1.0
        mysnake.update(200,10)
        pygame.mixer.Sound.play(appear)
        
        
    currentTime = time.time()
    if currentTime > timeUntilBackAlive:
        mysnake.alive = True
    

        
#drawing the images to the screen
    screen.blit(bg, (0,0))
    mysnake.blit()
    picogirl.blit()
    
        
    pygame.display.update()
