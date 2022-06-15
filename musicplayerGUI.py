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
	#"ApplicationName" will change from project to project

	#definition of the __init__() method whitch is our class constructor
	def __init__(self):
		#call the EasyFrame version of __init__
		EasyFrame.__init__(self, title = "Music Player GUI", background = "black", resizable = false)
		myFont = Font(family = "Impact", size = 28)
		self.addLabel(title = "Python Music Player", row = 0, column = 0, colunmspan = 3, background = "black", foreground = "orange", sticky = "NSEW", front = myFont)
		# create a lable variable for the image label
		self.imageLabel = self.addLabel(text = "", column = 0, colunmspan = 3, sticky = "NSEW", background = "black")
		#load the image into the image imageLabel object
		self.image = PhotoImage(file = "musicplayer.png")
		self.imageLable["image"] = self.image
		#label and button to load the music file
		self.addLabel(text = " Enter file name to load", row = 2, column = 0, background = "black", foreground = " orange")
		self.musicFile = self.addTextField(text ="", row = 2, column = 1, width = 25)
		self.addButton(text = "Load", row = 2, column = 2. command = self.loadFile)


		# 3 button for the music player function
		self.playButton = self.addButton(text = 3, column = 0, state = "disabled")
		self.pauseButton = self.Button(text = " Pause", row = 3, column = 1, state = "disabled")
		self.resumeButton = self.addButton(text = "Resume", row =3, column = 2, state = "disabled")

		#Event handing method for the command buttons
		def loadFile(self): 
			#initalize the pygame mixer
			mixer.init()
			songFile = self.musicFile.getText()
			mixer.music.load(songFile)
			self.playButton["state"] = "normal"

		def playMusic(self):
			#play the prevously music file
			mixer.music.play()
			self.pauseButton["state"] = "normal"



# definition of the main() method which will establish class odject
def main():
	#instantiate an object from the class into mainloop()
	MusicPlayer().mainloop()

#global call to the main() method
main()

