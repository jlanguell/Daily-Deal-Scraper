# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.2] - 2022-09-27
### Removed
- Unnecessary print statements.

### Added
- Option argument for Chromedriver that stops driver output to terminal

### Changed
- In GUI.py, function name getdepartments() to get_departments()

## [0.1.1] - 2022-09-22
### Changed
- Repository name from dealScraper to DailyDealScraper

### Fixed  
- Fixed typos and non-compliant Python variable names in all .py files

### Added
- Functionality in dealScraper.py to detect local files before loading GUI.py functions. 
  If params.json and number.txt exist, GUI.py functions do not run at all
  
### Removed
- Unused function in whatsapp.py: format_scraped_info()
- Unnecessary comments used in testing
- Unnecessary print() functions used for testing

## [0.1.0] - 2022-09-03
### Added
- Created Repository /dealScraper
- Created version.txt
- Created CHANGELOG.md
- Created README.md
- Created .gitignore (Python template)
- Created requirements.txt
- Created scrape.py
- Added chromedriver.exe

