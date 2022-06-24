str_inp = input().split()

while True:

    command = input()
    if command == "3:1":
        print(" ".join(str_inp))
        break

    command_split = command.split()
    main_command = command_split[0]

    if main_command == "merge":

        idx_start = int(command_split[1])
        idx_end = int(command_split[2])

        if idx_start < 0:
            idx_start = 0
        if idx_end >= len(str_inp):
            idx_end = len(str_inp) - 1

        str_inp[idx_start:idx_end + 1] = ["".join(i for i in str_inp[idx_start:idx_end + 1])]

    elif main_command == "divide":
        idx = int(command_split[1])
        partit = int(command_split[2])

        if partit == 0:
            continue
        else:
            if len(str_inp[idx]) % partit == 0:
                lenght_symbol = len(str_inp[idx]) // partit
                word = [str_inp[idx][i:i + lenght_symbol] for i in range(0, len(str_inp[idx]), lenght_symbol)]

            else:
                lenght_symbol = len(str_inp[idx]) // partit
                if lenght_symbol < 1:
                    continue
                else:
                    word = [str_inp[idx][i:i + lenght_symbol] for i in range(0, len(str_inp[idx]), lenght_symbol)]
                    merged_word = "".join(word[-2:])
                    word[-2:] = [merged_word]

        str_inp[idx:idx + 1] = word
