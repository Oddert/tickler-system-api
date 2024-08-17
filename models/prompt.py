from datetime import datetime

from sqlalchemy import Column, Boolean, Date, Number, String, UUID

from app.orm import ORMModelBase

class PromptModel(ORMModelBase):
    model_id = Column(UUID, nullable=False, primary_key=True)
    # checklist = Column() # FK.checklist
    created_on = Column(Date, nullable=False, default=datetime.now())
    criticality = Column(String, nullable=False, default='default')
    date = Column(Date, nullable=False)
    defer_period = Column(String, nullable=False, default='week')
    defer_quantity = Column(Number, nullable=False, default=2)
    defer_count = Column(Number, nullable=False, default=0)
    deleted = Column(Boolean, nullable=True, default=False)
    deleted_on = Column(Date, nullable=True)
    description = Column(String, nullable=True)
    # links = Column() # FK.links
    status = Column(String, nullable=False, default='open')
    title = Column(String, nullable=False)
    updated_on = Column(Date, nullable=False, default=datetime.now())

    def to_json(self):
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
            'model_id': self.model_id, #string;// uuid
            'status': self.status, #'open' | 'resolved' | 'archived' | 'deleted';
            'title': self.title, #string;
            'updatedOn': self.updated_on, #string | null; // date
        }
