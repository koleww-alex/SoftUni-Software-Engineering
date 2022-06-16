command = input()
secret_message = 0
word_creator = ""
list1 = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c",
         "v", "b", "n", "m", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K",
         "L", "Z", "X", "C", "V", "B", "N", "M"]

c_cnt = 0
o_cnt = 0
n_cnt = 0


while command != "End":
    if command == "c":
        if c_cnt == 0:
            c_cnt += 1
            command = input()
            continue
    if command == "o":
        if o_cnt == 0:
            o_cnt += 1
            command = input()
            continue

    if command == "n":
        if n_cnt == 0:
            n_cnt += 1
            command = input()
            continue

    if command not in list1:
        command = input()
        continue

    word_creator += command

    command = input()

if secret_message == 3:
    print(f"{word_creator}")
