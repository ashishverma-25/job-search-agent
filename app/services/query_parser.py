from app.models.job_search import JobSearchRequest
from app.ai.model import model

class JobQueryParser:

    def __init__(self):
        self.structured_model = model.with_structured_output(JobSearchRequest)

    def parse(self, query: str) -> JobSearchRequest:
        return self.structured_model.invoke(query)