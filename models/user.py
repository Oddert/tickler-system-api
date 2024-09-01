"""Config file for the user table model."""

from uuid import uuid4 as uuid

from sqlalchemy import Column, String, UUID
from sqlalchemy.orm import Session

from app.orm import ORMModelBase


class UserModel(ORMModelBase):
    '''Represents a user's details.'''
    __tablename__ = 'user'

    user_id = Column(UUID, nullable=False, primary_key=True, default=uuid)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def to_json(self) -> dict:
        """Returns a JSON serialisable object representing the model."""
        return {'userId': str(self.user_id), 'username': self.username}

    @classmethod
    def find_all(cls, db: Session):
        """Test route. Finds all users in the DB."""
        found_users = db.query(cls).all()
        return [u.to_json() for u in found_users]

    @classmethod
    def find_by_username(cls, db: Session, username: str) -> dict | None:
        """Attempts to find a user by username."""
        found_user = db.query(cls).filter_by(username=username).first()
        if found_user:
            return found_user
        return None

    @classmethod
    def validate_username(cls, db: Session, username: str) -> bool:
        """Returns true if a user exists, false if the user does not."""
        found_user = db.query(cls).filter_by(username=username).first()
        if found_user:
            return True
        return False
