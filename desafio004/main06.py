import pygame
pygame.init()
screen = pygame.mixer.Sound("main06.mp3")
pygame.mixer.Sound.play(screen)
pygame.event.wait()