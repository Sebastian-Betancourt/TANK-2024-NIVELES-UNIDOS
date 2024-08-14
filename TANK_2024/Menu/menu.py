import pygame
import sys
from ajustes import Ajustes
from Nivel_1 import Nivel1
from Nivel_2 import Nivel2
from Nivel_3 import Nivel3


class Menu:
    def __init__(self):
        pygame.init()
        self.ajustes = Ajustes()
        self.screen = pygame.display.set_mode((self.ajustes.anchura, self.ajustes.altura))
        self.fondo = pygame.image.load(self.ajustes.fondo)
        
        # Cargar las imágenes
        self.titulo_imagen = pygame.image.load('C:/Users/Usuario/Pictures/TITULO2.png')
        self.insert_coin_imagen = pygame.image.load('C:/Users/Usuario/Pictures/INSERT.png')
        
        # Imágenes para las opciones del menú 2
        self.imagen_comenzar = pygame.image.load('C:/Users/Usuario/Pictures/COMENZAR.png')
        self.imagen_acerca_del_juego = pygame.image.load('C:/Users/Usuario/Pictures/ACERCA_DEL_JUEGO.png')
        self.imagen_salir = pygame.image.load('C:/Users/Usuario/Pictures/SALIR.png')
        
        # Cargar la imagen de la flecha
        self.flecha_imagen = pygame.image.load('C:/Users/Usuario/Pictures/FLECHA.png')
        self.tamano_flecha = (50, 50)
        self.flecha_imagen = pygame.transform.scale(self.flecha_imagen, self.tamano_flecha)

        # Tamaños de íconos para diferentes menús
        self.tamano_icono_menu_1 = (500, 375)  # Tamaño grande para el Menu 1
        self.tamano_icono_menu_2 = (300, 225)  # Tamaño reducido para el Menu 2

        # Inicialmente, usa el tamaño del ícono para el Menu 1
        self.titulo_imagen_menu_1 = pygame.transform.scale(self.titulo_imagen, self.tamano_icono_menu_1)
        self.titulo_imagen_menu_2 = pygame.transform.scale(self.titulo_imagen, self.tamano_icono_menu_2)
        
        self.insert_coin_imagen_menu_1 = pygame.transform.scale(self.insert_coin_imagen, (400, 150))  # Ajusta el tamaño de la imagen de "INSERT COIN"

        self.titulo_rect_menu_1 = self.titulo_imagen_menu_1.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 3))  # Centrado y movido hacia arriba
        self.insert_coin_rect = self.insert_coin_imagen_menu_1.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 1.2))  # Más abajo que el título
        self.titulo_rect_menu_2 = self.titulo_imagen_menu_2.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 5))

        # Agregar en el método __init__
        self.texto_volver_comenzar = pygame.font.SysFont(None, 60).render('Volver', True, (255, 255, 255))
        self.texto_volver_comenzar_rect = self.texto_volver_comenzar.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura - 50))
        self.posicion_flecha_volver_comenzar = (self.texto_volver_comenzar_rect.left - 70, self.texto_volver_comenzar_rect.top)

        
        # Tamaños y posiciones para las imágenes del menú 2
        self.tamano_opcion_menu_2 = (200, 75)  # Tamaño para las imágenes de las opciones
        self.imagen_comenzar = pygame.transform.scale(self.imagen_comenzar, self.tamano_opcion_menu_2)
        self.imagen_acerca_del_juego = pygame.transform.scale(self.imagen_acerca_del_juego, (300, 120))  # Tamaño aumentado para "Acerca del juego"
        
        # Modifica aquí el tamaño de la imagen "Salir"
        self.imagen_salir = pygame.transform.scale(self.imagen_salir, (180, 65))  # Tamaño reducido para "Salir"

        # Posiciones horizontales centradas
        self.posicion_comenzar = (self.ajustes.anchura // 2 - self.tamano_opcion_menu_2[0] // 2, self.ajustes.altura // 2 - 50)
        self.posicion_acerca_del_juego = (self.ajustes.anchura // 2 - 300 // 2, self.ajustes.altura // 2 + 50)  # Ajuste para imagen más grande
        self.posicion_salir = (self.ajustes.anchura // 2 - 180 // 2, self.ajustes.altura // 2 + 200)  # Ajuste para la imagen más pequeña
        
        # Posiciones de la flecha
        self.posicion_flecha = self.posicion_comenzar  # Inicia en la primera opción
        
        # Lista de posiciones de las opciones para fácil navegación
        self.opciones_menu_2 = [self.posicion_comenzar, self.posicion_acerca_del_juego, self.posicion_salir]
        self.opcion_seleccionada = 0  # Índice de la opción seleccionada
        
        pygame.display.set_caption("TANK 2024")

        # Estado del menú
        self.estado_menu = 1

        # Configuraciones para "Acerca del juego"
        self.titulo_acerca_imagen = pygame.transform.scale(self.titulo_imagen, (150, 100))  # Reducir el tamaño
        self.titulo_acerca_rect = self.titulo_acerca_imagen.get_rect(topleft=(10, 10))  # Posición en la esquina superior izquierda

        self.texto_volver = pygame.font.SysFont(None, 60).render('Volver', True, (255, 255, 255))
        self.texto_volver_rect = self.texto_volver.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura - 50))
        self.posicion_flecha_volver = (self.texto_volver_rect.left - 70, self.texto_volver_rect.top)

    def actualizar_pantalla_menu_1(self):
        self.screen.blit(self.fondo, (0, 0))
        self.screen.blit(self.titulo_imagen_menu_1, self.titulo_rect_menu_1)
        self.screen.blit(self.insert_coin_imagen_menu_1, self.insert_coin_rect)  # Dibuja la imagen de "INSERT COIN"
        pygame.display.flip()

    def actualizar_pantalla_menu_2(self):
        self.screen.blit(self.fondo, (0, 0))
        self.screen.blit(self.titulo_imagen_menu_2, self.titulo_rect_menu_2)
        
        # Dibuja las imágenes para las opciones del menú 2
        self.screen.blit(self.imagen_comenzar, self.posicion_comenzar)
        self.screen.blit(self.imagen_acerca_del_juego, self.posicion_acerca_del_juego)
        self.screen.blit(self.imagen_salir, self.posicion_salir)
        
        # Dibuja la flecha en la opción seleccionada
        self.screen.blit(self.flecha_imagen, (self.opciones_menu_2[self.opcion_seleccionada][0] - 60, self.opciones_menu_2[self.opcion_seleccionada][1] + 10))
        
        pygame.display.flip()
    def actualizar_pantalla_comenzar(self):
        self.screen.blit(self.fondo, (0, 0))
        
        # Cargar y redimensionar las imágenes de los niveles
        self.imagen_nivel_1 = pygame.image.load('C:/Users/Usuario/Pictures/NIVEL_1.png')
        self.imagen_nivel_2 = pygame.image.load('C:/Users/Usuario/Pictures/NIVEL_2.png')
        self.imagen_nivel_3 = pygame.image.load('C:/Users/Usuario/Pictures/NIVEL_3.png')
        
        # Redimensionar las imágenes de los niveles
        self.imagen_nivel_1 = pygame.transform.scale(self.imagen_nivel_1, self.tamano_opcion_menu_2)
        self.imagen_nivel_2 = pygame.transform.scale(self.imagen_nivel_2, self.tamano_opcion_menu_2)
        self.imagen_nivel_3 = pygame.transform.scale(self.imagen_nivel_3, self.tamano_opcion_menu_2)

        # Posiciones de las imágenes de niveles
        self.posicion_nivel_1 = (self.ajustes.anchura // 2 - self.tamano_opcion_menu_2[0] // 2, self.ajustes.altura // 2 - 150)
        self.posicion_nivel_2 = (self.ajustes.anchura // 2 - self.tamano_opcion_menu_2[0] // 2, self.ajustes.altura // 2 - 50)
        self.posicion_nivel_3 = (self.ajustes.anchura // 2 - self.tamano_opcion_menu_2[0] // 2, self.ajustes.altura // 2 + 50)

        # Dibuja las imágenes de niveles en las posiciones correspondientes
        self.screen.blit(self.imagen_nivel_1, self.posicion_nivel_1)
        self.screen.blit(self.imagen_nivel_2, self.posicion_nivel_2)
        self.screen.blit(self.imagen_nivel_3, self.posicion_nivel_3)
        
        # Dibuja la flecha en la opción seleccionada
        if self.opcion_seleccionada == 0:  # NIVEL 1
            self.screen.blit(self.flecha_imagen, (self.posicion_nivel_1[0] - self.flecha_imagen.get_width() - 10, self.posicion_nivel_1[1]))
        elif self.opcion_seleccionada == 1:  # NIVEL 2
            self.screen.blit(self.flecha_imagen, (self.posicion_nivel_2[0] - self.flecha_imagen.get_width() - 10, self.posicion_nivel_2[1]))
        elif self.opcion_seleccionada == 2:  # NIVEL 3
            self.screen.blit(self.flecha_imagen, (self.posicion_nivel_3[0] - self.flecha_imagen.get_width() - 10, self.posicion_nivel_3[1]))
        
        # Dibuja el botón 'Volver' y la flecha si es necesario
        if self.estado_menu == 3:  # Pantalla de Comenzar
            self.screen.blit(self.texto_volver_comenzar, self.texto_volver_comenzar_rect)
            
            # Mostrar la flecha solo si 'Volver' está seleccionado
            if self.opcion_seleccionada == 3:  # Opcionalmente, asigna 3 o el valor correcto para 'Volver'
                self.screen.blit(self.flecha_imagen, (self.posicion_flecha_volver_comenzar[0], self.posicion_flecha_volver_comenzar[1]))
        
        pygame.display.flip()

    def actualizar_pantalla_acerca(self):
        self.screen.blit(self.fondo, (0, 0))
        
        # Dibuja el título 'TITULO2' en la esquina superior izquierda
        self.screen.blit(self.titulo_acerca_imagen, self.titulo_acerca_rect)
        
        # Cargar y posicionar la imagen del párrafo más arriba
        imagen_parrafo = pygame.image.load('C:/Users/Usuario/Pictures/PARRAFOO.png')
        imagen_parrafo = pygame.transform.scale(imagen_parrafo, (self.ajustes.anchura - 20, 200))  # Ajusta el tamaño según sea necesario
        parrafo_rect = imagen_parrafo.get_rect(center=(self.ajustes.anchura // 2, self.ajustes.altura // 2 - 100))  # Más arriba
        
        self.screen.blit(imagen_parrafo, parrafo_rect)

        # Agregar el texto 'ACERCA DEL JUEGO' más a la derecha del título
        fuente = pygame.font.SysFont(None, 60)
        texto_acerca = fuente.render('ACERCA DEL JUEGO', True, (255, 255, 255))
        texto_acerca_rect = texto_acerca.get_rect(center=(self.titulo_acerca_rect.centerx + 350, self.titulo_acerca_rect.centery))  # Más a la derecha
        
        self.screen.blit(texto_acerca, texto_acerca_rect)
        
        # Dibuja el botón 'Volver' y la flecha
        self.screen.blit(self.texto_volver, self.texto_volver_rect)
        self.screen.blit(self.flecha_imagen, self.posicion_flecha_volver)
        
        
        
         # Agregar el título "CONTROLES" debajo del párrafo y alineado a la izquierda
        fuente_controles = pygame.font.SysFont(None, 50)
        texto_controles = fuente_controles.render('CONTROLES', True, (255, 255, 255))
        texto_controles_rect = texto_controles.get_rect(topleft=(10, parrafo_rect.bottom + 20))  # Ajuste la posición justo debajo del párrafo y alineado a la izquierda
        
        self.screen.blit(texto_controles, texto_controles_rect)
        
        # Cargar y redimensionar la imagen "PARRAFO2" para ocupar la mitad de la pantalla
        imagen_parrafo2 = pygame.image.load('C:/Users/Usuario/Pictures/PARRAFO2.png')
        ancho_parrafo2 = (self.ajustes.anchura - 30) // 2  # La mitad del ancho de la pantalla menos un pequeño margen
        imagen_parrafo2 = pygame.transform.scale(imagen_parrafo2, (ancho_parrafo2, 150))  # Ajusta la altura si es necesario
        parrafo2_rect = imagen_parrafo2.get_rect(topleft=(10, texto_controles_rect.bottom + 20))  # Posicionar debajo del título "CONTROLES"
        
        self.screen.blit(imagen_parrafo2, parrafo2_rect)
        
        # Cargar y redimensionar la imagen "FLECHAS" para que sea más pequeña
        imagen_flechas = pygame.image.load('C:/Users/Usuario/Pictures/FLECHAS.png')
        ancho_flechas = (self.ajustes.anchura - 30) // 8  # Tamaño reducido
        imagen_flechas = pygame.transform.scale(imagen_flechas, (ancho_flechas, 50))  # Ajusta la altura si es necesario
        flechas_rect = imagen_flechas.get_rect(topleft=(self.ajustes.anchura // 2 + 10, texto_controles_rect.bottom + 20))  # Posicionar en la mitad derecha
        
        self.screen.blit(imagen_flechas, flechas_rect)
        
        # Cargar y redimensionar la imagen "ESPACIO" para que sea más pequeña
        imagen_espacio = pygame.image.load('C:/Users/Usuario/Pictures/ESPACIO.png')
        imagen_espacio = pygame.transform.scale(imagen_espacio, (ancho_flechas, 50))  # Ajusta la altura si es necesario
        espacio_rect = imagen_espacio.get_rect(topleft=(self.ajustes.anchura // 2 + 10, flechas_rect.bottom + 20))  # Posicionar debajo de la imagen "FLECHAS"
        
        self.screen.blit(imagen_espacio, espacio_rect)
        
        # Agregar el texto "DESARROLLADORES DEL JUEGO" al lado de las imágenes
        fuente_desarrolladores = pygame.font.SysFont(None, 30)  # Tamaño más pequeño
        texto_desarrolladores1 = fuente_desarrolladores.render('DESARROLLADORES', True, (255, 255, 255))
        texto_desarrolladores2 = fuente_desarrolladores.render('DEL JUEGO', True, (255, 255, 255))

        # Ajustar la posición para que esté más a la derecha
        texto_desarrolladores1_rect = texto_desarrolladores1.get_rect(topleft=(self.ajustes.anchura // 2 + 10 + ancho_flechas + 10, texto_controles_rect.top))  # Ajuste a la derecha
        texto_desarrolladores2_rect = texto_desarrolladores2.get_rect(topleft=(texto_desarrolladores1_rect.left, texto_desarrolladores1_rect.bottom + 5))  # Justo debajo del primer texto

        self.screen.blit(texto_desarrolladores1, texto_desarrolladores1_rect)
        self.screen.blit(texto_desarrolladores2, texto_desarrolladores2_rect)
        
        # Cargar y redimensionar la imagen "NOMBRES"
        imagen_nombres = pygame.image.load('C:/Users/Usuario/Pictures/NOMBRES.png')
        imagen_nombres = pygame.transform.scale(imagen_nombres, (ancho_flechas * 2, 100))  # Ajusta el tamaño según sea necesario
        nombres_rect = imagen_nombres.get_rect(topleft=(self.ajustes.anchura // 2 + 10 + ancho_flechas + 10, texto_desarrolladores2_rect.bottom + 20))  # Posicionar debajo del texto "DESARROLLADORES DEL JUEGO"
        
        self.screen.blit(imagen_nombres, nombres_rect)
        
        pygame.display.flip()
    def actualizar_pantalla_inicio(self):
        self.screen.blit(self.fondo, (0, 0))
        pygame.display.flip()

    def gestionar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if self.estado_menu == 1:  # Menu 1
                    if evento.key == pygame.K_SPACE:
                        self.estado_menu = 2  # Cambiar al Menu 2

                elif self.estado_menu == 2:  # Menu 2
                    if evento.key == pygame.K_DOWN:
                        self.opcion_seleccionada = (self.opcion_seleccionada + 1) % len(self.opciones_menu_2)
                    elif evento.key == pygame.K_UP:
                        self.opcion_seleccionada = (self.opcion_seleccionada - 1) % len(self.opciones_menu_2)
                    elif evento.key == pygame.K_SPACE:
                        if self.opcion_seleccionada == 0:  # Comenzar
                            self.estado_menu = 3  # Cambiar a la pantalla de niveles
                            self.opcion_seleccionada = 0  # Reiniciar selección de nivel
                        elif self.opcion_seleccionada == 1:  # Acerca del juego
                            self.estado_menu = 4  # Cambiar a la pantalla "Acerca del juego"
                        elif self.opcion_seleccionada == 2:  # Salir
                            pygame.quit()
                            sys.exit()

                elif self.estado_menu == 3:  # Pantalla de niveles
                    if evento.key == pygame.K_DOWN:
                        self.opcion_seleccionada = (self.opcion_seleccionada + 1) % 4
                    elif evento.key == pygame.K_UP:
                        self.opcion_seleccionada = (self.opcion_seleccionada - 1) % 4
                    elif evento.key == pygame.K_SPACE:
                        if self.opcion_seleccionada == 0:  # NIVEL 1
                            nivel = Nivel1()
                            nivel.run_game()
                        elif self.opcion_seleccionada == 1:  # NIVEL 2
                            nivel = Nivel2()
                            nivel.run_game()
                        elif self.opcion_seleccionada == 2:  # NIVEL 3
                            nivel = Nivel3()
                            nivel.run_game()
                        elif self.opcion_seleccionada == 3:  # Volver
                            self.estado_menu = 2  # Volver al Menu 2 
                            self.opcion_seleccionada = 0  # Reiniciar selección

                elif self.estado_menu == 4:  # Pantalla "Acerca del juego"
                    if evento.key == pygame.K_SPACE:
                        self.estado_menu = 2  # Volver al Menu 2

    def ejecutar(self):
        while True:
            self.gestionar_eventos()
            
            if self.estado_menu == 1:
                self.actualizar_pantalla_menu_1()
            elif self.estado_menu == 2:
                self.actualizar_pantalla_menu_2()
            elif self.estado_menu == 3:
                self.actualizar_pantalla_comenzar()
            elif self.estado_menu == 4:
                self.actualizar_pantalla_acerca()
            
if __name__ == "__main__":
    menu = Menu()
    menu.ejecutar()