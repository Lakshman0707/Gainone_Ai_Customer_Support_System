from langchain_groq import ChatGroq

from app.config import (
    GROQ_API_KEY,
    GROQ_MODEL
)


llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model=GROQ_MODEL
)


def generate_summary(conversation: str):

    prompt = f"""

You are an AI customer support assistant.

Summarize this conversation in 5-8 lines.

Include:

1. Customer requirement
2. Main discussion
3. Was AI able to solve?
4. Reason for escalation
5. Final conclusion

Conversation:

{conversation}

"""

    response = llm.invoke(prompt)

    return response.content