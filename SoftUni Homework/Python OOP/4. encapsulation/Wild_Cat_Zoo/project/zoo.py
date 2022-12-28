from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return 'Not enough budget'

        if self.__budget >= price and self.__animal_capacity == len(self.animals):
            return 'Not enough space for animal'

        self.animals.append(animal)
        self.__budget -= price

        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return 'Not enough space for worker'

        self.workers.append(worker)
        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salaries = sum([w.salary for w in self.workers])

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        total_maintenance = sum([a.money_for_care for a in self.animals])

        if self.__budget >= total_maintenance:
            self.__budget -= total_maintenance
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        output = [f'You have {len(self.animals)} animals']

        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        output.append(f'----- {len(lions)} Lions:')
        output.extend([str(l) for l in lions])

        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        output.append(f'----- {len(tigers)} Tigers:')
        output.extend([str(t) for t in tigers])

        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        output.append(f'----- {len(cheetahs)} Cheetahs:')
        output.extend([str(c) for c in cheetahs])

        return '\n'.join(output)

    def workers_status(self):
        output = [f'You have {len(self.workers)} workers']

        keepers = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        output.append(f'----- {len(keepers)} Keepers:')
        output.extend([str(k) for k in keepers])

        care_takers = [ct for ct in self.workers if ct.__class__.__name__ == 'Caretaker']
        output.append(f'----- {len(care_takers)} Caretakers:')
        output.extend([str(ck) for ck in care_takers])

        vets = [v for v in self.workers if v.__class__.__name__ == 'Vet']
        output.append(f'----- {len(vets)} Vets:')
        output.extend([str(v) for v in vets])

        return '\n'.join(output)
