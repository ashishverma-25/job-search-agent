from langchain.chat_models import init_chat_model

from app.config.settings import settings


model = init_chat_model(
    model=settings.llm_model,
    model_provider=settings.llm_provider,
    api_key=settings.openai_api_key,
    temperature=0
)