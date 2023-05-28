import pygame, sys

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')
clock = pygame.time.Clock()

# import images
background_surf = pygame.image.load('without_classes/graphics/background.png').convert()

ship_surf = pygame.image.load('without_classes/graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load('without_classes/graphics/laser.png').convert_alpha()
laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
                               
# import text
font = pygame.font.Font('without_classes/graphics/subatomic.ttf', 50)
text_surf = font.render('Space', True, (255,255,255))
text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # framerate limit
    clock.tick(120)

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # updates
    laser_rect.y -= 10

    # drawing
    display_surface.fill((0,0,0))
    display_surface.blit(background_surf, (0, 0))

    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (255,255,255), text_rect.inflate(30,30), width = 8, border_radius = 5)
    
    display_surface.blit(ship_surf, ship_rect)
    display_surface.blit(laser_surf, laser_rect)

    # Draw final frame
    pygame.display.update()