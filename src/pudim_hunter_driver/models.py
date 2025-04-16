from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class JobQuery(BaseModel):
    """Query parameters for job search."""
    keywords: str
    location: Optional[str] = None
    remote: bool = False
    page: int = 1
    items_per_page: int = 20


class Job(BaseModel):
    """Represents a normalized job posting."""
    id: str
    title: str
    company: str
    location: str
    description: str
    url: str
    salary_range: Optional[str] = None
    remote: bool = False
    posted_at: datetime
    source: str = Field(..., description="The job board source (e.g., 'LinkedIn', 'Indeed')")


class JobList(BaseModel):
    """Container for job search results."""
    jobs: List[Job]
    total_results: int
    page: int
    items_per_page: int 