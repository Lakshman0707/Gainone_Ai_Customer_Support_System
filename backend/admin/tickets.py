from sqlalchemy.orm import Session

from models.ticket import Ticket


def get_all_tickets(db: Session):

    return db.query(Ticket).all()