from app.models.jobs import Job
from app.sources.base import JobSource


class MockLinkedInSource(JobSource):

    def search(self, url: str) -> list[Job]:

        return [
            Job(
                title="Senior Python Backend Developer",
                company="ABC Technologies",
                location="Bengaluru",
                posted_time="6 hours ago",
                description=(
                    "Build scalable backend services using "
                    "Python, FastAPI, Docker and Kubernetes."
                ),
                job_url="https://www.linkedin.com/jobs/view/1234567890/",
                source="linkedin",
            ),
            Job(
                title="Python Developer",
                company="XYZ Technologies",
                location="Noida",
                posted_time="10 hours ago",
                description=(
                    "Develop REST APIs using Python and FastAPI "
                    "and work with MySQL."
                ),
                job_url="https://www.linkedin.com/jobs/view/9876543210/",
                source="linkedin",
            ),
        ]