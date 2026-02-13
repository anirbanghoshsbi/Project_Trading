from openai import OpenAI
from config import OPENAI_KEY, LLM_MODEL, LLM_TEMPERATURE

client = OpenAI(api_key=OPENAI_KEY)


SYSTEM_PROMPT = """
You are a strict trading discipline supervisor.

Rules:
- No trading decisions before 3:15 PM.
- No stop-loss modification.
- No strategy switching.
- Profit phases increase sabotage risk.
- You are NOT allowed to generate trading signals.
- You are NOT allowed to override rule engine.

Always respond in JSON format:

{
  "risk": "Low/Medium/High",
  "message": "Firm but concise response."
}
Do not include any text outside the JSON.
"""


def call_llm(user_message, context):

    prompt = f"""
User message:
{user_message}

System context:
{context}

Evaluate behavioral risk and respond.
"""

    response = client.chat.completions.create(
        model=LLM_MODEL,
        temperature=LLM_TEMPERATURE,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
    )

    return response.choices[0].message.content
