from pydantic import BaseModel


class NaturalLanguageSearchRequest(BaseModel):
    query: str