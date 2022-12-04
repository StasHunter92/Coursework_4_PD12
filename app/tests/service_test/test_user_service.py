import pytest

from app.services.user_service import UserService


# ----------------------------------------------------------------------------------------------------------------------
# Test class for user service
class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        """
        Create a test movie service \n
        :param user_dao: Mocked user dao
        """
        self.user_service = UserService(user_dao)

    def test_hash_password(self):
        hash_password = self.user_service.hash_password('password')
        assert type(hash_password) is bytes
        assert hash_password == b'oSvTQ3vIVvPszyYe1jCxs91Pklfsi8p64yUAkIc40oI='

    def test_compare_password(self):
        compare_password = self.user_service.compare_password('oSvTQ3vIVvPszyYe1jCxs91Pklfsi8p64yUAkIc40oI=',
                                                              'password')
        assert compare_password is True

    def test_get_user(self):
        user = self.user_service.get_user('test@example.com')
        assert user is not None, "Failed to get user from database"
        assert user.id == 1, "Wrong user id"

    def test_update_user(self):
        data = {"name": "User",
                "surname": "User",
                "favourite_genre": 8}
        assert self.user_service.update_user('test@example.com', data) is None, "Something returned"

    def test_update_password(self):
        data = {"old_password": "password", "new_password": "new_password"}

        assert self.user_service.update_password('test@example.com', data) is None, "Something returned"
