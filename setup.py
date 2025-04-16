from setuptools import setup, find_packages

setup(
    name="pudim-hunter-driver",
    version="0.1.0",
    description="Common interface for implementing job search drivers for The Pudim Hunter platform",
    author="The Pudim Hunter Team",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "pydantic>=2.5.0",
        "python-dateutil>=2.8.2",
        "typing-extensions>=4.8.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
) 