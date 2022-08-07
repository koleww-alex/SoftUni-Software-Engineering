import re
list_of_participants = input().split(", ")
participants_info = {}
pattern_for_names = r"[A-Za-z]+"
pattern_for_nums = r"\d"

while True:
    command = input()
    if command == "end of race":
        break
    ch_of_name = re.findall(pattern_for_names, command)
    name = "".join(ch_of_name)
    ch_of_nums = re.findall(pattern_for_nums, command)
    nums = [int(num) for num in ch_of_nums]
    km_ran = sum(nums)
    if name in list_of_participants:
        if name not in participants_info:
            participants_info[name] = 0
        participants_info[name] += km_ran
i = 0
sorted_dict = {k: v for k, v in sorted(participants_info.items(), key=lambda item: item[1], reverse=True)}
list_of_winners = []
for key in sorted_dict:
    i += 1
    list_of_winners.append(key)
    if i == 3:
        break
print(f"1st place: {list_of_winners[0]}")
print(f"2nd place: {list_of_winners[1]}")
print(f"3rd place: {list_of_winners[2]}")
