import os #enable us to interact with operating system
import pickle #enable us to get all the metadata about a song
from tkinter import * #for gui 
import pygame #added functionality
from tkinter import filedialog

from pygame.constants import BUTTON_RIGHT

root = Tk()
root.title('AIM Music Player')
root.iconbitmap('aim-icon.bmp')
root.geometry("700x500")
root.configure(background='black')

#initialise python mixer/turn on mixer to enable sound
pygame.mixer.init()

#function to add song from file explorer
def add_song():
    folder_selected = filedialog.askdirectory()
    song = filedialog.askopenfilename(filetypes=(("mp3 Files", "*.mp3"), ))
    playlist_box.insert(END,song)
    root.mainloop()
    
# #Playlist title name
playlist_name = Label(root, text = "Playlist", bg="red",
fg = "white",font=("calibri",14,"bold"), width="16")
playlist_name.pack(side=RIGHT)
# .grid(row=0, column=1)


#Playlist Box code
playlist_box = Listbox(root,bg="red",fg="black",font=("calibri"), 
highlightcolor="darkred", height="20", width="20",)
playlist_box.pack(side=RIGHT)
# .grid(row=1, column=1)

#Create Space
create_space1 = 1

#Add Song Button
add_songs = Button(root, text = "Add Songs", bg="red",fg="white",font=("calibri",14,
"bold"), highlightcolor="darkred", width="16",command=add_song)
add_songs.pack(side=RIGHT)
# .grid(row=2, column=1)

root.mainloop()