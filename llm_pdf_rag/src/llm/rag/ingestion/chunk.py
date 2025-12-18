from sqlalchemy import text
import json
from shared.database import engine
from llm.rag.embedding.document_embedding import get_embedding

def chunk_text(text_data: str, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text_data):
        end = start + chunk_size
        chunks.append(text_data[start:end])
        start = end - overlap
    return chunks

def save_chunks_and_embeddings(document_id: int, chunks: list[str], overlap=50):
 
    insert_query = text("""
        INSERT INTO document_chunk_and_embedding (document_id, chunk_text, embedding, metadata)
        VALUES (:document_id, :chunk_text, :embedded_text, :metadata)
    """)
    with engine.begin() as conn:
        for idx, chunk in enumerate(chunks):
            embedding = get_embedding(chunk)
            conn.execute(
                insert_query,
                {
                    "document_id": document_id,
                    "chunk_text": chunk,
                    "embedded_text": embedding,
                    "metadata": json.dumps({
                                    "length": len(chunk),
                                    "chunk_index": idx,
                                    "overlap": overlap,
                                    "document_id": document_id
                                })
                }
            )
        print(f"Chunks saved for document ID {document_id}")