import pygame
import random
"""
This is a module which will define the algorithms that will be used for the different buttons.
"""

#initialise mixer
pygame.mixer.init()
song_list = []
global paused
global play_next
paused = False

def play():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load("songs/Clean Bandit - Symphony (feat. Zara Larsson) [Official Video].mp3")
        pygame.mixer.music.play(loops=0)

def pause():
    global paused
    
    if paused:
        pygame.mixer.music.unpause()
        paused = False   
    else:
        pygame.mixer.music.pause()
        paused = True

def play_next():
        i = 0

        while i < len(song_list):
            pygame.mixer.music.load(song_list[i + 1])
            pygame.mixer.music.play()
            if paused:
            pause()
            i += 1

def play_prev():
    i = 0

        while i < len(song_list):
            if song_list[i] == song_list[0]:
                song_list[i] = song_list[-1]
                pygame.mixer.music.load(song_list[i - 1])
                pygame.mixer.music.play(loops=0)
            if paused:
            pause()
            i += 1

def shuffle():
    random_song = song_list.choice()
    pygame.mixer.music.load(random_song)
    pygame.mixer.music.play(loops=0)
    if paused:
            pause()


