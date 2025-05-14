import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-please-change')
    
    # File upload settings
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'pdf', 'txt', 'docx'}
    
    # Vector store settings
    VECTOR_STORE_PATH = 'vector_store'
    EMBEDDING_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
    
    # Document processing settings
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    
    # RAG settings
    NUM_RESULTS = 5  # Increased number of relevant passages to retrieve
    MIN_RELEVANCE_SCORE = 0.2  # Minimum relevance score for passages
    SEMANTIC_WEIGHT = 0.7  # Weight for semantic similarity in relevance scoring
    KEYWORD_WEIGHT = 0.3  # Weight for keyword matching in relevance scoring
    MAX_ANSWER_LENGTH = 150  # Maximum length of generated answers
    
    # Database settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///rag_assistant.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Create upload folder if it doesn't exist
os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
os.makedirs(Config.VECTOR_STORE_PATH, exist_ok=True) 