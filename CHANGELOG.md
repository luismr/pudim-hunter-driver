# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2024-03-14

### Added
- Initial project structure with src-based layout
- Base `JobDriver` interface with async support
- Data models using Pydantic:
  - `JobQuery` for search parameters
  - `Job` for normalized job data
  - `JobList` for search results
- Custom exceptions:
  - `DriverError`
  - `AuthenticationError`
  - `QueryError`
  - `RateLimitError`
- Example implementation in tests (`DummyDriver`)
- GitHub Actions workflows:
  - CI/CD with pytest and coverage reporting
  - Package publishing to GitHub Packages
- Documentation:
  - README.md with installation and usage instructions
  - Development setup guide
  - Contributing guidelines
  - MIT License

[0.0.1]: https://github.com/luismr/pudim-hunter-driver/releases/tag/v0.0.1
