import tkinter as tk
import music

root = tk.Tk()

#Load images
play_button_pic = tk.PhotoImage(file = "images/play_button.png")
next_button_pic = tk.PhotoImage(file = "images/next_button.png")
prev_button_pic = tk.PhotoImage(file = "images/prev_button.png")

prev_button = tk.Button(root, image = prev_button_pic, command = music.play_prev()).grid(row=0, column=0)
play_button = tk.Button(root, image = play_button_pic, command = music.play()).grid(row=0, column=1)
next_button = tk.Button(root, image = next_button_pic, command = music.play_next()).grid(row=0, column=2)


root.mainloop()