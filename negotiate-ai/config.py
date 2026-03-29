"""
config.py — All API keys and configuration in one place.
"""
import os

# ─── Gemini ───
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "Paste Gemini API Key here")
GEMINI_MODEL = "gemini-2.0-flash"

# ─── ElevenLabs ───
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY", "Paste ElevenLabs Key")
ELEVENLABS_VOICE_ID = "XrExE9yKIg1WjnnlVkGX"  # Matilda — Knowledgable, Professional (premade, free tier)

# ─── MongoDB ───
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://username:<password>@cluster0.ntbjlvr.mongodb.net/?appName=Cluster0")
MONGODB_DB_NAME = "negotiate_ai"

# ─── Solana ───
SOLANA_RPC_URL = "https://api.devnet.solana.com"  # Free devnet, no key needed
