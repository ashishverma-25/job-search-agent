from pydantic import BaseModel, Field
from enum import Enum

class PostTime(str, Enum):
    ANY_TIME = "any"
    PAST_24_HOURS = "24h"
    PAST_WEEK = "7d"
    PAST_MONTH = "30d"

class JobSearchRequest(BaseModel):
    keywords: list[str] = Field(
        description="Job titles, technologies, or skills to search for"
    )

    locations: list[str] = Field(
        description="Locations where the job should be located"
    )

    post_time: PostTime = Field(
        default=PostTime.ANY_TIME,
        description="How recently the job was posted"
    )

    experience_min: int | None = Field(
        default=None,
        description="Minimum years of experience"
    )

    experience_max: int | None = Field(
        default=None,
        description="Maximum years of experience"
    )