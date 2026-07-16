from sqlalchemy.orm import Session

from models.ticket import Ticket


def create_ticket(
    db: Session,
    user_id: int,
    issue: str,
    priority: str = "Medium"
):

    ticket = Ticket(

        user_id=user_id,

        issue=issue,

        status="Open",

        assigned_agent="Not Assigned",

        priority=priority

    )

    db.add(ticket)

    db.commit()

    db.refresh(ticket)

    return ticket