from app.dao.models.director_model import Director

# ----------------------------------------------------------------------------------------------------------------------
# Constants for director MagicMock
ALL_DIRECTORS = [
    Director(
        id=1,
        name="Director_1"
    ),
    Director(
        id=2,
        name="Director_2"
    )
]

ONE_DIRECTOR = Director(
    id=1,
    name="Director_1"
)
