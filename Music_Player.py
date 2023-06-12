from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title('Music Player')
root.geometry("500x300")

pygame.mixer.init()

menubar= Menu(root)
root.config(menu=menubar)

songs =[]
current_song = ""
paused = False

def load_music():
	global current_song
	root.directory = filedialog.askdirectory()

	for song in os.listdir(root.directory):
		name, ext= os.path.splitext(song)
		if ext == '.mp3':
			songs.append(song)

	for song in songs:
		songlist.insert("end", song)
	
	songlist.selection_set(0)
	current_song = songs[songlist.curselection()[0]]		

def play_music():
	global current_song, paused

	if not paused:
		pygame.mixer.load_music(os.path.join(root.askdirectory, current_song))
		pygame.mixer.music.play()
	else:
		pygame.mixer.music.unpause()
		paused = False
			

def pause_music():
	global paused
	pygame.mixer.music.paused()
	paused = True

def next_music():
	global current_song, paused
	try:
		songlist.selection_clear(0,END)
		songlist.selection_set(songs.index(current_song) + 1)
		current_song = songs[songlist.curselection()[0]]
		play_music()
	except:
		pass

def prev_music():
	global current_song, paused

	try:
		songlist.selection_clear(0,END)
		songlist.selection_set(songs.index(current_song) - 1)
		current_song = songs[songlist.curselection()[0]]
		play_music()

	except:
		pass


organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder', command=load_music	)
menubar.add_cascade(label='organise', menu=organise_menu)

songlist = Listbox(root, bg="white", fg="black", width=100, height=12)
songlist.pack(pady=10)

play_btn_img = PhotoImage(file='//put your location here//play.png')
pause_btn_img = PhotoImage(file='//put your location here//pause.png')
next_btn_img = PhotoImage(file='//put your location here//next.png')
prev_btn_img = PhotoImage(file='//put your location here//previous.png')

controls_frame = Frame(root)
controls_frame.pack()

play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play_music)
pause_btn = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=pause_music)
next_btn = Button(controls_frame, image=next_btn_img, borderwidth=0, command=next_music)
prev_btn = Button(controls_frame, image=prev_btn_img, borderwidth=0, command=prev_music)

play_btn.grid(row=0, column= 1, padx=7, pady=10)
pause_btn.grid(row=0, column= 2, padx=7, pady=10)
next_btn.grid(row=0, column= 3, padx=7, pady=10)
prev_btn.grid(row=0, column= 0, padx=7, pady=10)


root.mainloop()
