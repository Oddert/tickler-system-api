'''Config file for the user table model.'''
from uuid import uuid4 as uuid

from sqlalchemy import Column, String, UUID

from app.orm import ORMModelBase

class UserModel(ORMModelBase):
    __tablename__ = 'user'

    user_id = Column(UUID, nullable=False, primary_key=True, default=uuid)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def to_json(self) -> dict:
        return {
            'user_id': self.user_id,
            'username': self.username
        }

    @classmethod
    def find_by_username(cls, db, username: str) -> dict | None:
        '''Attempts to find a user by username.'''
        found_user = db.query(cls).filter_by(username=username).first()
        if found_user:
            return found_user
        return None