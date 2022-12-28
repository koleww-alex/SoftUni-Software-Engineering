class SteamUser:
    def __init__(self, name: str, games: list):
        self.username = name
        self.games = games
        self.played_hours = 0

    def play(self, game: str, hours_played: int):
        if game in self.games:
            self.played_hours += hours_played
            return f'{self.username} is playing {game}'

        return f'{game} is not in library'

    def buy_game(self, game: str):
        if game not in self.games:
            self.games.append(game)
            return f'{self.username} bought {game}'
        return f'{game} is already in your library'

    def status(self):
        return f'{self.username} has {len(self.games)} games. Total play time: {self.played_hours}'
