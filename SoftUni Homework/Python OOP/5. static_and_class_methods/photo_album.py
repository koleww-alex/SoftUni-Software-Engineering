from math import ceil


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label: str):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                slot_used = len(self.photos[i])

                return f'{label} photo added successfully on page {i + 1} slot {slot_used}'

        return 'No more free slots'

    def display(self):
        output = ['-' * 11]

        for i in range(len(self.photos)):
            output.append(('[] ' * len(self.photos[i])).rstrip())
            output.append('-' * 11)

        return '\n'.join(output)
