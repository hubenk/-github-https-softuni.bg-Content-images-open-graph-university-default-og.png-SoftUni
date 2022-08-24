from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if not room.is_taken:
                    if room.capacity >= people:
                        room.guests += people
                        room.is_taken = True

    def free_room(self, room_number):
        for room in self.rooms:
            if room == room_number:
                if room.is_taken:
                    room.guests = 0
                    room.is_taken = False

    def status(self):
        total_guests = 0
        taken_rooms = []
        free_rooms = []
        for room in self.rooms:
            total_guests += room.guests
            if room.is_taken:
                taken_rooms.append(room.number)
            else:
                free_rooms.append(room.number)

        result = f"Hotel {self.name} has {total_guests} total guests\n" \
                 f"Free rooms: {', '.join([str(x) for x in free_rooms])}\n" \
                 f"Taken rooms: {', '.join([str(x) for x in taken_rooms])}"

        return result
