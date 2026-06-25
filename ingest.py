from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb


PDF_PATH = "data/labor_law.pdf"
DB_PATH = "./chroma_db"
COLLECTION_NAME = "saudi_labor_law"


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text()

        if page_text:
            full_text += f"\n\n--- Page {page_number} ---\n"
            full_text += page_text

    return full_text


def chunk_text(text, chunk_size=800, overlap=150):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks


def main():
    print("Extracting text from PDF...")
    text = extract_text_from_pdf(PDF_PATH)

    print("Chunking text...")
    chunks = chunk_text(text)

    print(f"Total chunks created: {len(chunks)}")

    print("Loading embedding model...")
    model = SentenceTransformer("BAAI/bge-small-en-v1.5")

    print("Creating embeddings...")
    embeddings = model.encode(chunks)

    print("Saving to ChromaDB...")
    client = chromadb.PersistentClient(path=DB_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embeddings[i].tolist()],
            metadatas=[{"chunk_id": i}]
        )

    print("Ingestion complete.")


if __name__ == "__main__":
    main()