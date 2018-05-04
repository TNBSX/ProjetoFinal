# -*- coding: utf-8 -*-
"""
Created on Fri May  4 07:46:37 2018

@author: tiago
"""

import pygame
import sys
from pygame.locals import *
from random import randrange


#############-------Classes------##############

class square(pygame.sprite.Sprite):
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
        if self.rect.y >= 1 or pixel > 0 and self.rect.y <= 599 or pixel < 0:
            self.rect.y += pixel

    def moveX(self, pixel2):
        if self.rect.x >= 1 or pixel2 > 0:
            self.rect.x += pixel2
        if self.rect.x <= 799 or pixel2 < 0:
            self.rect.x += pixel2

    def moveDown(self):
        self.moveY(self.steps)
    
    def moveUp(self):
        self.moveY(-self.steps)
            
    
    def moveLeft(self):
        self.moveX(-self.steps)
    
    def moveRight(self):
        self.moveX(self.steps)
        
class bolinha_assassina(pygame.sprite.Sprite):
    def __init__(self, bolinha_imagem, pos_x2, pos_y2, vel_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.vy = vel_y
        self.image = pygame.image.load(bolinha_imagem)
        
        self.rect = self.image.get_rect() 
        self.rect.x = pos_x2
        self.rect.y = pos_y2
        
    def move3(self):
        self.rect.y += self.vy
        


###########-------Inicialização------###########
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption('JOGO')

# carrega imagem de fundo 
fundo = pygame.image.load("fundo-800X600.jpg").convert()

# cria quadrado 
quadrado = square("quadrado-vermelho-33x33.png", 100, 300)
quadrado_group = pygame.sprite.Group()
quadrado_group.add(quadrado)

# cria bolinha
bola = bolinha_assassina("bola-20X20.png", randrange(800),randrange(600), randrange(-1,1))
bola2 = bolinha_assassina("bola-20X20.png", randrange(800),randrange(600), randrange(-1,1))

bola_group = pygame.sprite.Group()
bola_group.add(bola)

# ===============   LOOPING PRINCIPAL   ===============
rodando = True
while rodando:
  
  for event in pygame.event.get():  #pega lista de eventos
    if event.type == QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
  
  #move o quadrado pela tela
  pressed_keys = pygame.key.get_pressed() #pega teclas pressionadas
  if pressed_keys[K_UP]:
      quadrado.moveUp()
  elif pressed_keys[K_DOWN]:
      quadrado.moveDown() 
  elif pressed_keys[K_LEFT]:
      quadrado.moveLeft()
  elif pressed_keys[K_RIGHT]:
      quadrado.moveRight()

       
      
#move a bolinha
  bola.move3()
  if bola.rect.y < 0 or bola.rect.y > 600:
    bola.vy = - bola.vy  


  #gera saídas
  tela.blit(fundo, (0, 0))
  quadrado_group.draw(tela)
  bola_group.draw(tela)
  pygame.display.update()     #coloca a tela na janela

pygame.display.quit()














