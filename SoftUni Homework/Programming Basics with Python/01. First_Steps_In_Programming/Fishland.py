price_skumriq_kilo = float(input())
price_caca_kilo = float(input())
price_palamud_per_kilo = float(input())
price_safrid_per_kilo = float(input())
price_midi_kilo = int(input())
price_palamud_kilos = price_skumriq_kilo + (price_skumriq_kilo * 0.6)
price_safrid_kilos = price_caca_kilo + (price_caca_kilo * 0.8)
price_palamud = price_palamud_kilos * price_palamud_per_kilo
price_safrid = price_safrid_kilos * price_safrid_per_kilo
price_midi = price_midi_kilo * 7.5
print(f"{price_palamud + price_safrid + price_midi:.2f}")
