import pygame, random, sys
from pygame.locals import *
pygame.init()

res = (640,640)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(res)
pygame.display.set_caption('Unicorn')

unicorn = pygame.image.load("unicorn.jpg")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(unicorn,(0,0))
    clock.tick(60)
    pygame.display.flip()
