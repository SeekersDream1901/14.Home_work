from flask import Flask

from utils import get_movie_by_title, get_movie_by_year, get_movie_by_rating, get_movie_by_genre

app = Flask(__name__)


@app.route('/movie/<title>')
def page_title(title):
    return f"<p>{get_movie_by_title(title)}<p>"


@app.route('/movie/<year_one>/to/<year_two>')
def page_year(year_one, year_two):
    return f"<p>{get_movie_by_year(year_one, year_two)}<p>"


@app.route('/rating/<g>')
def page_rating_children(g):
    if g == 'children':
        return f"<p>{get_movie_by_rating('G')}<p>"
    elif g == 'family':
        return f"""<p>{get_movie_by_rating('G')}<p>
                   <p>{get_movie_by_rating('PG')}<p>
                   <p>{get_movie_by_rating('PG-13')}<p>
        """
    elif g == 'adult':
        return f"""<p>{get_movie_by_rating('R')}<p>
                   <p>{get_movie_by_rating('NC-17')}<p>
        """


@app.route('/genre/<genre>')
def page_genre(genre):
    return f"<p>{get_movie_by_genre(genre)}<p>"


if __name__ == '__main__':
    app.run(debug=True)
