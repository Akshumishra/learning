import google.generativeai as genai

from src.shared.config import Config

genai.configure(api_key=Config.API_KEY)

def get_embedding(text: str) -> list[float]:
    response = genai.embed_content(
        model="models/text-embedding-004",
        content=text,
        task_type="retrieval_document"
    )
    return response["embedding"]
