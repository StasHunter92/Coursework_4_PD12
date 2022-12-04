from app.dao.models.user_model import User


# ----------------------------------------------------------------------------------------------------------------------
# Create DAO model
class UserDAO:
    def __init__(self, session):
        """
        Initialize DAO with session \n
        :param session: Database session
        """
        self.session = session

    def get_user_by_email(self, email: str) -> User:
        """
        Get a single user \n
        :param email: User email
        :return: User object
        """
        return self.session.query(User).filter(User.email == email).first()

    def create(self, data: dict) -> User:
        """
        Create a new user \n
        :param data: Dictionary with user information
        :return: User object
        """
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, email: str, data: dict) -> None:
        """
        Update user information \n
        :param email: User email
        :param data: Dictionary with user information
        :return: None
        """
        self.session.query(User).filter(User.email == email).update(data)
        self.session.commit()
