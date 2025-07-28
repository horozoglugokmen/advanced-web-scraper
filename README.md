# Real Estate Web Scraper System

Professional real estate data collection framework with intelligent risk management and anti-detection capabilities.

Specialized for scraping property listings from real estate websites with advanced security features and batch processing.

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

**Real Estate Data Processing**
- Smart batch processing (10 property pages per batch)
- Property data extraction (title, price, location, rooms, area, etc.)
- Progress tracking with JSON persistence
- Automatic duplicate property removal
- CSV export with proper encoding for real estate data

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
- `total_scrap.csv` - Scraped real estate property data
- `batch_progress.json` - Scraping progress tracking

## Legal Notice

For educational purposes only. Respect robots.txt and website terms of service. 