from math import ceil


class PhotoAlbum:

    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = self._init_photos(pages)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def _init_photos(self, pages):
        matrix = []
        for _ in range(pages):
            matrix.append([])
        return matrix

    def add_photo(self, label: str):
        pages = 0
        for page in self.photos:
            pages += 1
            if len(page) < self.PHOTOS_PER_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {pages} slot {len(page)}"
        return "No more free slots"


    def display(self):
        result = "-" * 11 + "\n"
        for page in self.photos:
            result += " ".join('[]' for x in page) + "\n"
            result += "-" * 11 + "\n"
        return result

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
