import os
import chromadb
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "saudi_labor_law"

GROQ_MODEL = "llama-3.3-70b-versatile"


def get_collection():
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    return client.get_collection(name=COLLECTION_NAME)


def retrieve_context(collection, question, n_results=5):
    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    documents = results.get("documents", [[]])[0]

    if not documents:
        return ""

    return "\n\n---\n\n".join(documents)


def generate_answer(question, context):
    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found. Add it to your .env file.")

    client_llm = OpenAI(
        api_key=groq_api_key,
        base_url="https://api.groq.com/openai/v1"
    )

    system_prompt = """
You are a helpful assistant answering questions about Saudi Labor Law.

Use ONLY the provided context.
If the answer is not found in the context, say:
"I could not find this in the provided Saudi Labor Law context."

Do not invent legal information.
Give a clear and simple answer.
"""

    user_prompt = f"""
Question:
{question}

Context:
{context}

Answer:
"""

    response = client_llm.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content


def main():
    collection = get_collection()

    while True:
        question = input("\nAsk a question about Saudi Labor Law, or type 'exit': ")

        if question.lower().strip() in ["exit", "quit"]:
            break

        context = retrieve_context(collection, question)

        if not context:
            print("\nNo relevant context found in ChromaDB.")
            continue

        answer = generate_answer(question, context)

        print("\nAnswer:")
        print(answer)


if __name__ == "__main__":
    main()