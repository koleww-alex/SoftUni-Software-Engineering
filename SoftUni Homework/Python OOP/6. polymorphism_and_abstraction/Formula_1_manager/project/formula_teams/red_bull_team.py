from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -250_000
        sponsors = {
            'Oracle': {1: 1_500_000, 2: 800_000},
            'Honda': {8: 20_000, 10: 10_000}
        }

        for info in sponsors.values():
            for needed_pos in info:
                if race_pos <= needed_pos:
                    revenue += info[needed_pos]
                    break

        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
