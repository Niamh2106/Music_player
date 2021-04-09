# Music_player by Ayotomiwa Adekunle, Ife Makinde and Niamh Osasu Idehen

This is a simple music player that can play songs from a playlist aswell as add songs to this playlist.
It can also change the volume of the song.

The two main modules aside from the module we created ourselves are **tkinter** and **pygame**.
Tkinter is a module allows you to create a program with a graphical user interface.
Pygame allows you to create games but for the purpose of this project we are only using its music features.

The **main.py** consists of the tkinter code (i.e all the graphics that displayed)
The **music.py** is a module we created for the various functions we have.

## **Instructions**
1. Any song that you want to add will need to have the following format: artist - songname eg. Coldplay - Paradise. Simply rename your song in that format.
   This is not necessary but is recommended for the best experience.
   There are already some songs that you can test the program with in the songs folder.
2. If you want a certain image to be displayed along with a song then rename the image to match the song name and put it in the **images folder**
   i.e if the song is called Paradise then likewise the image should be called Paradise. We have done this for three of the images. 
3. You must make sure pygame is installed on your device, tkinter comes with Python so there is no need to install it.

### How to install pygame:
**Windows:**
  * pip install pygame

**Mac or Linux:**
  * python3 -m pip install -U pygame --user

## **Note:**
* Please make sure an audio device is connected to your device before you run the program.
* It is best to run the program from an editor or command prompt, some bash shells are not capable of accesing a computer's
  audio device, therefore the program will not run.
* Only .png images can be used for the song image.
* Only .mp3 songs can be played.
* **You cannot select a song by clicking it in the playlist, songs are played in the order they were added to the playlist.**
