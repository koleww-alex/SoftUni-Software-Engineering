import sys

max_rating = -sys.maxsize
min_rating = sys.maxsize

number_movies = int(input())
total_rating = 0

highest_rating_movie = ""
lowest_rating_movie = ""

for _ in range(1, number_movies + 1):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating

    if movie_rating >= max_rating:
        max_rating = movie_rating
        highest_rating_movie = movie_name

    if movie_rating <= min_rating:
        min_rating = movie_rating
        lowest_rating_movie = movie_name
average_rating = total_rating / number_movies

print(f"{highest_rating_movie} is with highest rating: {max_rating:.1f}\n"
      f"{lowest_rating_movie} is with lowest rating: {min_rating:.1f}\n"
      f"Average rating: {average_rating:.1f}")
