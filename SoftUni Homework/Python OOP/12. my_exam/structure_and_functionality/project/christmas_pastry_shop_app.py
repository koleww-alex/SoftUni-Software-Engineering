from structure_and_functionality.project.booths.open_booth import OpenBooth
from structure_and_functionality.project.booths.private_booth import PrivateBooth
from structure_and_functionality.project.delicacies.gingerbread import Gingerbread
from structure_and_functionality.project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def __find_booth(self, booth_number: int):
        booth = [b for b in self.booths if b.booth_number == booth_number]
        if booth:
            return booth[0]

        return False

    def __find_delicacy(self, delicacy_name: str):
        delicacy = [d for d in self.delicacies if d.name == delicacy_name]
        if delicacy:
            return delicacy[0]

        return False

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if name in [d.name for d in self.delicacies]:
            raise Exception(f'{name} already exists!')

        if type_delicacy == 'Gingerbread':
            gingerbread = Gingerbread(name, price)
            self.delicacies.append(gingerbread)
            return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

        elif type_delicacy == 'Stolen':
            stolen = Stolen(name, price)
            self.delicacies.append(stolen)
            return f'Added delicacy {name} - {type_delicacy} to the pastry shop.'

        else:
            raise Exception(f'{type_delicacy} is not on our delicacy menu!')

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if booth_number in [b.booth_number for b in self.booths]:
            raise Exception(f'Booth number {booth_number} already exists!')

        if type_booth == 'Open Booth':
            open_booth = OpenBooth(booth_number, capacity)
            self.booths.append(open_booth)
            return f'Added booth number {booth_number} in the pastry shop.'

        elif type_booth == 'Private Booth':
            private_booth = PrivateBooth(booth_number, capacity)
            self.booths.append(private_booth)
            return f'Added booth number {booth_number} in the pastry shop.'

        else:
            raise Exception(f'{type_booth} is not a valid booth!')

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f'Booth {booth.booth_number} has been reserved for {number_of_people} people.'

        raise Exception(f'No available booth for {number_of_people} people!')

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth(booth_number)
        if not booth:
            raise Exception(f'Could not find booth {booth_number}!')

        delicacy = self.__find_delicacy(delicacy_name)
        if not delicacy:
            raise Exception(f'No {delicacy_name} in the pastry shop!')

        booth.delicacy_orders.append(delicacy)
        return f'Booth {booth_number} ordered {delicacy_name}.'

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth(booth_number)
        total_bill = 0

        total_bill += booth.price_for_reservation
        for delicacy in booth.delicacy_orders:
            total_bill += delicacy.price

        self.income += total_bill
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False
        output = [f'Booth {booth_number}:', f'Bill: {total_bill:.2f}lv.']

        return '\n'.join(output)

    def get_income(self):
        return f'Income: {self.income:.2f}lv.'


# shop = ChristmasPastryShopApp()
# print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
# print(shop.delicacies[0].details())
# print(shop.add_booth("Open Booth", 1, 30))
# print(shop.add_booth("Private Booth", 10, 5))
# print(shop.reserve_booth(30))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.reserve_booth(5))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.order_delicacy(1, "Gingy"))
# print(shop.leave_booth(1))
# print(shop.get_income())
