from app.models.job_search import JobSearchRequest
from app.models.natural_lang_search_req import NaturalLanguageSearchRequest
from app.services.job_search_service import get_job_search_service
from app.services.linkedin_url_builder import build_linkedin_urls
from app.sources.linkedin import LinkedInSource
from app.services.query_parser import JobQueryParser
from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

parser = JobQueryParser()
job_search_service = get_job_search_service()

@router.post("/linkedin/search")
def linkedin_search(request: JobSearchRequest):
    urls = build_linkedin_urls(request)
    
    return {
        "search": request.model_dump(mode="json"),
        "urls": urls
    }
    

@router.post("/linkedin/search/natural")
# async def natural_language_search(request: NaturalLanguageSearchRequest,):
#     print("\033[93mConverting Human Language into structured search request...\033[0m")
#     linkedin_source = LinkedInSource()
#     search_request = parser.parse(
#         request.query
#     )

#     print(f"\033[93mSearching jobs on LinkedIn for {search_request.locations} location...\033[0m")
#     jobs = linkedin_source.search(search_request)
#     print(f"\033[95mTotal Job Found: {len(jobs)} \033[0m")
#     print("\033[93mFetching description for each job...\033[0m")
#     start_time=datetime.now()
#     for job in jobs:
#         job.description = (
#             linkedin_source.get_job_description(
#                 job,
#                 search_request,
#             )
#         )
#     end_time = datetime.now()
#     processing_time = (end_time - start_time).total_seconds()
#     print(f"Processing time: {processing_time:.2f} seconds")
#     return {
#         "search": search_request.model_dump(
#             mode="json"
#         ),
#         "jobs": jobs,
#     }
def natural_language_search(request: NaturalLanguageSearchRequest):

    print(
        "\033[93m"
        "Converting Human Language into structured search request..."
        "\033[0m"
    )

    linkedin_source = LinkedInSource()

    search_request = parser.parse(
        request.query
    )

    print(
        f"\033[93m"
        f"Searching jobs on LinkedIn for "
        f"{search_request.locations} location..."
        f"\033[0m"
    )

    jobs = linkedin_source.search(
        search_request
    )

    print(
        f"\033[95m"
        f"Total Job Found: {len(jobs)}"
        f"\033[0m"
    )

    print(
        "\033[93m"
        "Fetching description for each job..."
        "\033[0m"
    )

    start_time = datetime.now()

    for job in jobs[:2]:

        job.description = (
            linkedin_source.get_job_description(
                job,
                search_request,
            )
        )

    end_time = datetime.now()

    processing_time = (
        end_time - start_time
    ).total_seconds()

    print(
        f"Processing time: "
        f"{processing_time:.2f} seconds"
    )

    return {
        "search": search_request.model_dump(
            mode="json"
        ),
        "jobs": jobs,
    }