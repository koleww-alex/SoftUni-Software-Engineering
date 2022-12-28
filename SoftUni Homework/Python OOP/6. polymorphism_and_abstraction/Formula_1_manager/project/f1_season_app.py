from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        valid_teams = ['Red Bull', 'Mercedes']

        if team_name not in valid_teams:
            raise ValueError('Invalid team name!')

        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)
            return f'Red Bull has joined the new F1 season.'
        else:
            self.mercedes_team = MercedesTeam(budget)
            return f'Mercedes has joined the new F1 season.'

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise Exception('Not all teams have registered for the season.')

        team_ahead = 'Red Bull' if red_bull_pos < mercedes_pos else 'Mercedes'

        red_bull_revenue = self.red_bull_team.calculate_revenue_after_race(red_bull_pos)
        mercedes_revenue = self.mercedes_team.calculate_revenue_after_race(mercedes_pos)

        return f'Red Bull: {red_bull_revenue}. Mercedes: {mercedes_revenue}.' \
               f' {team_ahead} is ahead at the {race_name} race.'
