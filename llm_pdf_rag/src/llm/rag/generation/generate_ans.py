import google.generativeai as genai
from shared.config import Config

genai.configure(api_key=Config.API_KEY)

def build_context(chunks, max_chars=2550):
    context = ""
    for chunk in chunks:
        if len(context) + len(chunk) > max_chars:
            break
        context += chunk + "\n"
    return context


def build_prompt(context: str, query: str) -> str:
    return f"""
You are a helpful assistant.
Answer the question ONLY using the context below.
If the answer is not present, say:
"I don't know based on the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""

def generate_answer(prompt: str) -> str:
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text