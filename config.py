import os

DATABASE = os.getenv("CERTIFICATE_DB", "certificates.db")

# Optional future GenAI configuration.
# Set these environment variables when connecting an LLM provider.
AI_PROVIDER = os.getenv("AI_PROVIDER", "demo")
AI_API_KEY = os.getenv("AI_API_KEY", "")
AI_MODEL = os.getenv("AI_MODEL", "")
