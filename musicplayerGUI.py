'''
Program: musicplayerGUI.py (page: 251)
Author: Alexa Ingria 6/13/22

GUI-based version of the music player app chapter 5
** Must install pygame package by running pip install pygame
** must install brezzy Python GUI
'''

from breezypythongui import EasyFrame
from pygame import mixer
from tkinter import PhotoImage
from tkinter.font import Font

# other imports

class MusicPlayer(EasyFrame):
	
	# definition of the __init__() method which is our class constructor
	def __init__(self):
		# call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Music Player GUI", background = "black", resizable = False)
		myFont = Font(family = "Impact", size = 28)
		self.addLabel(text = "Python Music Player", row = 0, column = 0, columnspan = 3, background = "black", foreground = "orange", sticky = "NSEW", font = myFont)
		# Create a label variable for the image label
		self.imageLabel = self.addLabel(text = "", row = 1, column = 0, columnspan = 3, sticky = "NSEW", background = "black")
		# Load the image into the imageLabel object
		self.image = PhotoImage(file = "music_player.png")
		self.imageLabel["image"] = self.image
		# Label and button to load the music file
		self.addLabel(text = "Enter file name to load", row = 2, column = 0, background = "black", foreground = "orange", sticky = "NE")
		self.musicFile = self.addTextField(text = "", row = 2, column = 1, width = 35)
		self.addButton(text = "Load", row = 2, column = 2, command = self.loadFile)
		# 3 buttons for the music player functions
		self.playButton = self.addButton(text = "Play", row = 3, column = 0, state = "disabled", command = self.playMusic)
		self.pauseButton = self.addButton(text = "Pause", row = 3, column = 1, state = "disabled", command = self.pauseMusic)
		self.resumeButton = self.addButton(text = "Resume", row = 3, column = 2, state = "disabled", command = self.resumeMusic)

	# Event handling methods for the command buttons
	def loadFile(self):
		# initialize the pygame mixer
		mixer.init()
		songFile = self.musicFile.getText()
		mixer.music.load(songFile)
		self.playButton["state"] = "normal"

	def playMusic(self):
		# play the previously loaded music file
		mixer.music.play()
		self.pauseButton["state"] = "normal"

	def pauseMusic(self):
		# pause the current song
		mixer.music.pause()
		self.pauseButton["state"] = "disabled"
		self.resumeButton["state"] = "normal"

	def resumeMusic(self):
		# take song out of pause mode
		mixer.music.unpause()
		self.pauseButton["state"] = "normal"
		self.resumeButton["state"] = "disabled"
	
# definition of the main() method which will establish class objects
def main():
	# instantiate an object from the class into mainloop()
	MusicPlayer().mainloop()

# global call to the main() method
main()