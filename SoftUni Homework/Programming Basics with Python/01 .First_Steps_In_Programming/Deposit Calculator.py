deposit = float(input())
term_of_deposit = int(input())
yearly_interest_percent = float(input()) / 100
deposti_per_month = deposit * yearly_interest_percent / 12
final_sum = deposit + (term_of_deposit * deposti_per_month)
print(final_sum)
