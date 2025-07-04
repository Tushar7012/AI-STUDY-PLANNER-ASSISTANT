import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

class ModelLoader:
    def __init__(self, model_provider: str = "groq"):
        self.provider = model_provider

    def load_llm(self):
        if self.provider.lower() == "groq":
            api_key = os.getenv("GROQ_API_KEY")
            if not api_key:
                raise ValueError("GROQ_API_KEY not set in .env")
            llm = ChatGroq(
                api_key=api_key,
                model=os.getenv("GROQ_MODEL_NAME", "llama-3.3-70b-versatile"),
                temperature=0.7,
                max_retries=3,
                request_timeout=60,
            )
            return llm
        else:
            raise NotImplementedError(f"Model provider '{self.provider}' is not supported.")
