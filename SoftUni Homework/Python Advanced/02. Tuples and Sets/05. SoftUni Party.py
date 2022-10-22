# Using SORTED function

number_of_iterations = int(input())
invitational_list = set()
arrived_guest = set()

for _ in range(number_of_iterations):
    invited_guest = input()
    invitational_list.add(invited_guest)

current_guest = input()
while current_guest != 'END':
    arrived_guest.add(current_guest)
    current_guest = input()

not_attend = invitational_list.difference(arrived_guest)
print(len(not_attend))
print('\n'.join(sorted(not_attend)))


# Without using SORTED function

number_of_iterations = int(input())
vips = set()
regulars = set()
for _ in range(number_of_iterations):
    invited_guest = input()
    if invited_guest[0].isdigit():
        vips.add(invited_guest)
    else:
        regulars.add(invited_guest)

current_guest = input()
while current_guest != 'END':
    if current_guest in vips:
        vips.remove(current_guest)
    else:
        regulars.remove(current_guest)

    current_guest = input()

print(len(vips) + len(regulars))
print('\n'.join(vips))
print('\n'.join(regulars))
