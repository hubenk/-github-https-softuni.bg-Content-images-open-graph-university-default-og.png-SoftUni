from .album import Album


class Band:

    albums = []

    def __init__(self, name):
        self.name = name

    def add_album(self, album: Album):
        for album in Band.albums:
            if album == album.name:
                return f"Band {self.name} already has {album} in their library."
        Band.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album in Band.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                Band.albums.remove(album_name)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}"
        for album in Band.albums:
            result += "\n"
            result += Album.details(album)
        return result
