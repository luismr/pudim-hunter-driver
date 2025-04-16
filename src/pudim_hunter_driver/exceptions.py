class DriverError(Exception):
    """Base exception for all driver-related errors."""
    pass


class AuthenticationError(DriverError):
    """Raised when there's an authentication error with the job board."""
    pass


class QueryError(DriverError):
    """Raised when there's an error with the search query."""
    pass


class RateLimitError(DriverError):
    """Raised when the job board's rate limit is exceeded."""
    pass 