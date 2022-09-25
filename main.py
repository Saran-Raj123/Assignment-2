"""
Name: Saranraj Saravanan
Date:25/09/2022
Brief Project Description:
GitHub URL:
"""
# TODO: Create your main program in this file, using the SongsToLearnApp class

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from songcollection import SongCollection
from song import Song


class SongsToLearnApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.song_collection = SongCollection()
        self.song = []

    def build(self):
        self.title = "Songs to Listen 2.0"
        self.print_songs()
        self.root = Builder.load_file("app.kv")
        self.song_collection.load_song("songs.csv")
        self.print_songs()
        self.count_unlisted_listen_songs()
        self.sort_list("title")
        return self.root


    def on_start(self):
        self.song_collection.load_song("songs.csv")
        self.print_songs()
        self.count_unlisted_listen_songs()
        self.sort_list("title")

    def sort_list(self, key):
        self.song_collection.sort(key)
        self.update_song()

    def count_unlisted_listen_song(self):
        # get number of listen and unlisted songs
        self.root.ids.song_status.text = "To listen: " \
                                          + str(self.song_collection.get_number_unlisted_songs()) \
                                          + " Listened: " + str(self.song_collection.get_number_listen_songs())

    def print_songs(self):
        self.song = self.song_collection.songs
        for song in self.song:
            if song.is_listened:
                song_button = Button(text="{} ({} from {}) listened".format(song.title, song.category, song.year))
                song_button.background_color = (51, 102, 0, 0.2)
            else:
                song_button = Button(text="{} ({} from {}) ".format(song.title, song.category, song.year))
                song_button.background_color = (0, 102, 153, 0.2)
            song_button.song = song
            song_button.bind(on_press=self.listen_song)
            self.root.ids.entry_box.add_widget(song_button)

    def title_validation(self, input_title):
        if not input_title.strip():
            self.pop_up_message("Your title must not be blank")
        else:
            return input_title

    def year_validation(self):
        try:
            current_year = 2022
            year = int(self.root.ids.input_year.text)
            if year < 0:
                raise ValueError
            elif year > current_year:
                raise ValueError
            return int(year)
        except ValueError:
            self.pop_up_message("Not a valid year input. Please try again!")

    def genre_validation(self):
        category = self.root.ids.input_category.text
        if category in ["Romantic", "melody", "Rock", "rap", "pop"]:
            return category
        else:
            self.pop_up_message("Invalid Category.Please try again")

    def add_song(self, title, category, year):
        if title and category and year:
            title_check = self.title_validation(title)
            category_check = self.genre_validation()
            year_check = self.year_validation()
            if title_check and category_check and year_check:
                separator = " "
                pretty_title_before = separator.join(title_check.split())
                pretty_title_after = pretty_title_before.title()
                self.song_collection.add_song(Song(pretty_title_after, year_check, category_check))
                self.print_songs()
                self.pop_up_message("{} has been added to song list".format(pretty_title_after))
                self.clear_add_song()
                self.update_song()
                self.count_unlisted_listen_songs()
        else:
            self.pop_up_message("Fill in all the fields")

    def listen_song(self, instance):
        right_now_song = instance.song
        if right_now_song.is_listened:
            self.root.ids.output_message.text = "You need to listen {}".format(right_now_song.title)
        else:
            self.root.ids.output_message.text = "You have unlisted {}".format(right_now_song.title)
        right_now_song.is_listened = not right_now_song.is_listened
        self.count_unlisted_watch_songs()
        self.update_song()

    def update_song(self):
        self.root.ids.entry_box.clear_widgets()
        self.print_songs()

    def pop_up_message(self, text):
        """display a pop-up message"""
        self.root.ids.show_message.text = text
        self.root.ids.popup.open()

    def close_pop_up_message(self):
        """Dismiss the pop-up message"""
        self.root.ids.show_message.text = " "
        self.root.ids.popup.dismiss()

    def clear_add_song(self):
        """Clear the text input"""
        self.root.ids.input_title.text = ""
        self.root.ids.input_year.text = ""
        self.root.ids.input_category.text = ""

    def on_stop(self):
        self.song_collection.save_song("songs.csv")

    pass


if __name__ == '__main__':
    SongsToLearnApp().run()
