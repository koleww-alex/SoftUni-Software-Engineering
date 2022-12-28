from structure_and_functionality.project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON_TO_RESERVE = 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        price = number_of_people * PrivateBooth.PRICE_PER_PERSON_TO_RESERVE
        self.price_for_reservation = price
        self.is_reserved = True
