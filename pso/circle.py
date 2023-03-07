import pygame
pygame.init()


screen=pygame.display.set_mode((500,500))
pygame.display.set_caption('Animated circle')


x,y=200,200

xv=5
yv=-5


while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            