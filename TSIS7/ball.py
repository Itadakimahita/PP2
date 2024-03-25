import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
work = True

dir = [0, 0]

x, y = 50, 50
speed = 20

clock = pygame.time.Clock()

while work:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            work = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dir[0] = 1
            elif event.key == pygame.K_LEFT:
                dir[0] = -1
            else:
                dir[0] = 0
            if event.key == pygame.K_UP:
                dir[1] = -1
            elif event.key == pygame.K_DOWN:
                dir[1] = 1
            else:
                dir[1] = 0
        else:
            dir = [0, 0]

    screen.fill((255, 255, 255))

    

    if dir == [1, 0]:
        if WIDTH <= x:
            x = 0
        x+=speed
        
    elif dir == [-1, 0]:
        if x <= 0:
            x = WIDTH
        x -= speed
    elif dir == [0, 1]:
        if y >= HEIGHT:
            y = 0
        y += speed
    elif dir == [0, -1]:
        if y <= 0:
            y = HEIGHT
        y -= speed

    pygame.draw.circle(screen, (0,0,0), (x,y), 25)

    pygame.display.flip()
    clock.tick(FPS)
