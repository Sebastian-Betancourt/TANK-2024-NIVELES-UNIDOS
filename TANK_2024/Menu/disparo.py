from typing import Any
import pygame
from pygame.sprite import Sprite

class Bala(Sprite):
    def __init__(self, dc_game):
        super().__init__()
        self.screen = dc_game.screen
        self.ajustes = dc_game.ajustes
        self.color = self.ajustes.colorBala

        self.rect = pygame.Rect(0,0,self.ajustes.anchuraBala,self.ajustes.alturaBala)
        self.rect.midtop = dc_game.tanke.rect.midtop

        self.y = float(self.rect.y)
    
    def update(self):
        self.y -= self.ajustes.velocidadBala
        self.rect.y = self.y 
    
    def pintarDisparo(self):
        pygame.draw.rect(self.screen,self.color,self.rect)


class balaEnemigo(Sprite):
    def __init__(self,dc_game,x,y):
        super().__init__()
        self.screen = dc_game.screen
        self.ajustes = dc_game.ajustes
        self.color = self.ajustes.colorBala
        self.rect = pygame.Rect (x,y,self.ajustes.anchuraBala, self.ajustes.alturaBala)

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.ajustes.velocidadBalaEnemiga
        self.rect.y = self.y
        
        if self.rect.bottom >= self.ajustes.altura:
            self.kill()
    
    def pintarDisparo(self):
        pygame.draw.rect(self.screen,self.color,self.rect)