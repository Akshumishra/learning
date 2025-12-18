from sqlalchemy import create_engine, text
from src.shared.config import Config

engine = create_engine(Config.DB_URL)

with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS documents (
            id SERIAL PRIMARY KEY,
            document_path TEXT NOT NULL UNIQUE,
            metadata JSONB NOT NULL
        );
    """))
    print("documents table created successfully!")
    conn.execute(text("""
        INSERT INTO documents (document_path, metadata)
        VALUES
            ('/Users/akshitamishra/Desktop/llm_pdf_rag/PDFS/the-time-machine.pdf', '{"document_name": "The Time Machine", "document_size": 120000}'),
            ('/Users/akshitamishra/Desktop/llm_pdf_rag/PDFS/romeo-and-juliet.pdf', '{"document_name": "Romeo And Juliet", "document_size": 4500}'),
            ('/Users/akshitamishra/Desktop/llm_pdf_rag/PDFS/alice-adventures-in-wonderland.pdf', '{"document_name": "Alice Adventures In Wonderland", "document_size": 8900}')
        ON CONFLICT (document_path) DO NOTHING;
    """))
    
    print("3 rows inserted successfully!")
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS document_chunk_and_embedding (
            id SERIAL PRIMARY KEY,
            document_id INT REFERENCES documents(id) ON DELETE CASCADE,
            chunk_text TEXT NOT NULL,
            embedding VECTOR(768),
            metadata JSONB NOT NULL
        );
    """))
    print("Created chunks and embedding table successfully!")
    print("Database Connected successfully!")
