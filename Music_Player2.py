import tkinter  # library for gui window
import copy
import tkinter.messagebox
import os
from tkinter import ttk  # for extended feature of tkinter
from PIL import Image, ImageTk
from pygame import mixer  # for music sound handling

root = tkinter.Tk()  # window page create here
root.title("Music Player")  # give title to your music player
root.geometry("1200x700")  # set default geomatry
root.iconbitmap(r'music_icon2.ico')  # add icon for your player
menubar = tkinter.Menu(root)  # creation of menu bar
root.config(menu=menubar)  # set menu bar
submenu = tkinter.Menu(menubar, tearoff=0)  # set sub menu in menubar
songs_list = []
mixer.init()  # to initialise the mixer module for their use
list_box = []  # music list create name inside root window
a = 0  # make variable for curser position
i = 0  # variable for taking song index from song_list

statusBar = tkinter.Label(root, text="Welcome in the world of music", relief='sunken', font='bold',
                          anchor='w')  # status for showing your current player status
statusBar.pack(side="bottom", fill='both') # bind up in pack and put status bar on your root window


def about_us():
    tkinter.messagebox.showinfo('Information', 'This is beta version')


song = 0
playing_Photo = ImageTk.PhotoImage(Image.open('playing.jpg'))
relax_Photo = ImageTk.PhotoImage(Image.open('relax.jpg'))
label = tkinter.Label(root, image=relax_Photo)
label.pack(side='left', fill='y')


def music_list():
    global songs
    global song
    global list_box
    list_box = tkinter.Listbox(bg_label, height=25, width=85, font='bold', selectmode='single')
    list_box.pack()
    music_dir = "path where your music store in your system"
    os.chdir(music_dir)
    songs = os.listdir(music_dir)
    for items in range(len(songs)):
        if songs[items].endswith('.mp3'):
            list_box.insert(items, songs[items])
    for items in songs:
        if items.endswith('.mp3'):
            songs_list.append(items)
    song = list_box.curselection()


play = False
paused = False


def music_play():
    global a
    global paused
    global play
    global list_box
    if play:
        if paused:
            label.config(image=playing_Photo)
            playBtn.config(image=play_Photo)
            mixer.music.unpause()
            statusBar['text'] = "Music now playing"
            paused = False
            play = False

        else:
            label.config(image=relax_Photo)
            playBtn.config(image=pause_Photo)
            mixer.music.pause()
            statusBar['text'] = "Music Pause now!"
            paused = True

    else:
        try:
            global i
            a = list_box.curselection()
            label.config(image=playing_Photo)
            mixer.music.load(list_box.get(a))
            mixer.music.play()
            statusBar['text'] = "Music now playing" + "-" + list_box.get(a)
            i = list(copy.copy(a))
            for x in i:
                i = x
            play = True

        except:
            tkinter.messagebox.showerror('Error', 'File not found')



def vol_manage(v):
    vol = int(v) / 100  # range 0-1
    mixer.music.set_volume(vol)  # mixer set_volume function value range between 0 and 1



def next_song():
    global i
    global play
    global a
    i += 1
    mixer.music.load(songs_list[i])
    mixer.music.play()
    play = True
    statusBar['text'] = "Music now playing" + "-" + songs_list[i]


def previous_song():
    global i
    global play
    i -= 1
    mixer.music.load(songs_list[i])
    mixer.music.play()
    play = True
    statusBar['text'] = "Music now playing" + "-" + songs_list[i]


mute = False  # music play and don't click on mute button


def unmute_music():
    global mute
    if mute:  # unmute
        mixer.music.set_volume(0.35)
        unmuteBtn.configure(image=unmute_photo)
        vol_scale.set(35)
        statusBar['text'] = 'Music now Unmuted!'
        mute = False
    else:  # mute
        mixer.music.set_volume(0)
        unmuteBtn.configure(image=mute_photo)
        vol_scale.set(0)
        statusBar['text'] = 'Music now Muted!'
        mute = True


frame1 = tkinter.Frame(root, relief='raised')
frame1.pack(side='bottom')

frame2 = tkinter.Frame(root, relief='raised')
frame2.pack(side='bottom')

button_label = tkinter.Label(root, bg='light yellow')
button_label.pack(side='bottom')

bg_Photo = ImageTk.PhotoImage(Image.open('bg_image1.jpg'))
bg_label = ttk.Label(root, image=bg_Photo, anchor='ne')
bg_label.pack(side='right')

menubar.add_cascade(label="My Music", menu=submenu)  # to create name and widget for submenubar
submenu.add_checkbutton(label="music", command=music_list)  # cascsde menu
submenu.add_checkbutton(label="Exit", command=root.destroy)

submenu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_checkbutton(label="About us", command=about_us)

pause_Photo = ImageTk.PhotoImage(Image.open("music_pause.png"))
play_Photo = ImageTk.PhotoImage(Image.open("play_music2.png"))  # to open photo
playBtn = tkinter.Button(button_label, image=play_Photo, anchor='w', command=music_play)
playBtn.grid(row=0, column=1, padx=5)


vol_scale = tkinter.Scale(frame2, from_=0, to=100, orient='horizontal', fg='red', length=280, width=10,
                          command=vol_manage)  # to make volume controller
vol_scale.set(35)  # it set value 35 initially
mixer.music.set_volume(0.35)  # it set volume 35
vol_scale.grid(row=0, column=0, padx=10)


mute_photo = ImageTk.PhotoImage(Image.open("mute.png"))
unmute_photo = ImageTk.PhotoImage(Image.open("unmute.jpg"))
unmuteBtn = tkinter.Button(frame2, image=unmute_photo, anchor='w', command=unmute_music)
unmuteBtn.grid(row=0, column=1, padx=5)

next_photo = ImageTk.PhotoImage(Image.open("next.png"))
nextBtn = tkinter.Button(button_label, image=next_photo, command=next_song)
nextBtn.grid(row=0, column=2, padx=5)

previous_photo = ImageTk.PhotoImage(Image.open("previous.png"))
previousBtn = tkinter.Button(button_label, image=previous_photo, command=previous_song)
previousBtn.grid(row=0, column=0, padx=5)
root.mainloop()
