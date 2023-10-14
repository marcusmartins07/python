import pygame
pygame.init()
pygame.mixer.music.load('C:\\Users\Marcus Martins\\Documents\\Estudos\\python\\ex001\\assets\\audio.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())