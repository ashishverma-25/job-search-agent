from app.models.jobs import Job
from app.models.job_search import JobSearchRequest
from app.sources.base import JobSource
from app.sources.mock_linkedin import MockLinkedInSource


class JobSearchService:

    def __init__(self, sources: list[JobSource]):
        self.sources = sources

    def search( self, search_request: JobSearchRequest, urls: list[str]) -> list[Job]:
        jobs: list[Job] = []

        for source in self.sources:
            for url in urls:
                source_jobs = source.search(url)
                jobs.extend(source_jobs)

        return self._deduplicate(jobs)

    def _deduplicate(self, jobs: list[Job]) -> list[Job]:

        unique_jobs = {}
        
        for job in jobs:
            unique_jobs[job.job_url] = job

        return list(unique_jobs.values())
    
def get_job_search_service() -> JobSearchService:
    return JobSearchService(
        sources=[MockLinkedInSource()]
    )