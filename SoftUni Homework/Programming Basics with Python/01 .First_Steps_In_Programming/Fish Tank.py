length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100
full_size = (length * width * height) / 1000
real_size = full_size - (full_size * percent)
print(real_size)
