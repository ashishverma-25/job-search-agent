from bs4 import BeautifulSoup
from app.models.jobs import Job
from app.services.browser_client import fetch_rendered_html
from app.services.http_client import fetch
from app.services.linkedin_url_builder import build_job_detail_url, build_linkedin_urls
from app.models.job_search import JobSearchRequest


class LinkedInSource:

    def search(self, request: JobSearchRequest) -> list[Job]:
        urls = build_linkedin_urls(request)
        jobs = []

        for url in urls:
            search_html = fetch(url)
            jobs.extend(self.parse_html(search_html))
            
        return jobs
    
    def get_job_description(self,job: Job,request: JobSearchRequest,) -> str | None:
        keywords = " ".join(request.keywords)

        detail_url = build_job_detail_url(
            keywords=keywords,
            location=job.location,
            job_id=job.job_id,
            post_time=request.post_time,
        )
        detail_html = fetch_rendered_html(detail_url)

        return self.parse_job_detail(detail_html)

    def parse_html(self, html: str) -> list[Job]:

        soup = BeautifulSoup(
            html,
            "lxml",
        )

        jobs = []

        job_cards = soup.select(
            "div.job-search-card"
        )

        for card in job_cards:

            title_element = card.select_one(
                ".base-search-card__title"
            )

            company_element = card.select_one(
                ".base-search-card__subtitle"
            )

            location_element = card.select_one(
                ".job-search-card__location"
            )

            posted_element = card.select_one(
                "time"
            )

            link_element = card.select_one(
                "a.base-card__full-link"
            )

            entity_urn = card.get(
                "data-entity-urn"
            )

            job_id = None

            if entity_urn:
                job_id = entity_urn.split(":")[-1]

            if not title_element or not link_element:
                continue

            jobs.append(
                Job(
                    title=title_element.get_text(
                        strip=True
                    ),
                    company=(
                        company_element.get_text(
                            strip=True
                        )
                        if company_element
                        else "Unknown"
                    ),
                    location=(
                        location_element.get_text(
                            strip=True
                        )
                        if location_element
                        else "Unknown"
                    ),
                    posted_time=(
                        posted_element.get_text(
                            strip=True
                        )
                        if posted_element
                        else None
                    ),
                    job_url=link_element.get(
                        "href"
                    ),
                    source="linkedin",
                    job_id=job_id,
                    description=None,
                )
            )

        return jobs

    def parse_job_detail(self, html: str) -> str | None:

        soup = BeautifulSoup(
            html,
            "lxml",
        )

        description = soup.select_one(
            ".description__text.description__text--rich "
            ".show-more-less-html__markup"
        )

        if not description:
            return None

        return description.get_text(
            "\n",
            strip=True,
        )
        
    def get_job_detail_urls(self, jobs: list[Job], request: JobSearchRequest) -> list[str]:

        keywords = " ".join(request.keywords)

        return [
            build_job_detail_url(
                keywords=keywords,
                location=job.location,
                job_id=job.job_id,
                post_time=request.post_time,
            )
            for job in jobs
        ]
    
    def get_job_description(self,job: Job,request: JobSearchRequest,) -> str | None:

        keywords = " ".join(request.keywords)

        detail_url = build_job_detail_url(
            keywords=keywords,
            location=job.location,
            job_id=job.job_id,
            post_time=request.post_time,
        )

        detail_html = fetch_rendered_html(
            detail_url
        )

        return self.parse_job_detail(
            detail_html
        )