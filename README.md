# Pudim Hunter Driver 🍮

[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Pytest 7.4](https://img.shields.io/badge/pytest-7.4-brightgreen.svg)](https://docs.pytest.org/en/7.4.x/)
[![CI](https://github.com/luismr/pudim-hunter-driver/actions/workflows/ci.yml/badge.svg)](https://github.com/luismr/pudim-hunter-driver/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/luismr/pudim-hunter-driver/branch/main/graph/badge.svg)](https://codecov.io/gh/luismr/pudim-hunter-driver)
[![PyPI version](https://badge.fury.io/py/pudim-hunter-driver.svg)](https://pypi.org/project/pudim-hunter-driver/)

## Table of Contents
- [Features](#features)
- [Usage](#usage)
  - [Installation](#installation)
  - [Interface Overview](#interface-overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Virtual Environment Setup](#virtual-environment-setup)
  - [Prerequisites](#prerequisites)
  - [macOS and Linux](#macos-and-linux)
  - [Windows](#windows)
  - [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Contributing](#contributing)
  - [Getting Started](#getting-started)
  - [Pull Request Process](#pull-request-process)
  - [Repository](#repository)
- [License](#license)

A Python package that provides a common interface for implementing job search drivers for The Pudim Hunter platform.

## Features

- Common interface for implementing job board drivers
- Standardized job search query format
- Normalized job posting data structure
- Type hints and validation using Pydantic
- Async support for better performance
- Built-in error handling

## Usage

### Installation

You can install the package directly from PyPI:

```bash
# Install directly using pip
pip install pudim-hunter-driver

# Or add to your requirements.txt
pudim-hunter-driver>=0.0.2  # Replace with the version you need
```

For development installations, see the [Development](#development) section.

### Interface Overview

This package provides the base interface and models for implementing job search drivers. To create a driver for a specific job board, you'll need to create a new package that depends on `pudim-hunter-driver` and implement the `JobDriver` interface.

1. `JobDriver` (ABC) - The base interface that all drivers must implement:
   - `fetch_jobs(query: JobQuery) -> JobList`
   - `validate_credentials() -> bool`

2. Data Models:
   - `JobQuery` - Search parameters
   - `Job` - Normalized job posting data
   - `JobList` - Container for search results

3. Exceptions:
   - `DriverError` - Base exception
   - `AuthenticationError` - For credential issues
   - `QueryError` - For search query issues
   - `RateLimitError` - For rate limiting issues

### Example Implementation

Here's a basic example of how to implement a job driver:

```python
from datetime import datetime
from pudim_hunter_driver.driver import JobDriver
from pudim_hunter_driver.models import Job, JobList, JobQuery
from pudim_hunter_driver.exceptions import AuthenticationError

class MyJobBoardDriver(JobDriver):
    def validate_credentials(self) -> bool:
        # Implement your authentication logic
        return True

    def fetch_jobs(self, query: JobQuery) -> JobList:
        # Implement your job search logic
        jobs = [
            Job(
                id="job-1",
                title="Python Developer",
                company="Example Corp",
                location="Remote",
                summary="Exciting opportunity for a Python Developer",
                description="""Join our team as a Python Developer! We're looking for someone with strong programming skills and passion for clean code.

Key Responsibilities:
- Develop and maintain Python applications
- Write clean, maintainable, and efficient code
- Collaborate with cross-functional teams
- Participate in code reviews
- Implement best practices and coding standards""",
                url="https://example.com/jobs/1",
                salary_range="$80,000 - $120,000",
                qualifications=[
                    "3+ years Python experience",
                    "Experience with web frameworks",
                    "Strong problem-solving skills"
                ],
                remote=True,
                posted_at=datetime.now(),
                source="MyJobBoard"
            )
        ]
        
        return JobList(
            jobs=jobs,
            total_results=1,
            page=query.page,
            items_per_page=query.items_per_page
        )
```

For a complete working example with tests, check out the `DummyDriver` implementation in the [tests/drivers/dummy_driver.py](tests/drivers/dummy_driver.py) file.

## Project Structure

```
pudim-hunter-driver/
├── src/
│   └── pudim_hunter_driver/
│       ├── __init__.py          # Package initialization
│       ├── driver.py            # JobDriver interface
│       ├── models.py            # Data models
│       └── exceptions.py        # Custom exceptions
├── tests/                       # Test directory
│   └── __init__.py
├── README.md                    # This file
├── requirements.txt             # Direct dependencies
├── setup.py                     # Package setup
└── pyproject.toml              # Project configuration
```

## Installation

From PyPI (coming soon):
```bash
pip install pudim-hunter-driver
```

From source:
```bash
git clone git@github.com:luismr/pudim-hunter-driver.git
cd pudim-hunter-driver
pip install -r requirements.txt
```

For development:
```bash
pip install -e .
```

## Virtual Environment Setup

We strongly recommend using a virtual environment for development and testing. This isolates the project dependencies from your system Python packages.

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- venv module (usually comes with Python 3)

### macOS and Linux

1. Open Terminal and navigate to the project directory:
```bash
cd pudim-hunter-driver
```

2. Create a virtual environment:
```bash
python3.9 -m venv venv
```

3. Activate the virtual environment:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
pip install -e .  # for development
```

5. To deactivate when done:
```bash
deactivate
```

### Windows

1. Open Command Prompt or PowerShell and navigate to the project directory:
```cmd
cd pudim-hunter-driver
```

2. Create a virtual environment:
```cmd
python -m venv venv
```

3. Activate the virtual environment:
- In Command Prompt:
```cmd
.\venv\Scripts\activate.bat
```
- In PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

4. Install dependencies:
```cmd
pip install -r requirements.txt
pip install -e .  # for development
```

5. To deactivate when done:
```cmd
deactivate
```

### Troubleshooting

#### macOS/Linux
- If `python3.9` is not found, install it using your package manager:
  - macOS (with Homebrew): `brew install python@3.9`
  - Ubuntu/Debian: `sudo apt-get install python39 python39-venv`
  - CentOS/RHEL: `sudo yum install python39 python39-devel`

#### Windows
- Ensure Python is added to your PATH during installation
- If PowerShell execution policy prevents activation:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

## Development

1. Create and activate a virtual environment:
```bash
python3.9 -m venv venv
source venv/bin/activate
```

2. Install in development mode:
```bash
pip install -e .
```

## Contributing

We love your input! We want to make contributing to Pudim Hunter Driver as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

### Getting Started

1. Fork the repository
   ```bash
   # Clone the repository
   git clone git@github.com:luismr/pudim-hunter-driver.git
   cd pudim-hunter-driver
   
   # Create your feature branch
   git checkout -b feature/amazing-feature
   
   # Set up development environment
   python3.9 -m venv venv
   source venv/bin/activate
   pip install -e .
   ```

2. Make your changes
   - Write clear, concise commit messages
   - Add tests for any new functionality
   - Ensure all tests pass: `pytest tests/ -v`

3. Push to your fork and submit a pull request
   ```bash
   git push origin feature/amazing-feature
   ```

### Pull Request Process

1. Update the README.md with details of changes if needed
2. Add any new dependencies to requirements.txt
3. Update the tests if needed
4. The PR will be merged once you have the sign-off of the maintainers

### Repository

- Main repository: [github.com/luismr/pudim-hunter-driver](https://github.com/luismr/pudim-hunter-driver)
- Issue tracker: [github.com/luismr/pudim-hunter-driver/issues](https://github.com/luismr/pudim-hunter-driver/issues)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Copyright (c) 2024-2025 Luis Machado Reis 