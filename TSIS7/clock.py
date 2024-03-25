import pygame
import os
from datetime import datetime


WIDTH = 400
HEIGHT = 400

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
work = True
fps = pygame.time.Clock()

clock_image = get_image('assets/mainclock.png')
clock_center = (WIDTH//2, HEIGHT//2)
clock_radius = 150

left_arm_image = get_image('assets/leftarm.png')
right_arm_image = get_image('assets/rightarm.png')




while work:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            work = False


    current_time = datetime.now()
    seconds = current_time.second
    minutes = current_time.minute

    left_arm_angle = -(seconds/60) * 360 + 90
    right_arm_angle = -((minutes+23)/60) * 360 + 90


    screen.blit(clock_image, (WIDTH // 2 - clock_image.get_width() // 2, HEIGHT // 2 - clock_image.get_height() // 2))

    blitRotateCenter(screen, left_arm_image, (clock_center[0] - left_arm_image.get_width() // 2, clock_center[1] - left_arm_image.get_height() // 2), left_arm_angle)
    blitRotateCenter(screen, right_arm_image, (clock_center[0] - right_arm_image.get_width() // 2, clock_center[1] - right_arm_image.get_height() // 2), right_arm_angle)


    pygame.display.flip()
    fps.tick(60)
