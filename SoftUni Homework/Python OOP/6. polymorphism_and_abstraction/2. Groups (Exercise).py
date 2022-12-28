class Person:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        merged_person = Person(self.name, other.surname)
        return merged_person


class Group:

    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        merged_group = Group(f'{self.name} {other.name}', self.people + other.people)
        return merged_group

    def __str__(self):
        return f'Group {self.name} with members {", ".join(str(x) for x in self.people)}'

    def __getitem__(self, index):
        return f'Person {index}: {str(self.people[index])}'
