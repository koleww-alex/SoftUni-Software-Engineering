from project.computer_types.computer import Computer
from math import log2, floor, ceil


class DesktopComputer(Computer):

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        max_ram_size = 128
        available_desktop_processors = {
            'AMD Ryzen 7 5700G': 500,
            'Intel Core i5-12600K': 600,
            'Apple M1 Max': 1800,
        }

        if processor not in available_desktop_processors:
            raise ValueError(f'{processor} is not compatible with desktop computer'
                             f' {self.manufacturer} {self.model}!')

        result = log2(ram)

        if ram > max_ram_size or floor(result) != ceil(result):
            raise ValueError(f'{ram}GB RAM is not compatible with desktop computer'
                             f' {self.manufacturer} {self.model}!')
        ram_price = int(result * 100)
        processor_price = available_desktop_processors[processor]
        self.processor = processor
        self.ram = ram
        self.price = ram_price + processor_price
        return f'Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$.'
