import pytest

from app.services.director_service import DirectorService


# ----------------------------------------------------------------------------------------------------------------------
# Test class for director service
class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        """
        Create a test director service \n
        """
        self.director_service = DirectorService(director_dao)

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None, "Failed to get directors from database"
        assert len(directors) > 0, "Empty list of directors"

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None, "Failed to get director from database"
        assert director.id == 1, "Wrong director id"
        assert director.name == "Director_1", "Wrong director name"
