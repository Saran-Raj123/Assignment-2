"""..."""


# TODO: Create your SongCollection class in this file

from operator import attrgetter
from song import Song
import csv

class SongCollection:
    def __init__(self):
        super().__init__()
        songs = []
        self.songs = songs

    def add_songs(self, song):
        self.songs.append(song)

    def get_number_listen_song(self):
        unlisted_count = 0
        for song in self.songs:
            if song.is_listened:
                unlisted_count += 1
        return unlisted_count

    def get_number_unlisted_songs(self):
        listen_count = 0
        for song in self.songs:
            if not song.is_listened:
                listen_count += 1
        return listen_count

    def load_songs(self, file_name):
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            list_songs = list(reader)
            for song in list_songs:
                self.songs.append(Song(title=song[0], year=int(song[1]), category=song[2]
                                        , is_listen="w" in song[3]))

    def save_songs(self, file_name):
        # save songs
        with open(file_name, "w", newline="") as csv_file:
            list_songs = csv.writer(csv_file)
            for song in self.songs:
                list_songs.writerow([song.title, song.year, song.category, "w" if song.is_listened else "u"])

    def sort(self, key):
        self.songs.sort(key=attrgetter(key))

    def __str__(self):
        for song in self.songs:
            print(song)
        return ""

    pass
