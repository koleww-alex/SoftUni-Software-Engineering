name = input()
from math import pi
if name == "square":
    a = float(input())
    print(f"{a * a:.3f}")
elif name == "rectangle":
    a = float(input())
    b = float(input())
    print(f"{a * b:.3f}")
elif name == "circle":
    r = float(input())
    print(f"{r * r * pi:.3f}")
elif name == "triangle":
    a = float(input())
    h = float(input())
    print(f"{a * h / 2:.3f}")
