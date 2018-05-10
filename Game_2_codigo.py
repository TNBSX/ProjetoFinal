# -*- coding: utf-8 -*-
"""
Created on Thu May 10 17:22:01 2018

@author: tiago
"""

import pygame
import sys
from pygame.locals import *
from random import randrange

BLUE = (50, 50, 255)
width=800
height=600


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
        
    #def checkCollision(self, sprite1, sprite2):
        #col = pygame.sprite.collide_rect(sprite1, sprite2)
        #if col == True:
            #sys.exit()
            
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


class Paredes(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    


###########-------Inicialização------###########
pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption('JOGO')

# carrega imagem de fundo 
fundo = pygame.image.load("fundo-800X600.jpg").convert()

# cria quadrado 
quadrado = square("quadrado-vermelho-25X25.png", 100, 300)
quadrado_group = pygame.sprite.Group()
quadrado_group.add(quadrado)

# cria bolinha
bola = bolinha_assassina("bola-20X20.png", 500, 500, 1)
#bola2 = bolinha_assassina2("bola-20X20.png", 700, 200, randrange(-1, 1))

bola_group = pygame.sprite.Group()
bola_group.add(bola)

#bola2_group = pygame.sprite.Group()
#bola2_group.add(bola2)

parede_group = pygame.sprite.Group()
 
parede = Paredes(0, 0, 10, 600)
parede_group.add(parede)

parede = Paredes(0, 0, 800, 10)
parede_group.add(parede)

parede = Paredes(790, 0, 10, 600)
parede_group.add(parede)

parede = Paredes(0, 590, 800, 10)
parede_group.add(parede)

relogio = pygame.time.Clock()


# ===============   LOOPING PRINCIPAL   ===============
rodando = True
while rodando:
  tempo = relogio.tick(200)
    
  for event in pygame.event.get():  #pega lista de eventos
    if event.type == pygame.QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
      
  if pygame.sprite.collide_rect(quadrado,bola):
     quadrado = square("quadrado-vermelho-25X25.png", 100, 300)
     quadrado_group = pygame.sprite.Group()
     quadrado_group.add(quadrado)
     
  #if pygame.sprite.collide_rect(quadrado, parede):
      #quadrado = square("quadrado-vermelho-25X25.png", pos_x, pos_y)
    
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
   

  #bola2.move4()
  #if bola.rect.x < 0 or bola.rect.x > 800:
  #    bola.vx = -bola.vx


  #gera saídas
  tela.blit(fundo, (0, 0))
  quadrado_group.draw(tela)
  bola_group.draw(tela)
  parede_group.draw(tela)
  #bola2_group.draw(tela)
  pygame.display.update()     #coloca a tela na janela

pygame.display.quit()