from services.email_service import send_support_email

send_support_email(

    customer_name="Lakshman",

    customer_email="lakshman@gmail.com",

    summary="""
Customer requested human support.

The AI answered general questions but
the customer wanted to speak with a support agent.
"""

)