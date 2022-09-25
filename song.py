"""..."""


# TODO: Create your Song class in this file


class Song:

        def __init__(self, title="", year=0, category="", is_listen=False):
            self.title = title
            self.category = category
            self.year = year
            self.is_listened = is_listen

        def __str__(self):
            return "{} - {} ({}) ({})".format(self.title, self.year, self.category,
                                              self.check_listen())

        def check_listen(self):
            """Changing song to listen"""
            if self.is_listened:
                return "listened"
            return "unlisted"


