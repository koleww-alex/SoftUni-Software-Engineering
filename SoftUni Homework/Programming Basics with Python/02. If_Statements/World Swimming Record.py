record_seconds = float(input())
distance_meters = float(input())
seconds_one_meter = float(input())

from math import floor
seconds_for_whole_distance = distance_meters * seconds_one_meter
water_resistance_seconds = floor((distance_meters / 15)) * 12.5
seconds_for_whole_distance_with_resistance = seconds_for_whole_distance + water_resistance_seconds

seconds_slower = abs(record_seconds - seconds_for_whole_distance_with_resistance)

if seconds_for_whole_distance_with_resistance < record_seconds:
    print(f"Yes, he succeeded! The new world record is {seconds_for_whole_distance_with_resistance:.2f} seconds.")
else:
    print(f"No, he failed! He was {seconds_slower:.2f} seconds slower.")

