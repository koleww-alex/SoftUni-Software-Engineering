# 1 - 26 + 1

from itertools import islice

list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
         "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

starting_letter = input()
ending_letter = input()
skip_letter = input()

for ch in list1:
    for ch1 in list1:
        for ch2 in list1:

            if ch and ch1 and ch2 != skip_letter:
                

                print(ch, ch1, ch2)


# Unfinished!!!
