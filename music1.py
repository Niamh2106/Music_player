import pygame
import os #enable us to interact with operating system
import pickle #enable us to get all the metadata about a song
from tkinter import * #for gui 
from tkinter import filedialog
from pygame.constants import BUTTON_RIGHT

"""
This is a module which will define the algorithms that will be used for the different buttons.
"""
#initialise mixer
pygame.mixer.init()
global songname
songname = ""
global path 
path = ""
global paused
paused = False
global song_list

global i
i = 0
song_list = []

#function to add song from file explorer
def add_song(playlist_box):
    # folder_selected = filedialog.askdirectory()
    song = filedialog.askopenfilename(filetypes=(("mp3 Files", "*.mp3"), ))
    global songname
    global path
    for songname in song:
        songname = song.split("/")
        path = "/".join(songname)
    song_list.append(path)
    playlist_box.insert(END,songname[-1])




def play():
    pygame.mixer.music.load(song_list[i])
    pygame.mixer.music.play(loops=0)
        # pygame.mixer.music.load(song_list[i])
        # pygame.mixer.music.play(loops=0)

    
def pause():
    global paused
    
    if paused:
        pygame.mixer.music.unpause()
        paused = False   
    else:
        pygame.mixer.music.pause()
        paused = True

def play_next():
    global i
    if i == len(song_list) - 1:
        i = -1
        pygame.mixer.music.load(song_list[i + 1])
        pygame.mixer.music.play(loops=0)
        i += 1
    else:
        pygame.mixer.music.load(song_list[i + 1])
        pygame.mixer.music.play(loops=0)
        i += 1
# If current song is at the end of the list go back to the first       

        # if song_list[i] == song_list[-1]:
        #     pygame.mixer.music.load(song_list[0])
        #     pygame.mixer.music.play(loops=0)
        # else:
        #     pygame.mixer.music.play(loops=0)
        #     pygame.mixer.music.load(song_list[len(song_list) - 1])
        # i += 1
    # i = 0
    # while i < len(song_list):
        # if len(song_list) == 1:
        #     i = 0
        #     pygame.mixer.music.load(song_list[i])
        #     pygame.mixer.music.play(loops=0)

        # if i + i > len(song_list):
        #     pygame.mixer.music.load(song_list[0])
        #     pygame.mixer.music.play(loops=0)
        
        # else:
        #     pygame.mixer.music.load(song_list[len(song_list) - 1])
        #     pygame.mixer.music.play(loops=0)
        # i += 1

def play_prev():
    global i
    if i == 0:
        i = len(song_list) - 1
        pygame.mixer.music.load(song_list[i])
        pygame.mixer.music.play(loops=0)
    else:
        pygame.mixer.music.load(song_list[i - 1])
        pygame.mixer.music.play(loops=0)
        i -= 1
                # if len(song_list) == 1:
            #     i = 0
            #     pygame.mixer.music.load(song_list[i])
            #     pygame.mixer.music.play(loops=0)
            # else:
            #     pygame.mixer.music.load(song_list[len(song_list) - 1 - i])
            #     pygame.mixer.music.play(loops=0)