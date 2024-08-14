import pygame
import sys
import random
from ajustes import Ajustes
from tanke import Tanke
from disparo import Bala
from enemigo import Enemigo

class Nivel2:
    def __init__(self):
        pygame.init()
        self.ajustes = Ajustes()
        self.screen = pygame.display.set_mode((self.ajustes.anchura, self.ajustes.altura))
        self.fondo = pygame.image.load(self.ajustes.fondo)
        pygame.display.set_caption("TANK 2024")
        self.tanke = Tanke(self)
        self.balas = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.balasEnemigo = pygame.sprite.Group()
        self.puntuacionJugador = 0
        self.salud = self.ajustes.vidaJugador
        self.enemigosHuir = self.ajustes.enemigosQuePuedenHuir 
        self.pausado = False
        self.puntuaciones_anteriores = []

    def mostrar_menu(self):
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 0, 0))
            fuente = pygame.font.SysFont("serif", 72)
            titulo_texto = fuente.render("TANK 2024", True, (255, 255, 255))
            titulo_rect = titulo_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 4))
            self.screen.blit(titulo_texto, titulo_rect)

            fuente_opciones = pygame.font.SysFont("serif", 56)
            jugar_texto = fuente_opciones.render("Jugar", True, (0, 255, 0))
            jugar_rect = jugar_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2))
            self.screen.blit(jugar_texto, jugar_rect)

            salir_texto = fuente_opciones.render("Salir", True, (255, 0, 0))
            salir_rect = salir_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 + 100))
            self.screen.blit(salir_texto, salir_rect)

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if jugar_rect.collidepoint(mouse) and click[0] == 1:
                menu = False  
            if salir_rect.collidepoint(mouse) and click[0] == 1:
                sys.exit()

            pygame.display.update()

    def enviarEnemigos(self):
        if len(self.enemigos) < 5 and random.randint(1, 100) <= self.ajustes.probabilidadEnviarEnemigo:
            tankeMalvado = Enemigo(self)
            self.enemigos.add(tankeMalvado)

    def eliminarEnemigosViejos(self):
        for enemigo in self.enemigos.copy():
            if enemigo.rect.bottom >= self.ajustes.altura:
                self.enemigos.remove(enemigo)
                self.enemigosHuir -= 1
                self.estaMuerto()
                self.enviarEnemigos()

    def actualizarEnemigos(self):
        self.enemigos.update()

    def colisionBalaNuestra(self):
        colision = pygame.sprite.groupcollide(self.balas, self.enemigos, True, True)
        if len(colision) != 0:
            self.puntuacionJugador += 10
            self.enemigosHuir += 1

    def colisionParaJugador(self):
        colisionEnemigo = pygame.sprite.spritecollide(self.tanke, self.enemigos, True)
        colisionBalaEnemiga = pygame.sprite.spritecollide(self.tanke, self.balasEnemigo, True)
        if len(colisionBalaEnemiga) != 0 or len(colisionEnemigo) != 0:
            self.salud -= 1
            self.estaMuerto()

    def dispararEnemigo(self):
        for enemigo in self.enemigos:
            if random.randint(1, 100) <= self.ajustes.probabilidadDisparo:
                enemigo.dispararBala()

    def estaMuerto(self):
        if self.salud <= 0 or self.enemigosHuir <= 0:
            self.mostrar_mensaje_final()
            self.opciones_final()

    def mostrar_mensaje_final(self):
        self.screen.fill((0, 0, 0))
        fuente = pygame.font.SysFont("serif", 56)
    
        mensaje_perdida = fuente.render("¡Perdiste!", True, (255, 0, 0))
        rect_mensaje = mensaje_perdida.get_rect()
        rect_mensaje.center = (self.ajustes.anchura // 2, self.ajustes.altura // 2 - 30)
        self.screen.blit(mensaje_perdida, rect_mensaje)
    
        mensaje_puntaje = fuente.render(f"Puntuación final: {self.puntuacionJugador}", True, (255, 255, 255))
        rect_puntaje = mensaje_puntaje.get_rect()
        rect_puntaje.center = (self.ajustes.anchura // 2, self.ajustes.altura // 2 + 30)
        self.screen.blit(mensaje_puntaje, rect_puntaje)

        y_offset = 80
        for i, puntaje in enumerate(self.puntuaciones_anteriores[-5:][::-1]):  # Mostrar las últimas 5 puntuaciones
            texto_puntaje_ant = fuente.render(f"Partida {len(self.puntuaciones_anteriores)-i}: {puntaje}", True, (255, 255, 255))
            rect_puntaje_ant = texto_puntaje_ant.get_rect()
            rect_puntaje_ant.center = (self.ajustes.anchura // 2, self.ajustes.altura // 2 + y_offset)
            self.screen.blit(texto_puntaje_ant, rect_puntaje_ant)
            y_offset += 50
            
        pygame.display.flip()

    def opciones_final(self):
        jugando = True
        while jugando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            fuente_opciones = pygame.font.SysFont("serif", 56)
            jugar_texto = fuente_opciones.render("Volver a Jugar", True, (0, 255, 0))
            jugar_rect = jugar_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 + 150))
            self.screen.blit(jugar_texto, jugar_rect)

            salir_texto = fuente_opciones.render("Salir", True, (255, 0, 0))
            salir_rect = salir_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 + 250))
            self.screen.blit(salir_texto, salir_rect)

            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if jugar_rect.collidepoint(mouse) and click[0] == 1:
                self.reiniciar_juego()
                jugando = False
            if salir_rect.collidepoint(mouse) and click[0] == 1:
                sys.exit()

            pygame.display.update()

    def reiniciar_juego(self):
        self.puntuaciones_anteriores.append(self.puntuacionJugador)
        self.puntuacionJugador = 0
        self.salud = self.ajustes.vidaJugador
        self.enemigosHuir = self.ajustes.enemigosQuePuedenHuir 
        self.balas.empty()
        self.enemigos.empty()
        self.balasEnemigo.empty()
        self.run_game()

    def pausar_juego(self):
        fuente = pygame.font.SysFont("serif", 56)
        pausa_texto = fuente.render("Juego en Pausa. Presiona 'P' para continuar.", True, (255, 255, 0))
        rect_pausa = pausa_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2))
        self.screen.blit(pausa_texto, rect_pausa)
        pygame.display.flip()

        pausado = True
        while pausado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pausado = False

    def actualizarPantalla(self):
        self.screen.blit(self.fondo, (0, 0))
        self.tanke.blime()
        for bala in self.balas.sprites():
            bala.pintarDisparo()
        self.enemigos.draw(self.screen)
        for balaEnemiga in self.balasEnemigo.sprites():
            balaEnemiga.pintarDisparo()
        self.puntuacion()
        self.textoSalud()
        self.cochesHuidos()
        pygame.display.flip()

    def dispararbala(self):
        if len(self.balas) < self.ajustes.balasPermitidas:
            nuevaBala = Bala(self)
            self.balas.add(nuevaBala)

    def elmininarDisparosviejos(self):
        for bala in self.balas.copy():
            if bala.rect.bottom <= 0:
                self.balas.remove(bala)

    def comprobarEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.tanke.moviendoDerecha = True
                elif event.key == pygame.K_LEFT:
                    self.tanke.moviendoIzquierda = True
                elif event.key == pygame.K_SPACE:
                    self.dispararbala()
                elif event.key == pygame.K_p:
                    self.pausar_juego()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.tanke.moviendoDerecha = False
                elif event.key == pygame.K_LEFT:
                    self.tanke.moviendoIzquierda = False

    def puntuacion(self):
        fuente = pygame.font.SysFont("serif", 56)
        superficeTexto = fuente.render(str(self.puntuacionJugador), True, (255, 255, 255))
        rectTexto = superficeTexto.get_rect()
        rectTexto.midtop = (420, 20)
        self.screen.blit(superficeTexto, rectTexto)

    def textoSalud(self):
        fuente = pygame.font.SysFont("serif", 56)
        superficeTexto = fuente.render(f" += {str(self.salud)}", True, (255, 255, 255), (0, 0, 255))
        rectTexto = superficeTexto.get_rect()
        rectTexto.midtop = (75, 0)
        self.screen.blit(superficeTexto, rectTexto)

    def cochesHuidos(self):
        fuente = pygame.font.SysFont("serif", 56)
        superficeTexto = fuente.render(f" Huidos = {str(self.enemigosHuir)}", True, (255, 255, 255), (220, 20, 60))
        rectTexto = superficeTexto.get_rect()
        rectTexto.midtop = (700, 0)
        self.screen.blit(superficeTexto, rectTexto)

    def run_game(self):
        while True:
            if not self.pausado:
                self.comprobarEventos()
                self.tanke.actualizar()
                self.balas.update()
                self.dispararEnemigo()
                self.colisionBalaNuestra()
                self.balasEnemigo.update()
                self.elmininarDisparosviejos()
                self.enviarEnemigos()
                self.actualizarEnemigos()
                self.eliminarEnemigosViejos()
                self.colisionParaJugador()
            self.actualizarPantalla()

if __name__ == '__main__':
    dc = Nivel2()
    dc.mostrar_menu()
    dc.run_game()