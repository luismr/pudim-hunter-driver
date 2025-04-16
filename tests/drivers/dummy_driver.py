from datetime import datetime
from typing import List

from pudim_hunter_driver.driver import JobDriver
from pudim_hunter_driver.models import Job, JobList, JobQuery
from pudim_hunter_driver.exceptions import AuthenticationError, QueryError


class DummyDriver(JobDriver):
    """A dummy driver implementation for testing and example purposes."""
    
    def __init__(self, is_authenticated: bool = True):
        self.is_authenticated = is_authenticated
        self._dummy_jobs = [
            Job(
                id="dummy-1",
                title="Python Developer",
                company="Dummy Corp",
                location="Remote",
                description="A great job at Dummy Corp!",
                url="https://dummy.jobs/1",
                salary_range="$80k - $120k",
                remote=True,
                posted_at=datetime.now(),
                source="DummyJobs"
            ),
            Job(
                id="dummy-2",
                title="Senior Python Engineer",
                company="Example Inc",
                location="New York, NY",
                description="Senior position at Example Inc",
                url="https://dummy.jobs/2",
                salary_range="$120k - $180k",
                remote=False,
                posted_at=datetime.now(),
                source="DummyJobs"
            )
        ]
    
    async def validate_credentials(self) -> bool:
        """Simulate credential validation."""
        return self.is_authenticated
    
    async def fetch_jobs(self, query: JobQuery) -> JobList:
        """Return dummy jobs based on the query."""
        if not self.is_authenticated:
            raise AuthenticationError("Not authenticated with DummyJobs")
            
        if not query.keywords:
            raise QueryError("Keywords are required for search")
            
        # Simulate filtering based on query
        filtered_jobs: List[Job] = []
        for job in self._dummy_jobs:
            if (query.keywords.lower() in job.title.lower() and
                (not query.location or query.location.lower() in job.location.lower()) and
                (not query.remote or job.remote == query.remote)):
                filtered_jobs.append(job)
                
        # Simulate pagination
        start_idx = (query.page - 1) * query.items_per_page
        end_idx = start_idx + query.items_per_page
        page_jobs = filtered_jobs[start_idx:end_idx]
        
        return JobList(
            jobs=page_jobs,
            total_results=len(filtered_jobs),
            page=query.page,
            items_per_page=query.items_per_page
        ) 