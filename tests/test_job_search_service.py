from app.services.job_search_service import JobSearchService
from app.sources.mock_linkedin import MockLinkedInSource


def test_job_search_service_deduplicates():

    service = JobSearchService(
        sources=[
            MockLinkedInSource()
        ]
    )

    urls = [
        "linkedin-url-1",
        "linkedin-url-2",
    ]

    jobs = service.search(
        search_request=None,
        urls=urls,
    )

    assert len(jobs) == 2