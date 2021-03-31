import tkinter as tk
import pygame
import music
import os #enable us to interact with operating system
import pickle #enable us to get all the metadata about a song
from tkinter import filedialog
from tkinter import * #for gui 


root = tk.Tk()
root.title('AIM Music Player')
root.iconbitmap('aim-icon.bmp')
root.geometry("700x500")
root.configure(background='black')

#initialise python mixer/turn on mixer to enable sound
pygame.mixer.init()

#function to add song from file explorer
def add_song():
    #folder_selected = filedialog.askdirectory()
    global songname
    song = filedialog.askopenfilename(filetypes=(("mp3 Files", "*.mp3"), ))
    for songname in song:
    	songname = song.split("/")
    playlist_box.insert(END,songname[-1:])
    print (songname[-1])
    
# #Playlist title name
playlist_name = Label(root, text = "Playlist", bg="red",
fg = "white",font=("calibri",14,"bold"), width="16")
playlist_name.grid(row=0, column=0)


#Playlist Box code
playlist_box = Listbox(root,bg="red",fg="black",font=("calibri"), 
highlightcolor="darkred", height="20", width="20",)
playlist_box.grid(row=1, column=0)
#Create Space
create_space1 = 1

#Add Song Button
add_songs = Button(root, text = "Add Songs", bg="red",fg="white",font=("calibri",14,
"bold"), highlightcolor="darkred", width="16",command=add_song)
add_songs.grid(row=2, column=0)


#Load images
play_button_pic = tk.PhotoImage(file = "images/play_button.png")
pause_button_pic = tk.PhotoImage(file = "images/pause.png") 
next_button_pic = tk.PhotoImage(file = "images/next_button.png")
prev_button_pic = tk.PhotoImage(file = "images/prev_button.png")
# shuffle_button_pic = tk.PhotoImage(file = "images/shuffle.png")

#Buttons
prev_button = tk.Button(root, image = prev_button_pic, borderwidth = 0, command = music.play_prev).grid(row=0, column=0)
play_button = tk.Button(root, image = play_button_pic, borderwidth = 0, command = music.play).grid(row=0, column=1)
pause_button = tk.Button(root, image = pause_button_pic, borderwidth = 0, command = music.pause).grid(row=0, column=2)
next_button = tk.Button(root, image = next_button_pic, borderwidth = 0, command = music.play_next).grid(row=0, column=3)
shuffle_button = tk.Button(root, image = next_button_pic, borderwidth = 0, command = music.play_next).grid(row=0, column=4)



root.mainloop()