"""
This is a module we created which will define the algorithms that will be used for the different buttons 
along with a class definition for songs.
"""
import pygame
from tkinter import filedialog, END, PhotoImage
import os

#song class
class Song:
    def __init__(self, artist, name, path, image = ""):
        self.artist = artist
        self.name = name
        self.image = image
        self.path = path

    """
    This is a function that will check if a song has an image associated with it.
    To associate a song with an image just rename the image to the song name and add the image to the images folder.
    Example: song name = Paradise then image name = Paradise
    Only supports .png images
    """
    def check_image(self):
        temp = self.name.strip() #remove spaces
        #checks to see if image exists
        if os.path.exists("images/" + temp + ".png"):
            self.image = PhotoImage(file="images/" + temp + ".png")
            self.image = self.image.subsample(3,3) #image resizing
        else:
            self.image = PhotoImage(file="images/aim.png") #default image
            self.image = self.image.subsample(6,6) 

#initialise the pygame mixer module
pygame.mixer.init()

global paused
paused = False

global i
i = 0

song_list = []

#songs must be named in the following format song - artist
#function to add song from file explorer
def add_song(playlist_box):
    try:
        #select song, only allows mp3 files to be selected
        path = filedialog.askopenfilename(filetypes=(("mp3 Files", "*.mp3"), ))
        
        #remove .mp3 file extension
        songname = path.split("/")
        songname = songname[-1].split(".")
        songname = songname[:-1]
        
        #isolate songname and artist
        temp = songname
        songname = ""
        songname = songname.join(temp)
        songname = songname.split("-")

        #create song object
        song_obj = Song(songname[0], songname[1], path)
        song_obj.check_image() #check if that song has an image 

        #add song to playlist
        song_list.append(song_obj)
        playlist_box.insert(END, song_obj.artist + song_obj.name)
    except IndexError: #if user clicks button does not add song this exception will handle the error
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
            obj = song_list[i]

            #Display current song and its image
            name.config(text=obj.name)
            artist.config(text=obj.artist)
            image.config(image=obj.image, bg=None)

            #load and play song
            pygame.mixer.music.load(obj.path)
            pygame.mixer.music.play(loops=0)
    except IndexError: #handles error for if user presses play before a song has been added to the playlist
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
            obj = song_list[i + 1]
            pygame.mixer.music.load(obj.path)
            pygame.mixer.music.play(loops=0)
            i += 1
        else:
            obj = song_list[i + 1]
            pygame.mixer.music.load(obj.path)
            pygame.mixer.music.play(loops=0)
            i += 1

        #Display current song and its image
        name.config(text=obj.name)
        artist.config(text=obj.artist)
        image.config(image=obj.image, bg=None)
    except IndexError:#handles error for if user presses play next button before a song has been added to the playlist
        pass

#play previous button
def play_prev(name, artist, image):
    try:
        global i

        #check if current song is first song
        if i == 0:
            i = len(song_list) - 1
            obj = song_list[i]
            pygame.mixer.music.load(obj.path)
            pygame.mixer.music.play(loops=0)
        else:
            obj = song_list[i - 1]
            pygame.mixer.music.load(obj.path)
            pygame.mixer.music.play(loops=0)
            i -= 1

        #Display current song and its image
        name.config(text=obj.name)
        artist.config(text=obj.artist)
        image.config(image=obj.image, bg=None)
    except IndexError: #handles error for if user presses play previous button before a song has been added to the playlist
        pass

#volume slider
def volume(val):
    volume = int(val)
    pygame.mixer.music.set_volume(volume)
