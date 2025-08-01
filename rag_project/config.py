import os

# --- LLM and API Configuration ---
# Use environment variables to keep your secrets safe
os.environ["OPENAI_API_KEY"] = ""
#

# --- LLM and API Configuration ---
LLM_CONFIG_LIST = [
    {
        "model": "gpt-4o",
        "api_key": os.getenv("OPENAI_API_KEY"),
    },
]

# --- RAG and Vector DB Configuration ---
# Get the absolute path to the project root directory
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# The path where your raw PDF documents are stored
PDF_SOURCE_PATH = os.path.join(PROJECT_ROOT, "pdfs/")

# The absolute path where ChromaDB will persist its data
CHROMA_DB_PATH = os.path.join(PROJECT_ROOT, "chroma_db/")

# The name of the ChromaDB collection to use for your documents
CHROMA_COLLECTION_NAME = "insurance_docs"

# The embedding model to use for converting text to vectors
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# --- Text Splitter Configuration ---
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# --- Agent Configuration ---
ASSISTANT_SYSTEM_MESSAGE = (
    "You are an expert assistant for answering questions about insurance policies. "
    "You will be provided with relevant document snippets to answer the user's questions. "
    "Always cite the document snippet you are using to formulate your answer."
)

