import pygame
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))

music_directory = "assets/"

music_files = [file for file in os.listdir(music_directory) if file.endswith(".mp3")]

current_index = 0

pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_directory, music_files[current_index]))

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_RIGHT:
                current_index = (current_index + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_directory, music_files[current_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                current_index = (current_index - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_directory, music_files[current_index]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

        elif event.type == pygame.QUIT:
            running = False

pygame.quit()
