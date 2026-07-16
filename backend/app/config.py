import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ===========================
# Database Configuration
# ===========================

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# ===========================
# Security
# ===========================

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60)
)

# ===========================
# AI API Keys
# ===========================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ===========================
# AI Model
# ===========================

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.1-8b-instant"
)

# ===========================
# RAG Configuration
# ===========================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL"
)

VECTOR_DB_PATH = os.getenv(
    "VECTOR_DB_PATH"
)

UPLOAD_FOLDER = os.getenv(
    "UPLOAD_FOLDER"
)

CONFIDENCE_THRESHOLD = float(
    os.getenv("CONFIDENCE_THRESHOLD", 0.75)
)

# ===========================
# Email Configuration
# ===========================

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

COMPANY_EMAIL = os.getenv(
    "COMPANY_EMAIL",
    "gainone.support@gmail.com"
)