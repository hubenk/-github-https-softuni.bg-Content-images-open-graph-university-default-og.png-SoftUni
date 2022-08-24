### Разминаването с джъдж идва от това, че матрицата се създава динамично, а той иска да се създаде от самото начало.###


from math import ceil


class PhotoAlbum:

    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[]]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        if len(self.photos[-1]) < self.PHOTOS_PER_PAGE:
            self.photos[-1].append(label)
            page = len(self.photos)
            slot = len(self.photos[-1])
            if len(self.photos[-1]) == self.PHOTOS_PER_PAGE and len(self.photos) < self.pages:
                self.photos.append([])
            elif len(self.photos[-1]) == self.PHOTOS_PER_PAGE and len(self.photos) == self.pages:
                return "No more free slots"
            return f"{label} photo added successfully on page {page} slot {slot}"

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
