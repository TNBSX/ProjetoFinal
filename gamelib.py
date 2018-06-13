
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:44:58 2018

@author: tiago
"""

#############-------Classes------##############

import pygame
import sys
from pygame.locals import *
from random import randrange
from matplotlib.pyplot import imread

GREEN = (0, 200, 0)
BLUE = (50, 50, 255)
WHITE = (255,255,255)
width=800
height=600
contador = 0
velb = 4   # controlador de velocidade das bolinhas

mortes = 0

class Square(pygame.sprite.Sprite):
    def __init__(self, Quadrado_imagem, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        #self.x = pos_x
        #self.y = pos_y
        self.image = pygame.image.load(Quadrado_imagem)
        
        self.rect = self.image.get_rect() 
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.steps = 1
        
    
    def moveY(self, pixel):
        if self.rect.y >= 1 or pixel > 0:
            self.rect.y += pixel
        #elif self.rect.y <= 400 or pixel < 0:   #NAO FUNCIONA
        #    self.rect.y -= pixel  #NAO FUNCIONA


    def moveX(self, pixel2):
        if self.rect.x >= 1 or pixel2 > 0:
            self.rect.x += pixel2
        #elif self.rect.x <= 799 or pixel2 > 0:  #NAO FUNCIONA
        #    self.rect.x -= pixel2   #NAO FUNCIONA

    def moveDown(self):
        self.moveY(self.steps)
    
    def moveUp(self):
        self.moveY(-self.steps)
    
    def moveLeft(self):
        self.moveX(-self.steps)
    
    def moveRight(self):
        self.moveX(self.steps)
        
            
class Bolinha_assassina(pygame.sprite.Sprite):
    def __init__(self, bolinha_imagem, pos_x2, pos_y2, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(bolinha_imagem)
        
        self.rect = self.image.get_rect() 
        self.rect.x = pos_x2
        self.rect.y = pos_y2
        
    def move3(self):
        self.rect.y += self.vy
        self.rect.x += self.vx

class Bolaquepega(pygame.sprite.Sprite):
    def __init__(self, imagem_amarelo, pos_x2, pos_y2):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(imagem_amarelo)
        self.rect = self.image.get_rect() 
        
        self.rect.x = pos_x2
        self.rect.y = pos_y2
        
class Paredes(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        

class Zona_segura(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Button(pygame.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y):
        height, width, channels = imread(img).shape
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.x = [pos_x, pos_x + width]
        self.y = [pos_y, pos_y + height]