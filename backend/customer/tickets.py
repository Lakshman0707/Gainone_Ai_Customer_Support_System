from sqlalchemy.orm import Session

from models.ticket import Ticket


def get_my_tickets(
    db: Session,
    user_id: int
):

    return db.query(Ticket).filter(

        Ticket.user_id == user_id

    ).all()