from sqlalchemy.orm import Session

from models.ticket import Ticket


def close_ticket(
    db: Session,
    ticket_id: int
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if ticket:

        ticket.status = "Closed"

        db.commit()

        db.refresh(ticket)

    return ticket