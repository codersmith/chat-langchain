"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle

from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS

from dotenv import load_dotenv
load_dotenv()

def ingest_pdf_docs():
    """Read PDF documents in `./pdf/*`."""
    loader = PyPDFDirectoryLoader(path="./pdfs", glob="**/[!.]*.pdf")
    pages = loader.load_and_split()
    vectorstore = FAISS.from_documents(pages, OpenAIEmbeddings())

    # Save vectorstore
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    ingest_pdf_docs()
