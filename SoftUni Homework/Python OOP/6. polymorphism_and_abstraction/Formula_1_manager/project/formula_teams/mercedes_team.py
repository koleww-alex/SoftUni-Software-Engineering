from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -200_000
        sponsors = {
            'Petronas': {1: 1_000_000, 3: 500_000},
            'TeamViewer': {5: 100_000, 7: 50_000}
        }

        for info in sponsors.values():
            for needed_pos in info:
                if race_pos <= needed_pos:
                    revenue += info[needed_pos]
                    break

        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
