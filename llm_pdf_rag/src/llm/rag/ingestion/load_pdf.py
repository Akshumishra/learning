import re
import PyPDF2
from sqlalchemy import text

from shared.database import engine

def get_all_documents():
    query = text("SELECT id, document_path FROM documents " \
    "where id NOT IN (Select DISTINCT document_id from document_chunk_and_embedding)")
    with engine.connect() as conn:
        return conn.execute(query).fetchall()

def extract_text_from_pdf(file_path: str) -> str:
    pdf_text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            pdf_text += page.extract_text() or ""
        pdf_text = re.sub(r'\s+', ' ', pdf_text)
        pdf_text = ''.join(ch for ch in pdf_text if ch.isprintable())
        pdf_text = pdf_text.strip()
    return pdf_text
