from app.dao.models.movie_model import Movie
# ----------------------------------------------------------------------------------------------------------------------
# Constants for movie MagicMock
ALL_MOVIES = [
    Movie(
        id=1,
        title="Movie_1",
        description="Test description 1",
        trailer="Test trailer 1",
        year=2000,
        rating=1.0,
        genre_id=1,
        director_id=1
    ),
    Movie(
        id=2,
        title="Movie_2",
        description="Test description 2",
        trailer="Test trailer 2",
        year=2022,
        rating=10.0,
        genre_id=2,
        director_id=2
    )
]

ONE_MOVIE = Movie(
    id=1,
    title="Movie_1",
    description="Test description 1",
    trailer="Test trailer 1",
    year=2000,
    rating=1.0,
    genre_id=1,
    director_id=1
)
