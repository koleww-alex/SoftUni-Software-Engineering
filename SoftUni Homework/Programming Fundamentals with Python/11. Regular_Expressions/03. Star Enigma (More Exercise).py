import re
decrypting_pattern = r"[star]"
pattern = r"@([A-Za-z]+).?\:(\d+)!(A|D)!->(\d+)"
number_of_inputs = int(input())
attacked_planets = []
destroyed_planets = []
for _ in range(number_of_inputs):
    number_of_ch = 0
    command = input()
    x = re.findall(decrypting_pattern, command, re.IGNORECASE)
    number_of_ch += len(x)

    decrypted_message = ""
    for ch in command:
        new_ch = chr(ord(ch) - number_of_ch)
        decrypted_message += new_ch

    matches = re.findall(pattern, decrypted_message)
    for match in matches:
        planet_name, population, attack_type, soldiers = match
        if attack_type == "A":
            attacked_planets.append(planet_name)
        else:
            destroyed_planets.append(planet_name)

print(f"Attacked planets: {len(attacked_planets)}")
if len(attacked_planets):
    print("\n".join(f"-> {planet}" for planet in sorted(attacked_planets)))

print(f"Destroyed planets: {len(destroyed_planets)}")
if len(destroyed_planets):
    print("\n".join(f"-> {planet}" for planet in sorted(destroyed_planets)))
