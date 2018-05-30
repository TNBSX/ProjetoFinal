# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:17:12 2018

@author: tiago
"""

import pygame
import sys
from pygame.locals import *
from random import randrange
from matplotlib.pyplot import imread
import gamelib as gl

GREEN = (0, 200, 0)
BLUE = (50, 50, 255)
WHITE = (255,255,255)
width=800
height=600
contador = 0
velb = 4   # controlador de velocidade das bolinhas
mortes = 0

###########-------Inicialização------###########

pygame.init()

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((800, 600), 0, 32)
menu_jogo = pygame.image.load("TELA.PNG").convert()
menu_teste = pygame.transform.scale(menu_jogo, (width, height))
tela.blit(menu_teste, (0,0))

button = pygame.sprite.Group()
playb = "play.png"
quitb = "Exit_Button.png"
quita = gl.Button(quitb, 400, 250)
play = gl.Button(playb, 100, 250)
button.add(play)
button.add(quita)


#pygame.init()
pygame.mixer.init()
#tela = pygame.display.set_mode((800, 600), 0, 32)

pygame.display.set_caption('O JOGO MAIS INSPER DO MUNDO')

# carrega imagem de fundo 
fundo = pygame.image.load("roxo-em-ingles.jpg").convert()

#Fasen3
def Fase3():
    global rodando3
    WHITE = (255,255,255)
    contador = 0
    velb = 3   # controlador de velocidade das bolinhas
    mortes = 0
    
    rodando3 = True
    #cria zona segura
    zona_group = pygame.sprite.Group()

    #zona = Zona_segura(10, 200, 150, 200)
    #zona_group.add(zona)
    
    zona = gl.Zona_segura(740, 10, 50, 100)
    zona_group.add(zona)
    
    # cria quadrado 
    quadrado = gl.Square("quadrado-vermelho-25X25.png", 75, 520)
    quadrado_group = pygame.sprite.Group()
    quadrado_group.add(quadrado)
    
    # cria bolinha
    bola_group = pygame.sprite.Group()

    #=============Bolinhas do eixo Y=============
    
    bola = gl.Bolinha_assassina("bola-menor.png", 250, 125,velb, 0) #anda no Y 1 bolinha (da esquerda para direita)
    bola_group.add(bola)
    
    bola2 = gl.Bolinha_assassina("bola-menor.png", 200, 155, 0, velb) #anda no Y 2 bolinha (da esquerda para direita)
    bola_group.add(bola2)
    
    bola7 = gl.Bolinha_assassina("bola-menor.png", 400, 185, velb, 0) #anda no Y 3 bolinha (da esquerda para direita)
    bola_group.add(bola7)
    
    bola8 = gl.Bolinha_assassina("bola-menor.png", 275, 215, 0, velb) #anda no Y 4 bolinha (da esquerda para direita)
    bola_group.add(bola8)
    
    bola5 = gl.Bolinha_assassina("bola-menor.png", 550, 245,velb, 0) #anda no Y 5 bolinha (da esquerda para direita)
    bola_group.add(bola5)
    
    bola6 = gl.Bolinha_assassina("bola-menor.png", 350, 275, 0, velb) #anda no Y 6 bolinha (da esquerda para direita)
    bola_group.add(bola6)
    
    #============Bolinhas do eixo X================
    
    bola9 = gl.Bolinha_assassina("bola-menor.png", 425, 50, 0, velb) #anda no X 1 MAIS EM CIMA
    bola_group.add(bola9)
    
    bola4 = gl.Bolinha_assassina("bola-menor.png", 75, 305, velb,0) #anda no X 2 bolinha (de cima para baixo)
    bola_group.add(bola4)
    
    #bola11 = Bolinha_assassina("bola-menor.png", 575, 335, velb, 0) #anda no X 3 bolinha (de cima para baixo)
    #bola_group.add(bola11)
    
    bola3 = gl.Bolinha_assassina("bola-menor.png", 575, 365, velb, 0) #anda no X 4 bolinha (de cima para baixo)
    bola_group.add(bola3)
    
    bola12 = gl.Bolinha_assassina("bola-menor.png", 500, 395, 0, velb) #anda no X 5 bolinha (de cima para baixo)
    bola_group.add(bola12)
    
    bola10 = gl.Bolinha_assassina("bola-menor.png", 550, 425, velb, 0) #anda no X 6 MAIS EM BAIXO
    bola_group.add(bola10) 
    
    bola11 = gl.Bolinha_assassina("bola-menor.png", 550, 485, velb, 0)
    bola_group.add(bola11)
    
    bolaP_group = pygame.sprite.Group()
    
    # cria a bola que pega para ganhar o jogo
    bolaP1 = gl.Bolaquepega("amarelo-pega.png", 200 , 200)
    bolaP_group.add(bolaP1)
    
    bolaP2 = gl.Bolaquepega("amarelo-pega.png", 600 , 390)
    bolaP_group.add(bolaP2)
    
    bolaP3 = gl.Bolaquepega("amarelo-pega.png", 400 , 290)
    bolaP_group.add(bolaP3)
    
    bolaP4 = gl.Bolaquepega("amarelo-pega.png", 650 , 520)
    bolaP_group.add(bolaP4)
    
    # cria parede
    parede_group = pygame.sprite.Group()
     
    parede = gl.Paredes(0, 0, 10, 600) #Parede da esquerda
    parede_group.add(parede)
    
    parede = gl.Paredes(0, 0, 800, 10) #Parede de cima
    parede_group.add(parede)
    
    parede = gl.Paredes(790, 0, 10, 600) #Parede da direita
    parede_group.add(parede)
    
    parede = gl.Paredes(0, 590, 800, 10) #Parede de baixo
    parede_group.add(parede)
    
    
    tela.fill(WHITE)
    myfont = pygame.font.SysFont("monospace", 16)
    morte_texto = myfont.render("Mortes = " +str(mortes), 1, (0,0,0))
    
    
    relogio = pygame.time.Clock()
    coin = pygame.mixer.Sound("coin.wav")
    death = pygame.mixer.Sound("voldemort2.wav")
    # ===============   LOOPING PRINCIPAL   ===============
    
    while rodando3:
      tempo = relogio.tick(20)
        
      for event in pygame.event.get():  #pega lista de eventos
        if event.type == pygame.QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
          rodando3 = False            #executa a função de sistema "exit"
          
      for bolaq in bola_group:
                
            # Jogar bate no obstáculo 
            if pygame.sprite.collide_rect(quadrado, bolaq):       
                contador = 0 #Zera contagem, reiniciando jogo..  
                #Reset jogador
                quadrado.rect.x = 75
                quadrado.rect.y = 520
        
                #Rest marcador 1
                bolaP1.rect.x = 200
                bolaP1.rect.y = 200
        
                #Reset marcador 2
                bolaP2.rect.x = 600
                bolaP2.rect.y = 390
                
                #Reset marcador 3
                bolaP3.rect.x = 400
                bolaP3.rect.y = 290
                
                #Reset marcador 4
                bolaP4.rect.x = 650
                bolaP4.rect.y = 520
                
                morte_texto = myfont.render("Mortes = " +str(mortes+1), 1, (0,0,0))
                mortes += 1 #
                
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
                
                #Jogodor colide com 4 marcador..
            if pygame.sprite.collide_rect(quadrado, bolaP4):
                
                  #Esconde marcador 2 encontrado
                  bolaP4.rect.x = 1003
                  bolaP4.rect.y = 1003
                  coin.play(0)
                  contador += 1 #Adiciona ponto
                
          #if pygame.sprite.collide_rect(quadrado, parede):
              #quadrado = Square("quadrado-vermelho-25X25.png", pos_x, pos_y)
            
            #move o quadrado pela tela
            pressed_keys = pygame.key.get_pressed() #pega teclas pressionadas
            if pressed_keys[K_UP] and quadrado.rect.y > 10:
                quadrado.moveUp()
            if pressed_keys[K_DOWN] and quadrado.rect.y < 565:
                quadrado.moveDown() 
            if pressed_keys[K_LEFT] and quadrado.rect.x > 10:
                quadrado.moveLeft()
            if pressed_keys[K_RIGHT] and quadrado.rect.x < 765:
                quadrado.moveRight()
        
          #move a bolinha
            bola.move3()
            if bola.rect.x < 10 or bola.rect.x > 775:
                bola.vx = -bola.vx 
            
            bola2.move3()
            if bola2.rect.y < 10 or bola2.rect.y > 575:
                bola2.vy = -bola2.vy
              
            bola3.move3()
            if bola3.rect.x < 10 or bola3.rect.x > 775:  ###
                bola3.vx = - bola3.vx
          
            bola4.move3()
            if bola4.rect.x < 10 or bola4.rect.x > 775:  ###
                bola4.vx = -bola4.vx 
             
            bola5.move3()
            if bola5.rect.x < 10 or bola5.rect.x > 775:
                bola5.vx = -bola5.vx 
        
            bola6.move3()
            if bola6.rect.y < 10 or bola6.rect.y > 575:
                bola6.vy = -bola6.vy
              
            bola7.move3()
            if bola7.rect.x < 10 or bola7.rect.x > 775:
                bola7.vx = -bola7.vx 
        
            bola8.move3()
            if bola8.rect.y < 10 or bola8.rect.y > 575:
                bola8.vy = -bola8.vy 
              
            bola9.move3()
            if bola9.rect.y < 10 or bola9.rect.y > 575:
                bola9.vy = -bola9.vy
        
            bola10.move3()
            if bola10.rect.x < 10 or bola10.rect.x > 775:
                bola10.vx = -bola10.vx
              
            bola11.move3()
            if bola11.rect.x < 10 or bola11.rect.x > 775:
                bola11.vx = -bola11.vx
              
            bola12.move3()
            if bola12.rect.y < 10 or bola12.rect.y > 575:
                bola12.vy = -bola12.vy
            
            
          # FALTA MENSAGEM DE VENCEU -- 1 FASE
          # MUDAR PARA A PRÓXIMA FASE CASO CHEGUE NA ZONA 2
            if contador == 4 and pygame.sprite.collide_rect(quadrado,zona):
                pygame.quit()
                sys.exit('temporary solution')
        
        
            #gera saídas
            tela.blit(fundo, (0, 0))
            zona_group.draw(tela)
            quadrado_group.draw(tela)
            bola_group.draw(tela)  #10x bolinhas moveis
            bolaP_group.draw(tela) #2x Marcador
            parede_group.draw(tela)
            tela.blit(morte_texto, (10,10))
          
            pygame.display.update()     #coloca a tela na janela
        
    pygame.display.quit()
    
    
#Fase 2
def Fase2():
    global rodando2
    WHITE = (255,255,255)
    contador = 0
    velb = 4 # controlador de velocidade das bolinhas
    mortes = 0

    #zona = Zona_segura(10, 200, 150, 200)
    #zona_group.add(zona)
    
    rodando2 = True
    #cria zona segura
    zona_group = pygame.sprite.Group()
    
    #zona = Zona_segura(10, 200, 150, 200)
    #zona_group.add(zona)
    
    zona = gl.Zona_segura(740, 10, 50, 100)
    zona_group.add(zona)
    
    # cria quadrado 
    quadrado = gl.Square("quadrado-vermelho-25X25.png", 75, 500)
    quadrado_group = pygame.sprite.Group()
    quadrado_group.add(quadrado)
    
    # cria bolinha
    bola_group = pygame.sprite.Group()
    
    #=============Bolinhas do eixo Y=============
    
    bola = gl.Bolinha_assassina("bola-menor.png", 250, 125,velb, 0) #anda no Y 1 bolinha (da esquerda para direita)
    bola_group.add(bola)
    
    #bola2 = Bolinha_assassina("bola-menor.png", 325, 155,-velb, 0) #anda no Y 2 bolinha (da esquerda para direita)
    #bola_group.add(bola2)
    
    bola7 = gl.Bolinha_assassina("bola-menor.png", 400, 185, velb, 0) #anda no Y 3 bolinha (da esquerda para direita)
    bola_group.add(bola7)
    
    #bola8 = Bolinha_assassina("bola-menor.png", 475, 215,-velb, 0) #anda no Y 4 bolinha (da esquerda para direita)
    #bola_group.add(bola8)
    
    bola5 = gl.Bolinha_assassina("bola-menor.png", 550, 245,velb, 0) #anda no Y 5 bolinha (da esquerda para direita)
    bola_group.add(bola5)
    
    #bola6 = Bolinha_assassina("bola-menor.png", 625, 275,-velb, 0) #anda no Y 6 bolinha (da esquerda para direita)
    #bola_group.add(bola6)
    
    #============Bolinhas do eixo X================
    
    #bola9 = Bolinha_assassina("bola-menor.png", 475, 50, velb, 0) #anda no X 1 MAIS EM CIMA
    #bola_group.add(bola9)
    
    bola4 = gl.Bolinha_assassina("bola-menor.png", 75, 305, velb,0) #anda no X 2 bolinha (de cima para baixo)
    bola_group.add(bola4)
    
    #bola11 = Bolinha_assassina("bola-menor.png", 575, 335, velb, 0) #anda no X 3 bolinha (de cima para baixo)
    #bola_group.add(bola11)
    
    bola3 = gl.Bolinha_assassina("bola-menor.png", 575, 365, velb, 0) #anda no X 4 bolinha (de cima para baixo)
    bola_group.add(bola3)
    
    #bola12 = Bolinha_assassina("bola-menor.png", 575, 395, velb, 0) #anda no X 5 bolinha (de cima para baixo)
    #bola_group.add(bola12)
    
    bola10 = gl.Bolinha_assassina("bola-menor.png", 550, 425, velb, 0) #anda no X 6 MAIS EM BAIXO
    bola_group.add(bola10) 
    
    
    bolaP_group = pygame.sprite.Group()
    
    # cria a bola que pega para ganhar o jogo
    bolaP1 = gl.Bolaquepega("amarelo-pega.png", 430 , 190)
    bolaP_group.add(bolaP1)
    
    bolaP2 = gl.Bolaquepega("amarelo-pega.png", 430 , 390)
    bolaP_group.add(bolaP2)
    
    bolaP3 = gl.Bolaquepega("amarelo-pega.png", 430 , 290)
    bolaP_group.add(bolaP3)
    
    # cria parede
    parede_group = pygame.sprite.Group()
     
    parede = gl.Paredes(0, 0, 10, 600) #Parede da esquerda
    parede_group.add(parede)
    
    parede = gl.Paredes(0, 0, 800, 10) #Parede de cima
    parede_group.add(parede)
    
    parede = gl.Paredes(790, 0, 10, 600) #Parede da direita
    parede_group.add(parede)
    
    parede = gl.Paredes(0, 590, 800, 10) #Parede de baixo
    parede_group.add(parede)
    
    
    tela.fill(WHITE)
    myfont = pygame.font.SysFont("monospace", 16)
    morte_texto = myfont.render("Mortes = " +str(mortes), 1, (0,0,0))
    
    
    relogio = pygame.time.Clock()
    coin = pygame.mixer.Sound("coin.wav")
    death = pygame.mixer.Sound("voldemort2.wav")
    
    while rodando2:
        tempo = relogio.tick(30)
    
        for event in pygame.event.get():  #pega lista de eventos
            if event.type == pygame.QUIT:      #verifica se um dos eventso é QUIT (janela fechou)
                rodando2 = False            #executa a função de sistema "exit"
        
        for bolaq in bola_group:
            
            # Jogar bate no obstáculo 
            if pygame.sprite.collide_rect(quadrado, bolaq):       
                contador = 0 #Zera contagem, reiniciando jogo..  
                #Reset jogador
                quadrado.rect.x = 75
                quadrado.rect.y = 500
    
                #Rest marcador 1
                bolaP1.rect.x = 430
                bolaP1.rect.y = 190
    
                #Reset marcador 2
                bolaP2.rect.x = 430
                bolaP2.rect.y = 390
            
                #Reset marcador 3
                bolaP3.rect.x = 430
                bolaP3.rect.y = 290
    
                morte_texto = myfont.render("Mortes = " +str(mortes+1), 1, (0,0,0))
                mortes += 1 #
            
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
            pressed_keys2 = pygame.key.get_pressed() #pega teclas pressionadas
            if pressed_keys2[K_UP] and quadrado.rect.y > 10:
                quadrado.moveUp()
            if pressed_keys2[K_DOWN] and quadrado.rect.y < 565:
                quadrado.moveDown() 
            if pressed_keys2[K_LEFT] and quadrado.rect.x > 10:
                quadrado.moveLeft()
            if pressed_keys2[K_RIGHT] and quadrado.rect.x < 765:
                quadrado.moveRight()

        #move a bolinha
            bola.move3()
            if bola.rect.x < 10 or bola.rect.x > 775:
                bola.vx = -bola.vx 
        
      #bola2.move3()
      #if bola2.rect.x < 10 or bola2.rect.x > 775:
      #    bola2.vx = -bola2.vx
          
            bola3.move3()
            if bola3.rect.x < 10 or bola3.rect.x > 775:  ###
                bola3.vx = - bola3.vx
      
            bola4.move3()
            if bola4.rect.x < 10 or bola4.rect.x > 775:  ###
                bola4.vx = -bola4.vx 
         
            bola5.move3()
            if bola5.rect.x < 10 or bola5.rect.x > 775:
                bola5.vx = -bola5.vx 
     
      #bola6.move3()
      #if bola6.rect.x < 10 or bola6.rect.x > 775:
      #    bola6.vx = -bola6.vx 
          
            bola7.move3()
            if bola7.rect.x < 10 or bola7.rect.x > 775:
                bola7.vx = -bola7.vx 
    
          #bola8.move3()
          #if bola8.rect.x < 10 or bola8.rect.x > 775:
          #    bola8.vx = -bola8.vx 
          
      #bola9.move3()
      #if bola9.rect.x < 100 or bola9.rect.x > 675:
       #   bola9.vx = -bola9.vx
    
            bola10.move3()
            if bola10.rect.x < 10 or bola10.rect.x > 775:
                bola10.vx = -bola10.vx
          
      #bola11.move3()
      #if bola11.rect.x < 10 or bola11.rect.x > 775:
      #    bola11.vx = -bola11.vx
          
      #bola12.move3()
      #if bola12.rect.x < 10 or bola12.rect.x > 775:
      #    bola12.vx = -bola12.vx
        
        
      # FALTA MENSAGEM DE VENCEU -- 1 FASE
      # MUDAR PARA A PRÓXIMA FASE CASO CHEGUE NA ZONA 2
            if contador == 3 and pygame.sprite.collide_rect(quadrado,zona):
                rodando2 = False
                Fase3()
    
    
      #gera saídas
            tela.blit(fundo, (0, 0))
            zona_group.draw(tela)
            quadrado_group.draw(tela)
            bola_group.draw(tela)  #10x bolinhas moveis
            bolaP_group.draw(tela) #2x Marcador
            parede_group.draw(tela)
            tela.blit(morte_texto, (10,10))
       
            pygame.display.update()     #coloca a tela na janela
    
    #pygame.display.quit()
            
#Fase1
def Fase1():
    global rodando
    print('Fase 1...')
    WHITE = (255,255,255)
    contador = 0
    velb = 1   # controlador de velocidade das bolinhas
    mortes = 0
    zona_group = pygame.sprite.Group()
    
    #zona = Zona_segura(10, 200, 150, 200)
    #zona_group.add(zona)
    
    zona = gl.Zona_segura(650, 250, 50, 100)
    zona_group.add(zona)
    
    # cria quadrado 
    quadrado = gl.Square("quadrado-vermelho-25X25.png", 150, 300)
    quadrado_group = pygame.sprite.Group()
    quadrado_group.add(quadrado)
    
    # cria bolinha
    bola_group = pygame.sprite.Group()
    
    #=============Bolinhas do eixo Y=============
    
    bola = gl.Bolinha_assassina("bola-menor.png", 250, 400, 0,velb) #anda no Y 1 bolinha (da esquerda para direita)
    bola_group.add(bola)
    
    bola2 = gl.Bolinha_assassina("bola-menor.png", 325, 100, 0,-velb) #anda no Y 2 bolinha (da esquerda para direita)
    bola_group.add(bola2)
    
    bola7 = gl.Bolinha_assassina("bola-menor.png", 400, 400, 0, velb) #anda no Y 3 bolinha (da esquerda para direita)
    bola_group.add(bola7)
    
    bola8 = gl.Bolinha_assassina("bola-menor.png", 475, 100, 0, -velb) #anda no Y 4 bolinha (da esquerda para direita)
    bola_group.add(bola8)
    
    bola5 = gl.Bolinha_assassina("bola-menor.png", 550, 400, 0,velb) #anda no Y 5 bolinha (da esquerda para direita)
    bola_group.add(bola5)
    
    bola6 = gl.Bolinha_assassina("bola-menor.png", 625, 100, 0,-velb) #anda no Y 6 bolinha (da esquerda para direita)
    bola_group.add(bola6)
    
    #============Bolinhas do eixo X================
    
    #bola9 = Bolinha_assassina("bola-menor.png", 475, 50, velb, 0) #anda no X 1 MAIS EM CIMA
    #bola_group.add(bola9)
    
    bola4 = gl.Bolinha_assassina("bola-menor.png", 175, 130, velb,0) #anda no X 2 bolinha (de cima para baixo)
    bola_group.add(bola4)
    
    bola11 = gl.Bolinha_assassina("bola-menor.png", 475, 200, velb, 0) #anda no X 3 bolinha (de cima para baixo)
    bola_group.add(bola11)
    
    bola3 = gl.Bolinha_assassina("bola-menor.png", 175, 390, velb, 0) #anda no X 4 bolinha (de cima para baixo)
    bola_group.add(bola3)
    
    bola12 = gl.Bolinha_assassina("bola-menor.png", 475, 451, velb, 0) #anda no X 5 bolinha (de cima para baixo)
    bola_group.add(bola12)
    
    #bola10 = Bolinha_assassina("bola-menor.png", 475, 550, velb, 0) #anda no X 6 MAIS EM BAIXO
    #bola_group.add(bola10) 
    
    
    bolaP_group = pygame.sprite.Group()
    
    # cria a bola que pega para ganhar o jogo
    bolaP1 = gl.Bolaquepega("amarelo-pega.png", 430 , 190)
    bolaP_group.add(bolaP1)
    
    bolaP2 = gl.Bolaquepega("amarelo-pega.png", 430 , 390)
    bolaP_group.add(bolaP2)
    
    bolaP3 = gl.Bolaquepega("amarelo-pega.png", 430 , 290)
    bolaP_group.add(bolaP3)
    
    # cria parede
    parede_group = pygame.sprite.Group()
     
    parede = gl.Paredes(100, 100, 10, 400) #Parede da esquerda
    parede_group.add(parede)
    
    parede = gl.Paredes(100, 100, 600, 10) #Parede de cima
    parede_group.add(parede)
    
    parede = gl.Paredes(690, 100, 10, 400) #Parede da direita
    parede_group.add(parede)
    
    parede = gl.Paredes(100, 490, 600, 10) #Parede de baixo
    parede_group.add(parede)
    
    
    tela.fill(WHITE)
    myfont = pygame.font.SysFont("monospace", 16)
    morte_texto = myfont.render("Mortes = " +str(mortes), 1, (0,0,0))
    
    relogio = pygame.time.Clock()
    
    coin = pygame.mixer.Sound("coin.wav")
    #win =  pygame.mixer.Sound("bazinga.wav")
    death = pygame.mixer.Sound("voldemort2.wav")

    while rodando:
            tempo = relogio.tick(30)
        
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
                    
                    morte_texto = myfont.render("Mortes = " +str(mortes+1), 1, (0,0,0))
                    mortes += 1 #
                    
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
                    #pygame.quit()
                    #sys.exit('temporary solution')
                    Fase2()
                    rodando = False

              #gera saídas
                tela.blit(fundo, (0, 0))
                zona_group.draw(tela)
                quadrado_group.draw(tela)
                bola_group.draw(tela)  #10x bolinhas moveis
                bolaP_group.draw(tela) #2x Marcador
                parede_group.draw(tela)
                tela.blit(morte_texto, (10,10))
              
                pygame.display.update()     #coloca a tela na janela
   
menu = True

while menu:
    
    button.draw(tela)
    
    for event in pygame.event.get():  
        if pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0] == 1:
                if pygame.mouse.get_pos()[0] in range(play.x[0], play.x[1]) and pygame.mouse.get_pos()[1] in range(play.y[0], play.y[1]):
                    menu = False
                    rodando = True
                    Fase1()
                    rodando2 = True
                    Fase2()
                    rodando3 = True
                    Fase3()
                if pygame.mouse.get_pos()[0] in range(quita.x[0], quita.x[1]) and pygame.mouse.get_pos()[1] in range(quita.y[0], quita.y[1]):
                    menu = False
                    rodando = False
                    rodando2 = False
                    rodando3 = False
                    pygame.quit()
                    sys.exit('temporary solution')

    pygame.display.update()