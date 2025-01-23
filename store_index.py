from src.helper import load_pdf, text_split, download_hugging_face_embeddings
import pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_API_ENV = os.getenv("PINECONE_API_ENV")

extracted_data = load_pdf("data/")
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

index_name='medibot'
pc = pinecone.Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index=pc.Index(index_name)
vectorstore_from_docs = PineconeVectorStore.from_documents(
        text_chunks,
        index_name=index_name,
        embedding=embeddings
    )

