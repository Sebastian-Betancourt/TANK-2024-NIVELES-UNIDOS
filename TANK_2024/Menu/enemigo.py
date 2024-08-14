import pygame
from pygame.sprite import Sprite
import random
from disparo import balaEnemigo

class Enemigo(Sprite):
    def __init__(self,dc_game):
        super().__init__()
        self.dc_game= dc_game
        self.screen  = dc_game.screen

        self.image = pygame.image.load('C:/Users/Usuario/Pictures/tanque_enemigo.png')
        self.rect = self.image.get_rect()

        self.rect.y = self.rect.height-150 
        self.rect.x = random.randint(10,self.rect.width)*10
        self.ajustes = dc_game.ajustes
        self.y = float(self.rect.y)

    def update(self):
        self.rect.y += self.ajustes.velocidadEnemigo
        self.y += self.ajustes.velocidadEnemigo  
        self.rect.y = self.y  

    def dispararBala(self):
        nuevaBala = balaEnemigo(self.dc_game, self.rect.centerx, self.rect.bottom)
        self.dc_game.balasEnemigo.add(nuevaBala)
        