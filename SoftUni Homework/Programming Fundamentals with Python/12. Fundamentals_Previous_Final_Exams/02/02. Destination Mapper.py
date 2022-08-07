import re
text = input()
pattern = r"=([A-Z][A-Za-z]+)=|\/([A-Z][A-Za-z]+)\/"
matches = re.findall(pattern, text)
travel_points = 0
travel_journal = []
for match in matches:
    for destination in match:
        if len(destination) >= 3:
            travel_points += len(destination)
            travel_journal.append(destination)

print(f"Destinations: {', '.join(travel_journal)}")
print(f"Travel Points: {travel_points}")
