from langchain_mistralai import ChatMistralAI

from config import static_config

# LLM that I am going to use
MistralLLM = ChatMistralAI(  # type: ignore
    model_name="mistral-large-latest",
    max_tokens=100,
    max_retries=3,
    api_key=static_config["mistral_key"],  # type: ignore
)  # type: ignore
