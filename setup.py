from setuptools import setup, find_packages
import os

def get_version():
    # Get version from git tag if available
    version = os.environ.get('GITHUB_REF', '')
    if version.startswith('refs/tags/v'):
        return version.split('/')[-1][1:]  # Remove 'v' prefix
    return "0.0.2" 

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="pudim_hunter_driver",
    version=get_version(),
    description="Common interface for implementing job search drivers for The Pudim Hunter platform",
    author="Luis Machado Reis",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={
        "Source": "https://github.com/luismr/pudim-hunter-driver",
        "Bug Tracker": "https://github.com/luismr/pudim-hunter-driver/issues",
    }
) 