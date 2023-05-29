import pygame, sys
from random import randint, uniform

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')
clock = pygame.time.Clock()

def laser_update(laser_list, speed = 1000):
    for rect in laser_list:
        rect.y -= round(speed * dt)
        if rect.bottom < 0:
            laser_list.remove(rect) 

def meteor_update(meteor_list, speed = 300):
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)

def display_score():
    score_text = f'Score: {pygame.time.get_ticks() // 1000}'
    text_surf = font.render(score_text, True, (255,255,255))
    text_rect = text_surf.get_rect(midbottom = (WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, (255,255,255), text_rect.inflate(30,30), width = 8, border_radius = 5)

def laser_timer(can_shoot, duration = 100):
    if not can_shoot:
        current_time = pygame.time.get_ticks()
        if current_time - shoot_time > duration:
            can_shoot = True
    return can_shoot

# import images
background_surf = pygame.image.load('without_classes/graphics/background.png').convert()

ship_surf = pygame.image.load('without_classes/graphics/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2) )

laser_surf = pygame.image.load('without_classes/graphics/laser.png').convert_alpha()
laser_list = []

# meteors
meteor_surf = pygame.image.load('without_classes/graphics/meteor.png').convert_alpha()
meteor_list = []

#laser timer
can_shoot = True
shoot_time = None
                               
# import text
font = pygame.font.Font('without_classes/graphics/subatomic.ttf', 50)

# meteor timer
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 250)

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            # laser
            laser_rect = laser_surf.get_rect(midbottom = ship_rect.midtop)
            laser_list.append(laser_rect)

            # timer
            can_shoot = False
            shoot_time = pygame.time.get_ticks()
        if event.type == meteor_timer:
            # random position
            y_pos = randint(-100,-50)
            x_pos = randint(-100,WINDOW_WIDTH + 100)

            # drawig a rect
            meteor_rect = meteor_surf.get_rect(midbottom = (x_pos, y_pos))

            # create a random direction
            direction = pygame.math.Vector2(uniform(-0.5, 0.5), 2)
            meteor_list.append((meteor_rect, direction))
    
    # framerate limit
    dt = clock.tick(120) / 1000

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # updates
    laser_update(laser_list=laser_list)
    meteor_update(meteor_list=meteor_list)

    #collisions
    for meteor_tuple in meteor_list:
        meteor_rect = meteor_tuple[0]
        if ship_rect.colliderect(meteor_rect):
            print(f'Score: {pygame.time.get_ticks() // 1000}')
            pygame.quit()
            sys.exit()
    
    for laser_rect in laser_list:
        for meteor_tuple in meteor_list:
            meteor_rect = meteor_tuple[0]
            if laser_rect.colliderect(meteor_rect):
                meteor_list.remove(meteor_tuple)
                try:
                    laser_list.remove(laser_rect)
                except ValueError:
                    pass
    # drawing
    display_surface.fill((0,0,0))
    display_surface.blit(background_surf, (0, 0))

    # display score
    display_score()
    # display ship
    display_surface.blit(ship_surf, ship_rect)

    # display laser
    can_shoot = laser_timer(can_shoot)
    for rect in laser_list:
        display_surface.blit(laser_surf, rect)
    # display meteor
    for meteor_tuple in meteor_list:
        display_surface.blit(meteor_surf, meteor_tuple[0])

    # Draw final frame
    pygame.display.update()
