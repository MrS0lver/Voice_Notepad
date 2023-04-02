import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import speech_recognition as sr

class Notepad:

	__root = Tk()

	# default window width and height
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(__root)
	__thisMenuBar = Menu(__root)
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0)
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
	
	# To add scrollbar
	__thisScrollBar = Scrollbar(__thisTextArea)	
	__file = None

	def __init__(self,**kwargs):

		# Set icon
		try:
				self.__root.wm_iconbitmap("Notepad.ico")
		except:
				pass

		# Set window size (the default is 300x300)

		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			pass

		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			pass

		# Set the window text
		self.__root.title("Untitled - Notepad")

		# Center the window
		screenWidth = self.__root.winfo_screenwidth()
		screenHeight = self.__root.winfo_screenheight()
	
		# For left-align
		left = (screenWidth / 2) - (self.__thisWidth / 2)
		
		# For right-align
		top = (screenHeight / 2) - (self.__thisHeight /2)
		
		# For top and bottom
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
											self.__thisHeight,
											left, top))

		# To make the textarea auto resizable
		self.__root.grid_rowconfigure(0, weight=1)
		self.__root.grid_columnconfigure(0, weight=1)

		# Add controls (widget)
		self.__thisTextArea.grid(sticky = N + E + S + W)
		
		# To open new file
		self.__thisFileMenu.add_command(label="New",
										command=self.__newFile)
		
		# To open a already existing file
		self.__thisFileMenu.add_command(label="Open",
										command=self.__openFile)
		
		# To save current file
		self.__thisFileMenu.add_command(label="Save",
										command=self.__saveFile)

		# To create a line in the dialog	
		self.__thisFileMenu.add_separator()										
		self.__thisFileMenu.add_command(label="Exit",
										command=self.__quitApplication)
		self.__thisMenuBar.add_cascade(label="File",
									menu=self.__thisFileMenu)	
		
		# To give a feature of cut
		self.__thisEditMenu.add_command(label="Cut",
										command=self.__cut)			
	
		# to give a feature of copy
		self.__thisEditMenu.add_command(label="Copy",
										command=self.__copy)		
		
		# To give a feature of paste
		self.__thisEditMenu.add_command(label="Paste",
										command=self.__paste)		
		
		# To give a feature of editing
		self.__thisMenuBar.add_cascade(label="Edit",
									menu=self.__thisEditMenu)	
		
		# To create a feature of description of the notepad
		self.__thisHelpMenu.add_command(label="About Notepad",
										command=self.__showAbout)
		self.__thisMenuBar.add_cascade(label="Help",
									menu=self.__thisHelpMenu)

		self.__root.config(menu=self.__thisMenuBar)

		self.__thisScrollBar.pack(side=RIGHT,fill=Y)				
		
		# Scrollbar will adjust automatically according to the content	
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
	