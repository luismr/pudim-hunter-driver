import pytest
from datetime import datetime
from pudim_hunter_driver.models import JobQuery, Job, JobList
from pudim_hunter_driver.exceptions import AuthenticationError, QueryError
from .drivers.dummy_driver import DummyDriver
    

@pytest.fixture
def driver():
    return DummyDriver()


@pytest.fixture
def unauthenticated_driver():
    return DummyDriver(is_authenticated=False)


def test_validate_credentials(driver, unauthenticated_driver):
    """Test credential validation."""
    assert driver.validate_credentials() is True
    assert unauthenticated_driver.validate_credentials() is False


def test_fetch_jobs_basic_search(driver):
    """Test basic job search functionality."""
    query = JobQuery(keywords="Python")
    result = driver.fetch_jobs(query)
    
    assert len(result.jobs) == 2  # Both dummy jobs contain "Python"
    assert result.total_results == 2
    assert result.page == 1
    assert result.items_per_page == 20
    
    # Verify job fields
    job = result.jobs[0]
    assert isinstance(job, Job)
    assert job.id is not None
    assert job.title == "Python Developer"
    assert job.company == "Dummy Corp"
    assert job.location == "Remote"
    assert job.summary == "Exciting opportunity for a Python Developer at Dummy Corp"
    assert "Key Responsibilities" in job.description
    assert job.url.startswith("https://dummy.jobs/")
    assert job.salary_range == "$80k - $120k"
    assert len(job.qualifications) == 4
    assert job.remote is True
    assert isinstance(job.posted_at, datetime)
    assert job.source == "DummyJobs"


def test_fetch_jobs_with_location(driver):
    """Test job search with location filter."""
    query = JobQuery(keywords="Python", location="New York")
    result = driver.fetch_jobs(query)
    
    assert len(result.jobs) == 1
    assert result.jobs[0].location == "New York, NY"


def test_fetch_jobs_with_remote(driver):
    """Test job search with remote filter."""
    query = JobQuery(keywords="Python", remote=True)
    result = driver.fetch_jobs(query)
    
    assert len(result.jobs) == 1
    assert result.jobs[0].remote is True
    assert result.jobs[0].location == "Remote"


def test_fetch_jobs_pagination(driver):
    """Test job search pagination."""
    query = JobQuery(keywords="Python", items_per_page=1, page=2)
    result = driver.fetch_jobs(query)
    
    assert len(result.jobs) == 1
    assert result.total_results == 2
    assert result.page == 2
    assert result.items_per_page == 1
    assert result.jobs[0].title == "Senior Python Engineer"


def test_fetch_jobs_no_results(driver):
    """Test job search with no matching results."""
    query = JobQuery(keywords="NonExistent")
    result = driver.fetch_jobs(query)
    
    assert len(result.jobs) == 0
    assert result.total_results == 0


def test_fetch_jobs_unauthenticated(unauthenticated_driver):
    """Test job search with unauthenticated driver."""
    query = JobQuery(keywords="Python")
    
    with pytest.raises(AuthenticationError):
        unauthenticated_driver.fetch_jobs(query)


def test_fetch_jobs_invalid_query(driver):
    """Test job search with invalid query."""
    query = JobQuery(keywords="")
    
    with pytest.raises(QueryError):
        driver.fetch_jobs(query) 