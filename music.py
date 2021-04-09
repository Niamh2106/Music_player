"""
This is a module which will define the algorithms that will be used for the different buttons .
"""
import pygame
from tkinter import filedialog, END, PhotoImage
import random
import os

#song class
class Song:
    def __init__(self, artist, name, image = ""):
        self.artist = artist
        self.name = name
        self.image = image

    """
    This is a function that will check if a song has an image associated with it.
    To associate a song with an image just rename the image to the song name and add the image to the images folder.
    Example: song name = Paradise then image name = Paradise 
    """
    def check_image(self):
        if os.path.exists("images/" + self.name + ".png"):
            self.image = PhotoImage(file="images/" + self.name + ".png")
            self.image = self.image.subsample(3,3)
        else:
            self.image = PhotoImage(file="images/aim.png")
            self.image = self.image.subsample(6,6) 

#initialise the pygame mixer module
pygame.mixer.init()

global songname
songname = ""

global path 
path = ""

global paused
paused = False


global i
i = 0

song_list = []
songs_objects = {}

#songs must be named in the following format song - artist
#function to add song from file explorer
def add_song(playlist_box):

    try:
        #select song
        song = filedialog.askopenfilename(filetypes=(("mp3 Files", "*.mp3"), ))
        path = song
        
        #remove .mp3 file extension
        songname = song.split("/")
        songname = songname[-1].split(".")
        songname = songname[:-1]
        
        #isolate songname and artist
        temp = songname
        songname = ""
        songname = songname.join(temp)
        songname = songname.split("-")

        #create song object
        song_obj = Song(songname[0].strip(), songname[1].strip())
        song_obj.check_image()
        songs_objects[song_obj] = path

        #add song to playlist
        song_list.append(path)
        playlist_box.insert(END,song_obj.artist + song_obj.name)
    except IndexError:
        pass

#play button
def play(name, artist, image):
    try:
        global paused

        #check if already paused
        if paused:
            pygame.mixer.music.unpause()
            paused = False   
        else:
            obj = None

            #obtain songname
            for key, value in songs_objects.items():
                if value == song_list[i]:
                    obj = key
                    break

            #Display current song
            name.config(text=obj.name)
            artist.config(text=obj.artist)
            image.config(image=obj.image, bg=None)

            #load and play song
            pygame.mixer.music.load(song_list[i])
            pygame.mixer.music.play(loops=0)
    except AttributeError:
        pass


#pause button  
def pause():
    global paused
    
    #check if already paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False   
    else:
        pygame.mixer.music.pause()
        paused = True

#play next button
def play_next(name, artist, image):
    try:
        global i

        #check if current song is last song
        if i == len(song_list) - 1:
            i = -1
            pygame.mixer.music.load(song_list[i + 1])
            pygame.mixer.music.play(loops=0)
            i += 1
        else:
            pygame.mixer.music.load(song_list[i + 1])
            pygame.mixer.music.play(loops=0)
            i += 1
        
        obj = None
        #obtain songname
        for key, value in songs_objects.items():
            if value == song_list[i]:
                obj = key
                break

        #Display current song
        name.config(text=obj.name)
        artist.config(text=obj.artist)
        image.config(image=obj.image, bg=None)
    except IndexError:
        pass

#play previous button
def play_prev(name, artist, image):
    try:
        global i

        #check if current song is first song
        if i == 0:
            i = len(song_list) - 1
            pygame.mixer.music.load(song_list[i])
            pygame.mixer.music.play(loops=0)
        else:
            pygame.mixer.music.load(song_list[i - 1])
            pygame.mixer.music.play(loops=0)
            i -= 1
        
        obj = None
        #obtain songname
        for key, value in songs_objects.items():
            if value == song_list[i]:
                obj = key
                break

        #Display current song
        name.config(text=obj.name)
        artist.config(text=obj.artist)
        image.config(image=obj.image, bg=None)
    except IndexError:
        pass

#volume slider
def volume(val):
    volume = int(val)
    pygame.mixer.music.set_volume(volume)