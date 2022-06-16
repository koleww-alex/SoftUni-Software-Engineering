number_of_iterations = int(input())

start = False
end = False
balanced = False

for _ in range(1, number_of_iterations + 1):
    current_str = input()
    first_str = "("

    if current_str == "(":
        start = True
    else:
        break

    if current_str == ")":
        end = True

    if start and end:
        balanced = True

if balanced:
    print("BALANCED")
else:
    print("UNBALANCED")

# Unfinished!