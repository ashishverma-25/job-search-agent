from pathlib import Path
from app.sources.linkedin import LinkedInSource
from app.services.http_client import fetch
from app.services.linkedin_url_builder import build_job_detail_url
from app.services.browser_client import fetch_rendered_html
from urllib.parse import urlencode

BASE_URL = "https://www.linkedin.com/jobs/search/"
def test_linkedin_source():
    source = LinkedInSource()
    
    params = {
        "keywords": "Python Developer",
        "location": "Gurugram"
    }
    params["f_TPR"] = "24h"

    query_string = urlencode(params)
    url = f"{BASE_URL}?{query_string}"

    search_html = fetch(url)
    jobs = source.parse_html(search_html)

    assert len(jobs) > 0

    job = jobs[0]

    assert job.title
    assert job.company
    assert job.location
    assert job.posted_time
    assert job.job_url
    assert job.job_id
    assert job.source == "linkedin"

    print("\nJob:")
    print(job.model_dump())

    detail_url = build_job_detail_url(
        keywords="python developer",
        location=job.location,
        job_id=job.job_id,
        post_time="r86400",
    )

    detail_html = fetch_rendered_html(detail_url)

    description = source.parse_job_detail(detail_html)
    print("HTML length:", len(detail_html))
    assert description is not None
    assert len(description) > 0

    print("\nDescription:")
    print(description)

    assert "Python" in description