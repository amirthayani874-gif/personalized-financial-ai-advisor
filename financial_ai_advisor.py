from openai import OpenAI

client = OpenAI(api_key="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")

def ask_ai(question, user_profile):
    prompt = f"""
You are a friendly, personalized financial advisor.

User details:
{user_profile}

Answer the question clearly, step by step, with examples.

Question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a financial AI advisor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    return response.choices[0].message.content
if __name__ == "__main__":
    user_profile = """
    Name: Varsha
    Monthly Income: 50,000
    Monthly Expenses: 30,000
    Savings: 1,00,000
    Risk: Low
    Goal: Save 2 lakh in 1 year
    """

    question = "How much should I save every month?"
    answer = ask_ai(question, user_profile)
    print(answer)
