from sqlalchemy.orm import Session

from models.ticket import Ticket


def assign_ticket(
    db: Session,
    ticket_id: int,
    agent_name: str
):

    ticket = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if ticket:

        ticket.assigned_agent = agent_name

        ticket.status = "In Progress"

        db.commit()

        db.refresh(ticket)

    return ticket