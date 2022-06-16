n = int(input())

for thousands in range(1, 9 + 1):
    for hundreds in range(1, 9 + 1):
        for tens in range(1, 9 + 1):
            for nums in range(1, 9 + 1):

                if n % thousands == 0 and n % hundreds == 0 and n % tens == 0 and n % nums == 0:
                    print(f"{thousands}{hundreds}{tens}{nums}", end=" ")

