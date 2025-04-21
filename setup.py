from setuptools import setup, find_packages
import os

def get_requirements():
    """Get requirements from requirements.txt"""
    requirements = []
    try:
        with open('requirements.txt') as f:
            requirements = [line.strip() for line in f.readlines() if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        # Fallback to minimal requirements if file not found
        requirements = [
            "pydantic>=2.5.0",
            "python-dateutil>=2.8.2",
            "typing-extensions>=4.8.0",
        ]
    return requirements

# Read README.md for long description
try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Common interface for implementing job search drivers for The Pudim Hunter platform"

setup(
    name="pudim-hunter-driver",
    use_scm_version={
        "version_scheme": "post-release",
        "local_scheme": "node-and-date",
        "write_to": "src/pudim_hunter_driver/_version.py",
        "fallback_version": "0.0.1.dev0"
    },
    description="Common interface for implementing job search drivers for The Pudim Hunter platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Pudim Hunter Team",
    author_email="luis.reis@gmail.com",
    url="https://github.com/luismr/pudim-hunter-driver",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=get_requirements(),
    setup_requires=['setuptools_scm'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Source": "https://github.com/luismr/pudim-hunter-driver",
        "Bug Tracker": "https://github.com/luismr/pudim-hunter-driver/issues",
    }
) 