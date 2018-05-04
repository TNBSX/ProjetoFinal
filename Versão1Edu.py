# -*- coding: utf-8 -*-
"""
Created on Fri May  4 07:45:39 2018

@author: eduar
"""
import pygame
import sys
from pygame.locals import *

#                   INICIALIZAÇÃO

pygame.init()
tela = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Jogo mais difícil do mundo')
fundo = pygame.image.load('fundo.png').convert()
tela.blit(fundo, (0, 0)) #linha 17 e
pygame.display.update()  #linha 18 devem ser depois movidas para o looping principal!!!!!
