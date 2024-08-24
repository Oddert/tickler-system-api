'''Config file for PromptModel.'''
from datetime import datetime
from uuid import uuid4

from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String, UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    # relationship,
    Session,
)

from app.orm import ORMModelBase

class PromptModel(ORMModelBase):
    '''Represents a Prompt.'''
    __tablename__ = 'prompt'

    prompt_id = Column(UUID, nullable=False, primary_key=True, unique=True, default=uuid4)
    # checklist = Column() # FK.checklist
    created_on = Column(Date, nullable=False, default=datetime.now)
    criticality = Column(String, nullable=False, default='default')
    date = Column(Date, nullable=False)
    defer_period = Column(String, nullable=False, default='week')
    defer_quantity = Column(Integer, nullable=False, default=2)
    defer_count = Column(Integer, nullable=False, default=0)
    deleted = Column(Boolean, nullable=True, default=False)
    deleted_on = Column(Date, nullable=True)
    description = Column(String, nullable=True)
    # links = Column() # FK.links
    status = Column(String, nullable=False, default='open')
    title = Column(String, nullable=False)
    updated_on = Column(Date, nullable=False, default=datetime.now)
    user_id: Mapped[UUID] = mapped_column(ForeignKey('user.user_id'))

    # user: = relationship(back_populates='prompts')

    def to_json(self):
        '''Returns a JSON serialisable object representing the model.'''
        return {
            'checklist': None, #string | null; // FK.checklist
            'createdOn': self.created_on, #string; // date
            'criticality': self.criticality, #'severe' | 'default' | 'reminder' | 'reference';
            'date': self.date, #string;
            'deferPeriod': self.defer_period, #'day' | 'month' | 'year';
            'deferQuantity': self.defer_quantity, #number;
            'deferredCount': self.defer_count, #number; // number (default: 0)
            'deleted': self.deleted, #boolean; // boolean
            'deletedOn': self.deleted_on, #string | null; // date
            'description': self.description, #string | null; // str(2000)
            'links': None, #string[]; // [] FK.links
            'prompt_id': str(self.prompt_id), #string;// uuid
            'status': self.status, #'open' | 'resolved' | 'archived' | 'deleted';
            'title': self.title, #string;
            'updatedOn': self.updated_on, #string | null; // date
            'userId': str(self.user_id)
        }

    @classmethod
    def find_all(cls, db: Session):
        '''Returns all prompts in the DB.'''
        return db.query(cls).all()

    @classmethod
    def find_by_id(cls, db: Session, prompt_id: str):
        '''Finds a single Prompt by an ID..'''
        result = db.query(cls).filter_by(prompt_id=UUID(prompt_id)).first()
        if not result:
            return None
        return result

    @classmethod
    def find_all_by_username(cls, db: Session, username: str):
        '''Returns all prompts for a given username.'''
        return db.query(cls).filter_by(username=username.lower()).all()
