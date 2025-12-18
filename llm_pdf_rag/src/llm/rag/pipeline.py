from src.llm.rag.ingestion.load_pdf import get_all_documents, extract_text_from_pdf
from src.llm.rag.ingestion.chunk import chunk_text, save_chunks_and_embeddings
from src.llm.rag.retrieval.similarity_search import similarity_search
from src.llm.rag.generation.generate_ans import generate_answer, build_prompt, build_context

def process_all_documents():
    documents = get_all_documents()

    for doc_id, document_path in documents:
        print(f"Processing document ID {doc_id}")

        try:
            pdf_text = extract_text_from_pdf(document_path)

            if not pdf_text.strip():
                print(f"No text found in {document_path}")
                continue
            chunks = chunk_text(pdf_text)
            save_chunks_and_embeddings(doc_id, chunks)

            print(f"Stored {len(chunks)} chunks")

        except Exception as e:
            print(f"Error processing {document_path}: {e}")

def query_processing():
    query = input("Enter your query: ")

    results = similarity_search(query)
    print("\nRetrieved Chunks:")
    for row in results:
        print(f"Doc {row.document_id} | Similarity {row.similarity:.3f}")

    print("\nAnswer:")
    retrieved_chunks = [row.chunk_text]
    context = build_context(retrieved_chunks)
    prompt = build_prompt(context, query)
    print(generate_answer(prompt))
