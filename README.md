# Advanced Web Scraper System

Professional web scraping framework with intelligent risk management and anti-detection capabilities.

## Features

**Security & Anti-Detection**
- Undetected Chrome Driver for basic bot detection bypass
- Manual security challenge handling (requires user interaction)
- Smart delays (60-150 seconds) between requests
- Realistic user behavior simulation
- Peak hours detection and avoidance

**Intelligent Risk Management**
- Real-time success rate monitoring
- Adaptive break system based on risk level
- Daily page limits (50 pages max)
- Automatic health checks

**Batch Processing**
- Smart batch processing (10 pages per batch)
- Progress tracking with JSON persistence
- Automatic duplicate removal
- CSV export with proper encoding

## Quick Start

```bash
pip install undetected-chromedriver selenium beautifulsoup4 pandas
python scrap.py
```

**Important**: When security challenges appear, manually complete the verification before the scraper continues automatically.

## Configuration

- `MIN_PAGE_DELAY`: 60 seconds
- `MAX_PAGE_DELAY`: 150 seconds  
- `BATCH_SIZE`: 10 pages
- `DAILY_PAGE_LIMIT`: 50 pages
- `CHALLENGE_WAIT`: 90 seconds (time to complete security challenges)

## Requirements

- Python 3.7+
- Chrome Browser
- Dependencies: undetected-chromedriver, selenium, beautifulsoup4, pandas

## Output Files

- `advanced_web_scraper.log` - System logs
- `total_scrap.csv` - Scraped data
- `batch_progress.json` - Progress tracking

## Legal Notice

For educational purposes only. Respect robots.txt and website terms of service. 