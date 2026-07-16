from sqlalchemy.orm import Session

from models.ticket import Ticket


def update_ticket_status(
    db: Session,
    ticket_id: int,
    status: str
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if ticket:

        ticket.status = status

        db.commit()

        db.refresh(ticket)

    return ticket