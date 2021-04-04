import tkinter as tk
import pygame
import music1
from tkinter import * #for gui 


root = tk.Tk()
root.title('AIM Music Player')
root.iconbitmap('aim-icon.bmp')
root.geometry("380x500")
root.configure(background='black')

#initialise python mixer/turn on mixer to enable sound


#Load images
play_button_pic = tk.PhotoImage(file = "images/play_button.png")
pause_button_pic = tk.PhotoImage(file = "images/pause.png") 
next_button_pic = tk.PhotoImage(file = "images/next_button.png")
prev_button_pic = tk.PhotoImage(file = "images/prev_button.png")

# Resizing images
play_button_pic = play_button_pic.subsample(4,4)
pause_button_pic = pause_button_pic.subsample(4,4)
next_button_pic = next_button_pic.subsample(4,4)
prev_button_pic = prev_button_pic.subsample(4,4)


# #Playlist title name
playlist_name = Label(root, text = "Playlist", bg="red",
fg = "white",font=("calibri",14,"bold"), width="25")
playlist_name.grid(row=0, column=0)


#Playlist Box code
playlist_box = Listbox(root,bg="red",fg="black",font=("calibri"), 
highlightcolor="darkred", height="20", width="35",)
playlist_box.grid(row=1, column=0)


#Add Song Button
add_songs = Button(root, text = "Add Songs", bg="red",fg="white",font=("calibri",14,
"bold"), highlightcolor="darkred", width="16",command=lambda: music1.add_song(playlist_box))
add_songs.grid(row=2, column=0)

#Buttons
prev_button = tk.Button(root, image = prev_button_pic, borderwidth = 0, command = music1.play_prev).grid(row=1, column=1)
play_button = tk.Button(root, image = play_button_pic, borderwidth = 0, command = music1.play).grid(row=2, column=1)
pause_button = tk.Button(root, image = pause_button_pic, borderwidth = 0, command = music1.pause).grid(row=3, column=1)
next_button = tk.Button(root, image = next_button_pic, borderwidth = 0, command = music1.play_next).grid(row=4, column=1)




root.mainloop()