import google.generativeai as genai

from src.shared.config import Config

genai.configure(api_key=Config.API_KEY)

def get_query_embedding(query: str) -> list[float]:
    response = genai.embed_content(
        model="models/text-embedding-004",
        content=query,
        task_type="retrieval_query"
    )
    return response["embedding"]
