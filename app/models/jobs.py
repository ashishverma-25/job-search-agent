from pydantic import BaseModel, Field

class Job(BaseModel):
    title: str
    company: str
    location: str
    posted_time: str | None = None
    description: str | None = None
    job_url: str
    job_id: str | None = None
    source: str
    skills: list[str] = Field(default_factory=list)