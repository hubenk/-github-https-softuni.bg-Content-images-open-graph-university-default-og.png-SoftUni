from .song import Song


class Album:

    def __init__(self, name, *songs):
        self.name = name
        self.songs = [x for x in songs]
        self.published = False

    def add_song(self, song: Song):
        for sng in self.songs:
            if sng.name == song.name:
                return "Song is already in the album."

        if self.published:
            return "Cannot add songs. Album is published."
        elif song.single == True:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot add songs. Album is published."

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song_name)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        info = f"Album {self.name}"
        for song in self.songs:
            info += "\n"
            info += f"== {song.get_info()}"
        return info
