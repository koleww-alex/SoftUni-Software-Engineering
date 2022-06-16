year_commission = int(input())
basketball_sneakers = year_commission - (year_commission * 0.4)
basketball_outfit = basketball_sneakers - (basketball_sneakers * 0.2)
basketball_ball = basketball_outfit * 0.25
basketball_accessories = basketball_ball * 0.2
final_price = year_commission + basketball_sneakers + basketball_outfit + basketball_ball + basketball_accessories
print(final_price)
