import pygame

"""
This is a module which will define the algorithms that will be used for the different buttons.
"""

#initialise mixer
pygame.mixer.init()

global paused
paused = False

def play():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load(songname[-1])
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
    pass
    
def play_prev():
    pass