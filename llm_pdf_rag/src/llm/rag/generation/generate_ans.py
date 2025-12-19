import google.generativeai as genai
from src.shared.config import Config

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
            If the answer is not present, 
            search online from reliable sources and provide the answer.
            If you cannot find the answer, respond with "I don't know".

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