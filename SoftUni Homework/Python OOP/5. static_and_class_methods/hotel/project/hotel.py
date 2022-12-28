from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        for room in self.rooms:
            if room.number == room_number:
                if not room.is_taken and room.capacity >= people:
                    room.is_taken = True
                    room.guests = people

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken:
                    room.is_taken = False
                    room.guests = 0

    def status(self):
        for room in self.rooms:
            self.guests += room.guests
        return f'Hotel {self.name} has {self.guests} total guests\n' \
               f'Free rooms: {", ".join(str(r.number) for r in self.rooms if not r.is_taken)}\n' \
               f'Taken rooms: {", ".join(str(r.number) for r in self.rooms if r.is_taken)}'
