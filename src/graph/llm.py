from langchain_mistralai import ChatMistralAI
from config import static_config

MistralLLM = ChatMistralAI(
    model_name="mistral-large-latest",
    max_tokens=100,
    max_retries=3,
    api_key=static_config["mistral_key"],
)
