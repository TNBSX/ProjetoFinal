# -*- coding: utf-8 -*-
"""
Created on Tue May 15 18:03:12 2018

@author: tiago
"""


# ఠిస్ ఐస్ ది బెస్ట్ గేమ్ ఎవర్, ది మోస్ట్ డిఫికల్ట్ వన

import pygame
import sys
from pygame.locals import *
from random import randrange
from matplotlib.pyplot import imread


GREEN = (0, 200, 0)
BLUE = (50, 50, 255)
width=800
height=600
contador = 0
<<<<<<< HEAD
velb = 0   # controlador de velocidade das bolinhas
=======
velb = 4   # controlador de velocidade das bolinhas
>>>>>>> 59b2d9e72d309d9bc759f3a10ad53b81fd0ffdfa

#############-------Classes------##############

class Square(pygame.sprite.Sprite):
    def _init_(self, Quadrado_imagem, pos_x, pos_y):
        pygame.sprite.Sprite._init_(self)
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
    def _init_(self, bolinha_imagem, pos_x2, pos_y2, vel_x, vel_y):
        pygame.sprite.Sprite._init_(self)
        
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
    def _init_(self, imagem_amarelo, pos_x2, pos_y2):
        pygame.sprite.Sprite._init_(self)
        
        self.image = pygame.image.load(imagem_amarelo)
        self.rect = self.image.get_rect() 
        
        self.rect.x = pos_x2
        self.rect.y = pos_y2
        
class Paredes(pygame.sprite.Sprite):
    def _init_(self, x, y, width, height):
        super()._init_()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        

class Zona_segura(pygame.sprite.Sprite):
    def _init_(self, x, y, width, height):
        super()._init_()
        self.image = pygame.Surface([width, height])
        #self.image.fill(GREEN)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Button(pygame.sprite.Sprite):
    def _init_(self, img, pos_x, pos_y):
        height, width, channels = imread(img).shape
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.x = [pos_x, pos_x + width]
        self.y = [pos_y, pos_y + height]

###########-------Inicialização------###########
        
pygame.init()

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((800, 600), 0, 32)
menu_jogo = pygame.image.load('TELA.png').convert()
menu_teste = pygame.transform.scale(menu_jogo, (width, height))
tela.blit(menu_teste, (0,0))

button = pygame.sprite.Group()
playb = "play.png"
quitb = "Exit_Button.png"
quita = Button(quitb, 400, 250)
play = Button(playb, 100, 250)
button.add(play)
button.add(quita)

menu = True

while menu:
    
    button.draw(tela)
    
    for event in pygame.event.get():  
        if pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0] == 1:
                if pygame.mouse.get_pos()[0] in range(play.x[0], play.x[1]) and pygame.mouse.get_pos()[1] in range(play.y[0], play.y[1]):
                    menu = False
                    rodando = True
                if pygame.mouse.get_pos()[0] in range(quita.x[0], quita.x[1]) and pygame.mouse.get_pos()[1] in range(quita.y[0], quita.y[1]):
                    menu = False
                    rodando = False
    
    pygame.display.update()        
        
pygame.mixer.init()
#tela = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption('O JOGO MAIS INSPER DO MUNDO')

# carrega imagem de fundo 
fundo = pygame.image.load("roxo-em-ingles.jpg").convert()

#cria zona segura
zona_group = pygame.sprite.Group()

#zona = Zona_segura(10, 200, 150, 200)
#zona_group.add(zona)

zona = Zona_segura(650, 250, 50, 100)
zona_group.add(zona)

# cria quadrado 
quadrado = Square("quadrado-vermelho-25X25.png", 150, 300)
quadrado_group = pygame.sprite.Group()
quadrado_group.add(quadrado)

# cria bolinha
bola_group = pygame.sprite.Group()

#=============Bolinhas do eixo Y=============

bola = Bolinha_assassina("bola-menor.png", 250, 400, 0,velb) #anda no Y 1 bolinha (da esquerda para direita)
bola_group.add(bola)

bola2 = Bolinha_assassina("bola-menor.png", 325, 100, 0,-velb) #anda no Y 2 bolinha (da esquerda para direita)
bola_group.add(bola2)

bola7 = Bolinha_assassina("bola-menor.png", 400, 400, 0, velb) #anda no Y 3 bolinha (da esquerda para direita)
bola_group.add(bola7)

bola8 = Bolinha_assassina("bola-menor.png", 475, 100, 0, -velb) #anda no Y 4 bolinha (da esquerda para direita)
bola_group.add(bola8)

bola5 = Bolinha_assassina("bola-menor.png", 550, 400, 0,velb) #anda no Y 5 bolinha (da esquerda para direita)
bola_group.add(bola5)

bola6 = Bolinha_assassina("bola-menor.png", 625, 100, 0,-velb) #anda no Y 6 bolinha (da esquerda para direita)
bola_group.add(bola6)

#============Bolinhas do eixo X================

#bola9 = Bolinha_assassina("bola-menor.png", 475, 50, velb, 0) #anda no X 1 MAIS EM CIMA
#bola_group.add(bola9)

bola4 = Bolinha_assassina("bola-menor.png", 175, 130, velb,0) #anda no X 2 bolinha (de cima para baixo)
bola_group.add(bola4)

bola11 = Bolinha_assassina("bola-menor.png", 475, 200, velb, 0) #anda no X 3 bolinha (de cima para baixo)
bola_group.add(bola11)

bola3 = Bolinha_assassina("bola-menor.png", 175, 390, velb, 0) #anda no X 4 bolinha (de cima para baixo)
bola_group.add(bola3)

bola12 = Bolinha_assassina("bola-menor.png", 475, 451, velb, 0) #anda no X 5 bolinha (de cima para baixo)
bola_group.add(bola12)

#bola10 = Bolinha_assassina("bola-menor.png", 475, 550, velb, 0) #anda no X 6 MAIS EM BAIXO
#bola_group.add(bola10) 


bolaP_group = pygame.sprite.Group()

# cria a bola que pega para ganhar o jogo
bolaP1 = Bolaquepega("amarelo-pega.png", 430 , 190)
bolaP_group.add(bolaP1)

bolaP2 = Bolaquepega("amarelo-pega.png", 430 , 390)
bolaP_group.add(bolaP2)

bolaP3 = Bolaquepega("amarelo-pega.png", 430 , 290)
bolaP_group.add(bolaP3)

# cria parede
parede_group = pygame.sprite.Group()
 
parede = Paredes(100, 100, 10, 400) #Parede da esquerda
parede_group.add(parede)

parede = Paredes(100, 100, 600, 10) #Parede de cima
parede_group.add(parede)

parede = Paredes(690, 100, 10, 400) #Parede da direita
parede_group.add(parede)

parede = Paredes(100, 490, 600, 10) #Parede de baixo 
parede_group.add(parede)


relogio = pygame.time.Clock()

coin = pygame.mixer.Sound("coin.wav")
#win =  pygame.mixer.Sound("bazinga.wav")
death = pygame.mixer.Sound("voldemort2.wav")

# ===============   LOOPING PRINCIPAL   ===============
#rodando = True
while rodando:
  tempo = relogio.tick(200)
    
  for event in pygame.event.get():  #pega lista de eventos
    if event.type == pygame.QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
      rodando = False            #executa a função de sistema "exit"
      
  for bolaq in bola_group:
            
    # Jogar bate no obstáculo 
    if pygame.sprite.collide_rect(quadrado, bolaq):       
        contador = 0 #Zera contagem, reiniciando jogo..  
        #Reset jogador
        quadrado.rect.x = 150
        quadrado.rect.y = 300

        #Rest marcador 1
        bolaP1.rect.x = 430
        bolaP1.rect.y = 190

        #Reset marcador 2
        bolaP2.rect.x = 430
        bolaP2.rect.y = 390
        
        #Reset marcador 3
        bolaP3.rect.x = 430
        bolaP3.rect.y = 290
        
        death.play(0)
        
    #Jogador colide com 1 o marcador
  if pygame.sprite.collide_rect(quadrado, bolaP1):
        
        #Esconde marcador 1 encontrado
        bolaP1.rect.x = 1000
        bolaP1.rect.y = 1000
        coin.play(0)
        contador += 1 #Adiciona ponto
        
    #Jogodor colide com 2 marcador...
  if pygame.sprite.collide_rect(quadrado, bolaP2):
        
        #Esconde marcador 2 encontrado
        bolaP2.rect.x = 1001
        bolaP2.rect.y = 1001
        coin.play(0)
        contador += 1 #Adiciona ponto
        
      #Jogodor colide com 3 marcador...
  if pygame.sprite.collide_rect(quadrado, bolaP3):
        
        #Esconde marcador 2 encontrado
        bolaP3.rect.x = 1002
        bolaP3.rect.y = 1002
        coin.play(0)
        contador += 1 #Adiciona ponto
        
  #if pygame.sprite.collide_rect(quadrado, parede):
      #quadrado = Square("quadrado-vermelho-25X25.png", pos_x, pos_y)
    
  #move o quadrado pela tela
  pressed_keys = pygame.key.get_pressed() #pega teclas pressionadas
  if pressed_keys[K_UP] and quadrado.rect.y > 110:
      quadrado.moveUp()
  if pressed_keys[K_DOWN] and quadrado.rect.y < 465:
      quadrado.moveDown() 
  if pressed_keys[K_LEFT] and quadrado.rect.x > 110:
      quadrado.moveLeft()
  if pressed_keys[K_RIGHT] and quadrado.rect.x < 665:
      quadrado.moveRight()

#move a bolinha
  bola.move3()
  if bola.rect.y < 100 or bola.rect.y > 475:
    bola.vy = - bola.vy 
    
  bola2.move3()
  if bola2.rect.y < 100 or bola2.rect.y > 475:
      bola2.vy = - bola2.vy
      
  bola3.move3()
  if bola3.rect.x < 100 or bola3.rect.x > 675:  ###
      bola3.vx = - bola3.vx
  
  bola4.move3()
  if bola4.rect.x < 100 or bola4.rect.x > 675:  ###
      bola4.vx = -bola4.vx 
     
  bola5.move3()
  if bola5.rect.y < 100 or bola5.rect.y > 475:
      bola5.vy = -bola5.vy

  bola6.move3()
  if bola6.rect.y < 100 or bola6.rect.y > 475:
      bola6.vy = -bola6.vy
      
  bola7.move3()
  if bola7.rect.y < 100 or bola7.rect.y > 475:
      bola7.vy = -bola7.vy

  bola8.move3()
  if bola8.rect.y < 100 or bola8.rect.y > 475:
      bola8.vy = -bola8.vy    
      
  #bola9.move3()
  #if bola9.rect.x < 100 or bola9.rect.x > 675:
   #   bola9.vx = -bola9.vx

  #bola10.move3()
  #if bola10.rect.x < 100 or bola10.rect.x > 675:
   #   bola10.vx = -bola10.vx
      
  bola11.move3()
  if bola11.rect.x < 100 or bola11.rect.x > 675:
      bola11.vx = -bola11.vx
      
  bola12.move3()
  if bola12.rect.x < 100 or bola12.rect.x > 675:
      bola12.vx = -bola12.vx
    
    
  # Caso a bolinha chegue na segunda zona, vc VENCE e o jogo fecha
  # FALTA AS BOLINHAS PARA PEGAR PELA FASE  
  # AINDA TEM QUE MELHORAR 
  # FALTA MENSAGEM DE VENCEU -- 1 FASE
  # MUDAR PARA A PRÓXIMA FASE CASO CHEGUE NA ZONA 2
  if contador == 3 and pygame.sprite.collide_rect(quadrado,zona):
      pygame.quit()
      sys.exit('temporary solution')


  #gera saídas
  tela.blit(fundo, (0, 0))
  zona_group.draw(tela)
  quadrado_group.draw(tela)
  bola_group.draw(tela)  #10x bolinhas moveis
  bolaP_group.draw(tela) #2x Marcador
  parede_group.draw(tela)
  
  pygame.display.update()     #coloca a tela na janela

pygame.display.quit()