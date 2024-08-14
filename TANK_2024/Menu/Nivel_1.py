import pygame
import sys
import random
from ajustes import Ajustes
from tanke import Tanke
from enemigo import Enemigo

class Nivel1:
    def __init__(self):
        pygame.init()
        self.ajustes = Ajustes()
        self.screen = pygame.display.set_mode((self.ajustes.anchura, self.ajustes.altura))
        self.fondo = pygame.image.load(self.ajustes.fondo)
        pygame.display.set_caption("TANK 2024")
        self.tanke = Tanke(self)
        self.enemigos = pygame.sprite.Group()
        self.puntuacionJugador = 0
        self.salud = self.ajustes.vidaJugador
        self.puntajes_anteriores = []
        self.pausado = False

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
                menu = False  # Sale del menú y comienza el juego
            if salir_rect.collidepoint(mouse) and click[0] == 1:
                sys.exit()

            pygame.display.update()

    def enviarEnemigos(self):
        if len(self.enemigos) < 10 and random.randint(1, 100) <= self.ajustes.probabilidadEnviarEnemigo:
            tankeMalvado = Enemigo(self)
            self.enemigos.add(tankeMalvado)

    def eliminarEnemigosViejos(self):
        for enemigo in self.enemigos.copy():
            if enemigo.rect.bottom >= self.ajustes.altura:
                self.enemigos.remove(enemigo)
                self.puntuacionJugador += 10

    def actualizarEnemigos(self):
        self.enemigos.update()

    def colisionParaJugador(self):
        colisionEnemigo = pygame.sprite.spritecollide(self.tanke, self.enemigos, True)
        if len(colisionEnemigo):
            self.salud -= 1
            self.estaMuerto()

    def estaMuerto(self):
        if self.salud <= 0:
            self.puntajes_anteriores.append(self.puntuacionJugador)
            self.mostrar_mensaje_final()

    def mostrar_mensaje_final(self):
        self.screen.fill((0, 0, 0))
        fuente = pygame.font.SysFont("serif", 56)

        mensaje_perdida = fuente.render("¡Perdiste!", True, (255, 0, 0))
        rect_mensaje = mensaje_perdida.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 - 100))
        self.screen.blit(mensaje_perdida, rect_mensaje)

        mensaje_puntaje = fuente.render(f"Puntuación final: {self.puntuacionJugador}", True, (255, 255, 255))
        rect_puntaje = mensaje_puntaje.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 - 50))
        self.screen.blit(mensaje_puntaje, rect_puntaje)

        fuente_puntajes = pygame.font.SysFont("serif", 36)
        if self.puntajes_anteriores:
            mensaje_puntajes = fuente_puntajes.render("Puntajes Anteriores:", True, (255, 255, 255))
            rect_puntajes = mensaje_puntajes.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 + 20))
            self.screen.blit(mensaje_puntajes, rect_puntajes)

            for i, puntaje in enumerate(reversed(self.puntajes_anteriores[-5:]), start=1):
                puntaje_texto = fuente_puntajes.render(f"{i}. {puntaje}", True, (255, 255, 255))
                puntaje_rect = puntaje_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 + 50 + i * 40))
                self.screen.blit(puntaje_texto, puntaje_rect)

        fuente_opciones = pygame.font.SysFont("serif", 56)
        volver_texto = fuente_opciones.render("Volver a Jugar", True, (0, 255, 0))
        volver_rect = volver_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 + 250))
        self.screen.blit(volver_texto, volver_rect)

        salir_texto = fuente_opciones.render("Salir", True, (255, 0, 0))
        salir_rect = salir_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 + 320))
        self.screen.blit(salir_texto, salir_rect)

        pygame.display.flip()
        self.wait_for_option(volver_rect, salir_rect)

    def wait_for_option(self, volver_rect, salir_rect):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                if volver_rect.collidepoint(mouse) and click[0] == 1:
                    self.reset_game()  # Reinicia el juego de forma controlada
                if salir_rect.collidepoint(mouse) and click[0] == 1:
                    sys.exit()

            pygame.display.update()

    def reset_game(self):
        self.puntuacionJugador = 0
        self.salud = self.ajustes.vidaJugador
        self.enemigos.empty()
        self.pausado = False
        self.run_game()

    def pausar_juego(self):
        fuente = pygame.font.SysFont("serif", 56)
        pausa_texto = fuente.render("Juego en Pausa. Presiona 'P' para continuar.", True, (255, 255, 0))
        rect_pausa = pausa_texto.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2))
        self.screen.blit(pausa_texto, rect_pausa)
        pygame.display.flip()

        while self.pausado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pausado = False

    def actualizarPantalla(self):
        self.screen.blit(self.fondo, (0, 0))
        self.tanke.blime()
        self.enemigos.draw(self.screen)
        self.puntuacion()
        self.textoSalud()
        pygame.display.flip()

    def comprobarEventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.tanke.moviendoDerecha = True
                elif event.key == pygame.K_LEFT:
                    self.tanke.moviendoIzquierda = True
                elif event.key == pygame.K_UP:
                    self.tanke.moviendoArriba = True
                elif event.key == pygame.K_DOWN:
                    self.tanke.moviendoAbajo = True
                elif event.key == pygame.K_p:
                    self.pausado = True
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

    def run_game(self):
        while True:
            if not self.pausado:
                self.comprobarEventos()
                self.tanke.actualizar()
                self.enviarEnemigos()
                self.actualizarEnemigos()
                self.eliminarEnemigosViejos()
                self.colisionParaJugador()
                self.actualizarPantalla()
            else:
                self.pausar_juego()

if __name__ == '__main__':
    dc = Nivel1()
    dc.mostrar_menu()
    dc.run_game()
