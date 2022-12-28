from project.supply.drink import Drink
from project.supply.food import Food


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_player(self, player_name: str):
        player = [p for p in self.players if p.name == player_name][0]
        if player:
            return player

        return False

    def add_player(self, *args):
        players_to_add = []

        for player in args:
            if player not in self.players:
                self.players.append(player)
                players_to_add.append(player.name)

        return f'Successfully added: {", ".join(players_to_add)}'

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player(player_name)
        food_supplies = [s for s in self.supplies if isinstance(s, Food)]
        drink_supplies = [s for s in self.supplies if isinstance(s, Drink)]
        valid_supplies = ['Food', 'Drink']

        if player and sustenance_type in valid_supplies:

            if player.stamina == 100:
                return f'{player_name} have enough stamina.'

            if sustenance_type == 'Food' and not food_supplies:
                raise Exception('There are no food supplies left!')

            if sustenance_type == 'Drink' and not drink_supplies:
                raise Exception('There are no drink supplies left!')

            if sustenance_type == 'Food':
                supply_used = food_supplies[-1]
            else:
                supply_used = drink_supplies[-1]

            if player.stamina + supply_used.energy > 100:
                player.stamina = 100
            else:
                player.stamina += supply_used.energy

            for i in range(len(self.supplies) - 1, -1, -1):
                supply = self.supplies[i]
                if supply == supply_used:
                    self.supplies.pop(i)
                    break

            return f'{player_name} sustained successfully with {supply_used.name}.'

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)

        if first_player.stamina == 0 and second_player.stamina == 0:
            output = [
                f'Player {first_player_name} does not have enough stamina.',
                f'Player {second_player_name} does not have enough stamina.'
            ]
            return '\n'.join(output)

        elif first_player.stamina == 0:
            return f'Player {first_player_name} does not have enough stamina.'

        elif second_player.stamina == 0:
            return f'Player {second_player_name} does not have enough stamina.'

        first_attacker = first_player if first_player.stamina < second_player.stamina else second_player
        second_attacker = second_player if first_attacker == first_player else first_player

        if second_attacker.stamina - (first_attacker.stamina / 2) <= 0:
            second_attacker.stamina = 0
            return f'Winner: {first_attacker.name}'
        else:
            second_attacker.stamina -= first_attacker.stamina / 2

        if first_attacker.stamina - (second_attacker.stamina / 2) <= 0:
            first_attacker.stamina = 0
            return f'Winner: {second_attacker.name}'
        else:
            first_attacker.stamina -= second_attacker.stamina / 2

        winner = first_attacker if first_attacker.stamina > second_attacker.stamina else second_attacker
        return f'Winner: {winner.name}'

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        output = []

        for player in self.players:
            output.append(str(player))

        for supply in self.supplies:
            output.append(supply.details())

        return '\n'.join(output)



# controller = Controller()
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.add_player(first_player, second_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
# print(controller)
