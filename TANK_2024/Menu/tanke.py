import pygame
class Tanke:
    def __init__(self,dc_game):
        self.screen = dc_game.screen
        self.screen_rect = dc_game.screen.get_rect()

        self.imagen = pygame.image.load('C:/Users/Usuario/Pictures/tanque1.png')
        


        self.rect = self.imagen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        

        self.moviendoIzquierda = False
        self.moviendoDerecha = False


    def blime(self):
        self.screen.blit(self.imagen,self.rect)



    def actualizar(self):
        if self.moviendoDerecha and self.rect.right < self.screen_rect.right:
            self.rect.x += 4
        if self.moviendoIzquierda and self.rect.left > 0:
            self.rect.x -= 4


