from First_steps_in_OOP.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f'This pokemon is already caught'
        else:
            self.pokemons.append(pokemon)
            return f'Caught {Pokemon.pokemon_details(pokemon)}'

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemons:
            if p.name == pokemon_name:
                self.pokemons.remove(p)
                return f'You have released {pokemon_name}'

        return 'Pokemon is not caught'

    def trainer_data(self):
        output = [f'Pokemon Trainer {self.name}', f'Pokemon count {len(self.pokemons)}']
        for p in self.pokemons:
            output.append(f'- {Pokemon.pokemon_details(p)}')

        return '\n'.join(output)

