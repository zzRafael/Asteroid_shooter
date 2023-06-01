import pygame, sys

# init pygame
pygame.init()

# window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')

# set a clock
clock = pygame.time.Clock()

# main loop
while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # delta time
    dt = clock.tick() / 1000

    # draws
    display_surface.fill((50,50,0))

    # drawing final frame
    pygame.display.update()