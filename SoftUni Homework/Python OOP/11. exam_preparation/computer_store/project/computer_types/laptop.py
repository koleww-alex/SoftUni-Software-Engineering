from project.computer_types.computer import Computer
from math import log2, floor, ceil


class Laptop(Computer):

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        max_ram_size = 64
        available_laptop_processors = {
            'AMD Ryzen 9 5950X': 900,
            'Intel Core i9-11900H': 1050,
            'Apple M1 Pro': 1200,
        }

        if processor not in available_laptop_processors:
            raise ValueError(f'{processor} is not compatible with laptop {self.manufacturer} {self.model}!')

        result = log2(ram)
        if ram > max_ram_size or floor(result) != ceil(result):
            raise ValueError(f'{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!')

        ram_price = int(result * 100)
        processor_price = available_laptop_processors[processor]
        self.processor = processor
        self.ram = ram
        self.price = ram_price + processor_price
        return f'Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$.'
