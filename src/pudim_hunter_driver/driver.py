from abc import ABC, abstractmethod
from .models import JobQuery, JobList


class JobDriver(ABC):
    """
    Abstract base class defining the interface for job search drivers.
    
    Each job board (LinkedIn, Indeed, etc.) should implement this interface
    to provide a standardized way of searching for jobs.
    """
    
    @abstractmethod
    async def fetch_jobs(self, query: JobQuery) -> JobList:
        """
        Fetch jobs from the job board based on the provided query.
        
        Args:
            query (JobQuery): The search parameters
            
        Returns:
            JobList: A container with the search results
            
        Raises:
            DriverError: If there's an error during the search process
        """
        pass
    
    @abstractmethod
    async def validate_credentials(self) -> bool:
        """
        Validate if the driver has valid credentials to access the job board.
        
        Returns:
            bool: True if credentials are valid, False otherwise
        """
        pass 