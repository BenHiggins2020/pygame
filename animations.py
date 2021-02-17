import pygame
from classes import Player

class Man():
    def __init__(self,x,y,CameraX,CameraY):
        self.x = x
        self.y = y
        self.CameraX = CameraX
        self.CameraY = CameraY
        self.vel = 5
        self.idle = False
        #self.standing = pygame.image.load('018.png')
        self.standing = pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/018.png')
        self.attack = False
        self.die = False
        self.walk_right = True
        self.walkCount = 0
        self.walkrt = [pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/027.png'),
            pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/028.png'),
            pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/029.png'),
            pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/030.png'),
            pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/031.png'),
            pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/032.png'),
            pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/033.png'),
            pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/034.png'),
            pygame.image.load('C:/Users/Ben Higgins/Desktop/New folder - Copy/manwalk/035.png')]

    def draw(self,win):
        if self.walk_right:
            win.blit(self.walkrt[self.walkCount//3], (self.x - self.CameraX,self.y - self.CameraY))
        if self.idle:
          win.blit(self.standing, (self.x - self.CameraX, self.y - self.CameraY))
