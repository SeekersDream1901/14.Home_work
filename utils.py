# Imports
import sqlite3


def get_movie_by_title(title):
    """Поиск фильма по названию"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT title, country, release_year, listed_in, description
                    FROM netflix
                    WHERE title LIKE '%{title}%'
                    ORDER BY release_year DESC
                    LIMIT 1
        """
        cursor.execute(query)
        result = cursor.fetchall()

        the_movie = result[0]
        keys = ["title", "country", "release_year", "listed_in", "description"]
        the_movie_dict = dict(zip(keys, the_movie))
        return the_movie_dict


def get_movie_by_year(year_one, year_two):
    """Поиск фильма по году"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN '{year_one}' AND '{year_two}'
                    LIMIT 100
        """
        cursor.execute(query)
        result = cursor.fetchall()
        movie_dict = []

        for movie, year in result:
            movie_dict.append(f'"title": {movie}, "release_year": {year}')
        return movie_dict


def get_movie_by_rating(g):
    """Поиск фильмов по рейтингу"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT title, rating, description
                    FROM netflix
                    WHERE rating ='{g}'
                    LIMIT 100
            """
        cursor.execute(query)
        result = cursor.fetchall()
        movie_dict = []

        for movie, rating, description in result:
            movie_dict.append(f'"title": {movie}, "rating": {rating}, "description": {description}')
        return movie_dict


def get_movie_by_genre(genre):
    """Поиск фильмов по жанру"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT title, description
                    FROM netflix
                    WHERE listed_in LIKE '%{genre}%'
                    ORDER BY release_year DESC
                    LIMIT 10
            """
        cursor.execute(query)
        result = cursor.fetchall()
        movie_dict = []

        for movie, description in result:
            movie_dict.append(f'"title": {movie}, "description": {description}')
        return movie_dict


def get_movie_by_actors(actor_one, actor_two): # не уверен в правильности работы (так как не совсем понял условие)
    """Возвращает список тех актёров, кто играет с ними в паре больше 2 раз"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT "cast"
                    FROM netflix
                    WHERE "cast" LIKE '%{actor_one}%' AND "cast" LIKE '%{actor_two}%'
            """
        cursor.execute(query)
        return cursor.fetchall()


def get_movie_by_type(type_m, year, genre):
    """Формирует список названий картин с их описаниями в JSON"""
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
                    SELECT title, description
                    FROM netflix
                    WHERE type='{type_m}' AND release_year='{year}' AND listed_in LIKE '%{genre}%'
            """
        cursor.execute(query)
        return cursor.fetchall()

print(get_movie_by_type('Movie', '2016', 'Sports Movies'))