"""..."""
# TODO: Copy your first assignment to this file, commit, then update to use Song class

from song import Song
from songcollection import SongCollection

def append_song(my_collection):
    title = title_validation()
    year = year_validation()
    genre = genre_validation()
    print("{} ({} from {}) added to songs list ".format(title, genre, year))
    my_collection.add_song(Song(title, year, genre, is_listen=False))


def title_validation():
    title = input("Title: ")
    if title.isdigit() is True:
        print("Not a valid title input. Title can not be a number")
        print("Please try again!")
        return title_validation()
    elif len(title) == 0:
        print("Not a valid title input. Title can not be blanked")
        print("Please try again!")
        return title_validation()
    else:
        print(title.strip())
    return title.strip()


def year_validation():
    global year
    current_year = 2022
    while True:
        try:
            year = int(input("Year:"))
        except ValueError:
            print("Not a valid year input. Please try again!")
            continue
        if year < 0:
            print("Not a valid year input. Year must be >= 0")
            print("Please try again!")
            continue
        elif year > current_year:
            print("Invalid year input. Movie's year cannot be more than 2022")
            print("Please try again!")
            continue
        else:
            print(year)
            break
    return int(year)


def print_list(my_collection):
    songs_listen = my_collection.get_number_listen_songs()
    songs_unlisted = my_collection.get_number_unlisted_songs()
    for i, song_data in enumerate(my_collection.songs):
        if song_data.is_listened:
            print(
                "{}. * {:<50s}   -{:5s}  ({})".format(i, song_data.title, str(song_data.year), song_data.category))
        else:
            print(
                "{}.   {:<50s}   -{:5s}  ({})".format(i, song_data.title, str(song_data.year), song_data.category))
    print("\t" + "{} songs listened, {} songs unlisted".format(songs_listen, songs_unlisted))


def genre_validation():
    while True:
        genre = input("Category: ").capitalize()
        if genre not in ("Melody", "Sad Songs", "Romantic", "Hip Hop"):
            print("Not a valid genre input.Please try again! ")
        else:
            print(genre)
            break
    return genre


def check_song(my_collection):
    for song in my_collection.songs:
        if not song.is_listened:
            return False
    return True


def songs_number(my_collection):
    global listen
    while True:
        try:
            listen = int(input(">>>"))
        except ValueError:
            print("Invalid input. Enter a valid number")
            continue
        if listen < 0:
            print("Number must be >= 0")
            continue
        elif listen >= len(my_collection.songs):
            print("Invalid song number")
        else:
            break
    return listen


def listen_song(my_collection):
    if check_song(my_collection):
        print("No songs to listen")
    else:
        print("Enter the number of songs to mark as listened")
        listen = songs_number(my_collection)
        song = my_collection.songs[listen]
        if song.is_listened:
            print("You have already listened {}".format(song.title))
        else:
            song.is_listened = True
            print("{} from {} listened".format(song.title, song.year))


def main():
    print("Songs To Listen 2.0")
    song_collection = SongCollection()
    print()
    while True:
        print("\n-----Menu-----")
        print("(L)- List songs ")
        print("(A)- Add new songs ")
        print("(W)- Watch a video song ")
        print("(Q)- Quit ")
        choice = input(">>> ").upper()
        if choice == "L":
            song_collection.sort("title")
            print_list(song_collection)
        elif choice == "A":
            append_song(song_collection)
        elif choice == "W":
            check_song(song_collection)
            listen_song(song_collection)
        elif choice == "Q":
            song_collection.save_songs("songs.csv")
            print("{} songs saved to songs.csv".format(len(song_collection.songs)))
            print("Thank you")
            break
        else:
            print("Invalid menu choice. Please try a again ")


from song import Song
