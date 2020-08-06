import lyricsgenius
from py_imessage import imessage 
from time import sleep
from token_file import token

#gives access to Genius API to grab lyrics 
genius = lyricsgenius.Genius(token)
#removes the "Chorus" labels from the lyrics 
genius.remove_section_headers = True

#opens the lyric file and turns it into a string
def open_file(file_name):
    with open(file_name) as file:
        list = [line.strip() for line in file]
        string = " ".join(list)
        return string

#splits the string into single words inside a string array
def get_lyric_word(lyric_string):
    return lyric_string.split()

#goes through the whole array and sends the messages to the specific number
def send_messages(messages, phone_num):
    for message in messages:
        send_actual_message(message, phone_num)
        sleep(.15)

#takes in phone number and message and sends it to user
def send_actual_message(messsage, phone_num):
    imessage.send(phone_num, messsage)

#gets the song lyrics from the genius api and returns the file name that was made
def get_song_lyrics(name, song_name):
    song = genius.search_song(song_name, name)
    song.save_lyrics(song.title, 'txt')
    file_name = song.title + ".txt"
    return file_name

#asks users for artist name, song, and number then calls respective methods 
def main():
    print("Enter artist name")
    artist_name = input()
    print("Enter song name by the artist")
    song_name = input()
    print("What number do you want to send this to?")
    phone_num = input()
    name = get_song_lyrics(artist_name, song_name)
    new_str = open_file(name)
    send_messages(get_lyric_word(new_str), phone_num)


main()