class Party:
    def __init__(self):
        self.people = []


list_of_people = Party()
command = input()


while command != "End":
    current_people = command
    list_of_people.people.append(current_people)

    command = input()

print(f"Going: {', '.join(list_of_people.people)}")
print(f"Total: {len(list_of_people.people)}")

