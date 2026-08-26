from urllib.parse import urlencode
from app.models.job_search import JobSearchRequest, PostTime


POST_TIME_MAP = {
    PostTime.PAST_24_HOURS: "r86400",
    PostTime.PAST_WEEK: "r604800",
    PostTime.PAST_MONTH: "r2592000",
}
BASE_URL = "https://www.linkedin.com/jobs/search/"

def build_linkedin_urls(request: JobSearchRequest) -> list[str]:
    urls = []
    keywords = " ".join(request.keywords)

    for location in request.locations:
        params = {
            "keywords": keywords,
            "location": location
        }
        if request.post_time != PostTime.ANY_TIME:
            params["f_TPR"] = POST_TIME_MAP[request.post_time]

        query_string = urlencode(params)
        url = f"{BASE_URL}?{query_string}"
        urls.append(url)

    return urls


def build_job_detail_url(keywords: str, location: str, job_id: str, post_time: PostTime = PostTime.PAST_24_HOURS,) -> str:

    params = {
        "keywords": keywords,
        "location": location,
        "f_TPR": post_time,
        "currentJobId": job_id,
    }

    return f"{BASE_URL}?{urlencode(params)}"