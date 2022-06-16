deck_of_cards = input().split()
number_of_shuffles = int(input())

for shuffle in range(number_of_shuffles):
    final_deck = []
    mid_part = len(deck_of_cards) // 2

    left_part = deck_of_cards[:mid_part]
    right_part = deck_of_cards[mid_part:]

    for index in range(len(left_part)):

        final_deck.append(left_part[index])
        final_deck.append(right_part[index])

    deck_of_cards = final_deck

print(deck_of_cards)
