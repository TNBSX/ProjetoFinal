# -*- coding: utf-8 -*-
"""
Created on Thu May 10 17:22:01 2018

@author: tiago
"""

import pygame
import sys
from pygame.locals import *
from random import randrange
from matplotlib.pyplot import imread

GREEN = (0, 200, 0)
BLUE = (50, 50, 255)
width=800
height=600
rodando = False

#############-------Classes------##############

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
        
    #def checkCollision(self, sprite1, sprite2):
        #col = pygame.sprite.collide_rect(sprite1, sprite2)
        #if col == True:
            #sys.exit()
            
class Bolinha_assassina(pygame.sprite.Sprite):
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
        

class Zona_segura(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        #self.image.fill(GREEN)
        
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


###########-------Inicialização------###########

pygame.init()

relogio = pygame.time.Clock()

tela2 = pygame.display.set_mode((800, 600), 0, 32)
menu_jogo = pygame.image.load("Menu.PNG").convert()
menu_teste = pygame.transform.scale(menu_jogo, (width, height))
tela2.blit(menu_teste, (0,0))

button = pygame.sprite.Group()
playb = ("play.png")
play = Button(playb, 350, 400)
button.add(play)
menu = True

while menu:
    
    button.draw(tela2)
    pygame.display.update()
    
    if pygame.mouse.get_pressed():
        if pygame.mouse.get_pressed()[0] == 1:
            if pygame.mouse.get_pos[0] in range (playb.x[0], playb.x[1]) and pygame.mouse.get_pos[1] in range (playb.y[0], playb.y[1]):
                menu = False
                rodando = True
    else:
        menu = True
    
# ===============   LOOPING PRINCIPAL   ===============

pygame.display.set_caption('O JOGO MAIS INSPER DO MUNDO')

# carrega imagem de fundo 
fundo = pygame.image.load("roxo-em-ingles.jpg").convert()

#cria zona segura
zona_group = pygame.sprite.Group()

#zona = Zona_segura(10, 200, 150, 200)
#zona_group.add(zona)

zona = Zona_segura(690, 200, 100, 200)
zona_group.add(zona)

# cria quadrado 
quadrado = Square("quadrado-vermelho-25X25.png", 25, 300)
quadrado_group = pygame.sprite.Group()
quadrado_group.add(quadrado)

# cria bolinha
bola_group = pygame.sprite.Group()

bola = Bolinha_assassina("bola-menor.png", 250, 500, 3)
bola_group.add(bola)

bola2 = Bolinha_assassina("bola-menor.png", 325, 100, -2)
bola_group.add(bola2)

bola3 = Bolinha_assassina("bola-menor.png", 400, 500, 3)
bola_group.add(bola3)

bola4 = Bolinha_assassina("bola-menor.png", 475, 100, -3)
bola_group.add(bola4)

bola5 = Bolinha_assassina("bola-menor.png", 550, 100, 2)
bola_group.add(bola5)

bola6 = Bolinha_assassina("bola-menor.png", 625, 100, -3)
bola_group.add(bola6)


# cria parede
parede_group = pygame.sprite.Group()
 
parede = Paredes(0, 0, 10, 600)
parede_group.add(parede)

parede = Paredes(0, 0, 800, 10)
parede_group.add(parede)

parede = Paredes(790, 0, 10, 600)
parede_group.add(parede)

parede = Paredes(0, 590, 800, 10)
parede_group.add(parede)


while rodando:
  tempo = relogio.tick(200)
    
  for event in pygame.event.get():  #pega lista de eventos
    if event.type == pygame.QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
      
  if pygame.sprite.collide_rect(quadrado,bola):
     quadrado = Square("quadrado-vermelho-25X25.png", 50, 300)
     quadrado_group = pygame.sprite.Group()
     quadrado_group.add(quadrado)
     
  if pygame.sprite.collide_rect(quadrado,bola2):
     quadrado = Square("quadrado-vermelho-25X25.png", 50, 300)
     quadrado_group = pygame.sprite.Group()
     quadrado_group.add(quadrado)
  
  if pygame.sprite.collide_rect(quadrado,bola3):
     quadrado = Square("quadrado-vermelho-25X25.png", 50, 300)
     quadrado_group = pygame.sprite.Group()
     quadrado_group.add(quadrado)  
    
  if pygame.sprite.collide_rect(quadrado,bola4):
     quadrado = Square("quadrado-vermelho-25X25.png", 50, 300)
     quadrado_group = pygame.sprite.Group()
     quadrado_group.add(quadrado)
    
  if pygame.sprite.collide_rect(quadrado,bola5):
     quadrado = Square("quadrado-vermelho-25X25.png", 50, 300)
     quadrado_group = pygame.sprite.Group()
     quadrado_group.add(quadrado)
     
  if pygame.sprite.collide_rect(quadrado,bola6):
     quadrado = Square("quadrado-vermelho-25X25.png", 50, 300)
     quadrado_group = pygame.sprite.Group()
     quadrado_group.add(quadrado)
     
  #if pygame.sprite.collide_rect(quadrado, parede):
      #quadrado = Square("quadrado-vermelho-25X25.png", pos_x, pos_y)
    
  #move o quadrado pela tela
  pressed_keys = pygame.key.get_pressed() #pega teclas pressionadas
  if pressed_keys[K_UP] and quadrado.rect.y > 10:
      quadrado.moveUp()
  elif pressed_keys[K_DOWN] and quadrado.rect.y < 565:
      quadrado.moveDown() 
  elif pressed_keys[K_LEFT] and quadrado.rect.x > 10:
      quadrado.moveLeft()
  elif pressed_keys[K_RIGHT] and quadrado.rect.x < 765:
      quadrado.moveRight() 


#move a bolinha
  bola.move3()
  if bola.rect.y < 10 or bola.rect.y > 565:
    bola.vy = - bola.vy 
    
  bola2.move3()
  if bola2.rect.y < 0 or bola2.rect.y > 565:
      bola2.vy = - bola2.vy
      
  bola3.move3()
  if bola3.rect.y < 10 or bola3.rect.y > 565:
      bola3.vy = - bola3.vy
  
  bola4.move3()
  if bola4.rect.y < 10 or bola4.rect.y > 565:
      bola4.vy = -bola4.vy  
     
  bola5.move3()
  if bola5.rect.y < 10 or bola5.rect.y > 565:
      bola5.vy = -bola5.vy

  bola6.move3()
  if bola6.rect.y < 10 or bola6.rect.y > 565:
      bola6.vy = -bola6.vy
    
    
  # Caso a bolinha chegue na segunda zona, vc VENCE e o jogo fecha
  # FALTA AS BOLINHAS PARA PEGAR PELA FASE  
  # AINDA TEM QUE MELHORAR 
  # FALTA MENSAGEM DE VENCEU -- 1 FASE
  # MUDAR PARA A PRÓXIMA FASE CASO CHEGUE NA ZONA 2
  if pygame.sprite.collide_rect(quadrado,zona):
      pygame.quit()
      sys.exit('temporary solution')


  #gera saídas
  tela.blit(fundo, (0, 0))
  quadrado_group.draw(tela)
  bola_group.draw(tela)
  parede_group.draw(tela)
  zona_group.draw(tela)
  pygame.display.update()     #coloca a tela na janela

pygame.display.quit()