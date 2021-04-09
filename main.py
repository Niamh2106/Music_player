from tkinter import * #for gui 
import music

root = Tk() #initialise windoe
root.title('AIM Music Player') #window title
root.geometry("750x450") #window size
root.resizable(0, 0) #restrict window size
root.configure(background='black') #window background colour

#Load images
play_button_pic = PhotoImage(file = "images/play_button.png")
pause_button_pic = PhotoImage(file = "images/pause.png") 
next_button_pic = PhotoImage(file = "images/next_button.png")
prev_button_pic = PhotoImage(file = "images/prev_button.png")

aim_img = PhotoImage(file = "images/aim.png")
aim_img = aim_img.subsample(6,6) #resize image
root.iconphoto(False, aim_img) #set program icon image

#Image Frame
StatImgFrame = LabelFrame(root, bg = "black",bd=0, width=27,pady=0)
StatImgFrame.grid(row=1, column=0)

#Currently Playing Label 
current_play= Label(root, text = "Currently Playing", bg="#990000", fg = "white",font=("calibri",14,), width=27, pady=0, padx=0)
current_play.grid(row=0,column=0)

#Song Image 
song_image = Label(root, image = aim_img, bg = "#990000")
song_image.grid(row=1,column=0)

# Playlist Frame
playlistframe = LabelFrame(root, bg = "black",bd=0, width=27,pady=0)
playlistframe.grid(row=1, column=4)

#Playlist Label Name
playlist_name = Label(playlistframe, text = "Playlist", bg="#660000",
fg = "white",font=("calibri",14,), width =19)
playlist_name.grid(row=0,column=0)

#Playlist Box
playlist_box = Listbox(playlistframe,fg="black",bg = "#990000",font=("calibri",12),width = 23,bd=0,relief="solid",highlightbackground="#660000",highlightthickness=4)
playlist_box.grid(row=1,column=0)

#Slider Frame
sliderframe = LabelFrame(root,bg = "black", fg = "black", width = 7, height = 80, bd=0,padx=10,)
sliderframe.grid(row=1,column=1)

#Slider Label
slidername = Label(sliderframe, text = "Vol",bg="#990000",font=("calibri",14,),fg="white", width=4,)
slidername.pack(side=TOP)

#Volume Slider
volumeslider = Scale(sliderframe,from_=100, to=0, orient=VERTICAL, command= music.volume, fg = "black",bg = "#990000", 
troughcolor = "black", length=150, relief="solid",highlightbackground="#660000",highlightthickness=2)
volumeslider.pack(side=BOTTOM)
volumeslider.set(70) #set default volume

# Add Song Button
add_songs = Button(root, text = "Add Song", bg="#990000",fg="white",font=("calibri",14,
"bold"),width = "16", highlightcolor="darkred",command=lambda: music.add_song(playlist_box), relief="raised")
add_songs.grid(row=5, column=4)

#Song Title Label
SongTitle = Label(root, text = "Song title", bg = "#990000", fg = "white", font=("calibri", 20), highlightbackground="black", width=30, relief="sunken")
SongTitle.grid(row=4, column=0, padx=10, pady=10)

#Song Artist Label
SongArtist = Label(root, text = "Song artist", bg = "#990000", fg = "white", font=("calibri", 20), highlightbackground="black", width=30, relief="sunken")
SongArtist.grid(row=5, column=0)

#Buttons
Buttonframe = LabelFrame(root, bg = "black", fg = "black", width = 900, height = 80, bd=0,)
Buttonframe.grid(row=6, column=0)


prev_button = Button(Buttonframe, image = prev_button_pic, bg="black", bd= 4,relief="flat", command = lambda: music.play_prev(SongTitle, SongArtist, song_image)).grid(row=0, column=0,padx=10, pady=10)
play_button = Button(Buttonframe, image = play_button_pic, bd= 4, bg="black",relief="flat", command = lambda: music.play(SongTitle, SongArtist, song_image)).grid(row=0, column=1,padx=10, pady=10)
pause_button = Button(Buttonframe, image = pause_button_pic, bd= 4, bg="black",relief="flat", command = music.pause).grid(row=0, column=2, padx=10, pady=10)
next_button = Button(Buttonframe, image = next_button_pic, bd= 4, bg="black",relief="flat",command = lambda: music.play_next(SongTitle, SongArtist, song_image)).grid(row=0, column=3, padx=10, pady=10)

root.mainloop() #window mainloop
