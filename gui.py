from tkinter import * 
from app import *


main_window = Tk(className='iMessage Bot')
main_window.geometry("500x300")
main_window.resizable(False, False)

#Title Label
title_label = Label(main_window, text="iMessage Bot")
title_label.grid(row=0, column=4,padx=5, pady=5)

#Artist Input
Label(main_window, text="Artist Name:").grid(row=1, column=3, padx=5, pady=5)
artist_input = Entry(main_window,bd=1)
artist_input.grid(row=1, column=4, padx=5, pady=5)

#Song Input
Label(main_window, text="Song Name:").grid(row=2, column=3, padx=5, pady=5)
song_input = Entry(main_window, bd=1)
song_input.grid(row=2, column=4, padx=5, pady=5)

#Phone Number Input
Label(main_window, text="Phone Number:").grid(row=3, column=3, padx=5, pady=5)
num_input = Entry(main_window, bd=1)
num_input.grid(row=3, column=4, padx=5, pady=5)

def executeApp():
    if len(artist_input.get()) != 0 and len(song_input.get()) != 0 and len(num_input.get()) != 0:
        name = get_song_lyrics(artist_input.get(), song_input.get())
        new_str = open_file(name)
        send_messages(get_lyric_word(new_str), num_input.get())

#Send button 
send_bttn = Button(main_window, text="Send Lyrics", command = executeApp)
send_bttn.grid(row=4, column=4, padx=5, pady=5)



main_window.mainloop()