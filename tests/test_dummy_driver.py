import pytest
from pudim_hunter_driver.models import JobQuery
from pudim_hunter_driver.exceptions import AuthenticationError, QueryError
from .drivers.dummy_driver import DummyDriver


@pytest.fixture
def driver():
    return DummyDriver()


@pytest.fixture
def unauthenticated_driver():
    return DummyDriver(is_authenticated=False)


@pytest.mark.asyncio
async def test_validate_credentials(driver, unauthenticated_driver):
    """Test credential validation."""
    assert await driver.validate_credentials() is True
    assert await unauthenticated_driver.validate_credentials() is False


@pytest.mark.asyncio
async def test_fetch_jobs_basic_search(driver):
    """Test basic job search functionality."""
    query = JobQuery(keywords="Python")
    result = await driver.fetch_jobs(query)
    
    assert len(result.jobs) == 2  # Both dummy jobs contain "Python"
    assert result.total_results == 2
    assert result.page == 1
    assert result.items_per_page == 20


@pytest.mark.asyncio
async def test_fetch_jobs_with_location(driver):
    """Test job search with location filter."""
    query = JobQuery(keywords="Python", location="New York")
    result = await driver.fetch_jobs(query)
    
    assert len(result.jobs) == 1
    assert result.jobs[0].location == "New York, NY"


@pytest.mark.asyncio
async def test_fetch_jobs_with_remote(driver):
    """Test job search with remote filter."""
    query = JobQuery(keywords="Python", remote=True)
    result = await driver.fetch_jobs(query)
    
    assert len(result.jobs) == 1
    assert result.jobs[0].remote is True


@pytest.mark.asyncio
async def test_fetch_jobs_pagination(driver):
    """Test job search pagination."""
    query = JobQuery(keywords="Python", items_per_page=1, page=2)
    result = await driver.fetch_jobs(query)
    
    assert len(result.jobs) == 1
    assert result.total_results == 2
    assert result.page == 2
    assert result.items_per_page == 1
    assert result.jobs[0].title == "Senior Python Engineer"


@pytest.mark.asyncio
async def test_fetch_jobs_no_results(driver):
    """Test job search with no matching results."""
    query = JobQuery(keywords="NonExistent")
    result = await driver.fetch_jobs(query)
    
    assert len(result.jobs) == 0
    assert result.total_results == 0


@pytest.mark.asyncio
async def test_fetch_jobs_unauthenticated(unauthenticated_driver):
    """Test job search with unauthenticated driver."""
    query = JobQuery(keywords="Python")
    
    with pytest.raises(AuthenticationError):
        await unauthenticated_driver.fetch_jobs(query)


@pytest.mark.asyncio
async def test_fetch_jobs_invalid_query(driver):
    """Test job search with invalid query."""
    query = JobQuery(keywords="")
    
    with pytest.raises(QueryError):
        await driver.fetch_jobs(query) 