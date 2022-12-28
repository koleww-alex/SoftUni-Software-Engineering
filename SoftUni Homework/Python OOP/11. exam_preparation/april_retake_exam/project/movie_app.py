from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __find_user(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def register_user(self, username: str, age: int):
        if self.__find_user(username):
            raise Exception('User already exists!')

        user = User(username, age)
        self.users_collection.append(user)
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        if self.__find_user(username) is None:
            raise Exception('This user does not exist!')

        user = self.__find_user(username)
        if movie.owner != user:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        user = self.__find_user(username)
        if movie.owner != user:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        for key, val in kwargs.items():
            if key == 'title':
                movie.title = val

            elif key == 'year':
                movie.year = val

            elif key == 'age_restriction':
                movie.age_restriction = val

        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')

        user = self.__find_user(username)
        if movie.owner != user:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)

        if movie.owner == user:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')

        if movie in user.movies_liked:
            raise Exception(f'{username} already liked the movie {movie.title}!')

        user.movies_liked.append(movie)
        movie.likes += 1
        return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)

        if movie not in user.movies_liked:
            raise Exception(f'{username} has not liked the movie {movie.title}!')

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        if sorted_movies:
            return '\n'.join(m.details() for m in sorted_movies)

        return 'No movies found.'

    def __str__(self):
        users = []
        if self.users_collection:
            [users.append(u.username) for u in self.users_collection]
        else:
            users.append('No users.')

        movies = []
        if self.movies_collection:
            [movies.append(m.title) for m in self.movies_collection]
        else:
            movies.append('No movies.')

        if self.users_collection:
            users_output = [f'All users: {", ".join(users)}']
        else:
            users_output = ['All users: No users.']

        if self.movies_collection:
            movies_output = [f'All movies: {", ".join(movies)}']
        else:
            movies_output = [f'All movies: No movies.']

        output = users_output + movies_output
        return '\n'.join(output)


# movie_app = MovieApp()
# print(movie_app.register_user('Martin', 24))
# user = movie_app.users_collection[0]
# movie = Action('Die Hard', 1988, user, 18)
# print(movie_app.upload_movie('Martin', movie))
# print(movie_app.movies_collection[0].title)
# print(movie_app.register_user('Alexandra', 25))
# user2 = movie_app.users_collection[1]
# movie2 = Action('Free Guy', 2021, user2, 16)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.like_movie('Alexandra', movie))
# print(movie_app.dislike_movie('Martin', movie2))
# print(movie_app.like_movie('Martin', movie2))
# print(movie_app.delete_movie('Alexandra', movie2))
# movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.display_movies())
# print(movie_app)
