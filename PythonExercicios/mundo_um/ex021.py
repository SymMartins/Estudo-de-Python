# Tocando um MP3

import pygame

pygame.mixer.init()
pygame.mixer.music.load('temadavitoria.mp3')
pygame.mixer.music.play()

parar = input('Digite algo para parar: ')
