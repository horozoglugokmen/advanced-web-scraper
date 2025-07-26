#!/usr/bin/env python3
"""
=====================================
Advanced web scraper system - Anti-detection, batch processing and intelligent risk management
=====================================
"""

import time
import random
import json
import os
from datetime import datetime, timedelta
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import logging

# ================================
# LOGGING SETUP
# ================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('advanced_web_scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ================================
# ADVANCED WEB SCRAPER SYSTEM
# ================================

class HybridBatchScraper:
    
    def __init__(self):
        self.driver = None
        self.listings = []
        self.scraped_pages = 0
        self.current_batch = None
        
        # SECURITY SETTINGS
        self.MIN_PAGE_DELAY = 60
        self.MAX_PAGE_DELAY = 150
        self.CHALLENGE_WAIT = 90
        self.MIN_PAGE_ACTIVITY = 45
        self.MAX_PAGE_ACTIVITY = 120
        
        # BATCH SETTINGS
        self.BATCH_SIZE = 10
        self.TOTAL_CSV_FILE = "total_scrap.csv"
        self.PROGRESS_FILE = "batch_progress.json"
        
        # HYBRID CONTINUATION RULES
        self.continuation_rules = {
            'same_day_max_batches': 1,      # Only 1 batch per day
            'min_break_minutes': 15,        
            'max_break_minutes': 45,        
            'daily_page_limit': 50,         # 50 page limit
            'success_threshold': 90,        
            'peak_hours': (9, 17),         
            'off_peak_hours': (18, 23)     
        }
        
        # BATCH DEFINITIONS
        self.batches = [
            {'id': 1, 'start': 51, 'end': 60, 'name': 'Batch 1 (51-60)'}
        ]
        
        # SYSTEM STATS
        self.stats = {
            'total_pages_scraped': 0,
            'successful_pages': 0,
            'failed_pages': 0,
            'total_listings': 0,
            'avg_response_time': 0,
            'session_start_time': time.time()
        }
        
        # Load existing progress
        self.load_progress()
        
    def load_progress(self):
        """Load existing progress"""
        try:
            if os.path.exists(self.PROGRESS_FILE):
                with open(self.PROGRESS_FILE, 'r') as f:
                    progress = json.load(f)
                    
                logger.info(f"Progress loaded: {progress}")
                return progress
            else:
                logger.info("Creating new progress file")
                return self.create_initial_progress()
                
        except Exception as e:
            logger.error(f"Progress loading error: {e}")
            return self.create_initial_progress()
    
    def create_initial_progress(self):
        """Create initial progress file"""
        progress = {
            'current_batch_id': 1,
            'completed_batches': [],
            'daily_pages_scraped': 0,
            'last_scrape_date': datetime.now().strftime('%Y-%m-%d'),
            'session_stats': self.stats
        }
        self.save_progress(progress)
        return progress
    
    def save_progress(self, progress_data):
        """Save progress"""
        try:
            with open(self.PROGRESS_FILE, 'w') as f:
                json.dump(progress_data, f, indent=2)
            logger.info("Progress saved")
        except Exception as e:
            logger.error(f"Progress saving error: {e}")
    
    def get_next_batch(self):
        """Get next batch"""
        progress = self.load_progress()
        current_batch_id = progress.get('current_batch_id', 1)
        
        for batch in self.batches:
            if batch['id'] == current_batch_id:
                return batch
        
        return None
    
    def setup_driver(self):
        """Secure driver setup"""
        logger.info("Setting up secure Chrome driver...")
        
        try:
            options = uc.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-plugins')
            options.add_argument('--window-size=1920,1080')
            options.add_argument('--lang=tr-TR')
            options.add_experimental_option('prefs', {
                'intl.accept_languages': 'tr-TR,tr,en-US,en'
            })
            
            self.driver = uc.Chrome(options=options, version_main=None)
            
            # Anti-detection scripts
            self.driver.execute_script("""
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
                Object.defineProperty(navigator, 'plugins', {
                    get: () => [1, 2, 3, 4, 5]
                });
                Object.defineProperty(navigator, 'languages', {
                    get: () => ['tr-TR', 'tr', 'en-US', 'en']
                });
                window.chrome = { runtime: {} };
            """)
            
            logger.info("Secure Chrome driver successfully initialized")
            return True
            
        except Exception as e:
            logger.error(f"Driver setup failed: {e}")
            return False
    
    def advanced_same_page_scrolling(self):
        """Simplified scroll system"""
        logger.info("Starting scroll system...")
        
        for i in range(3):
            self.driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, -200);")
            time.sleep(2)
        
        logger.info("Scroll completed")
    
    def realistic_page_activity(self):
        """Realistic page activity"""
        activity_duration = random.uniform(self.MIN_PAGE_ACTIVITY, self.MAX_PAGE_ACTIVITY)
        logger.info(f"Realistic activity: {activity_duration:.1f} seconds")
        
        end_time = time.time() + activity_duration
        
        while time.time() < end_time:
            activity = random.choice([
                lambda: self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);"),
                lambda: self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);"),
                lambda: self.driver.execute_script("window.scrollBy(0, 300);"),
                lambda: self.simulate_mouse_movement()
            ])
            
            try:
                activity()
            except Exception as e:
                logger.warning(f"Activity error: {e}")
            
            time.sleep(random.uniform(1, 4))
    
    def simulate_mouse_movement(self):
        """Mouse movement simulation"""
        try:
            x = random.randint(100, 1800)
            y = random.randint(100, 900)
            
            self.driver.execute_script(f"""
                document.dispatchEvent(new MouseEvent('mousemove', {{
                    clientX: {x},
                    clientY: {y}
                }}));
            """)
        except Exception as e:
            logger.warning(f"Mouse movement error: {e}")
    
    def smart_page_delay(self):
        """Smart page delay"""
        delay = random.uniform(self.MIN_PAGE_DELAY, self.MAX_PAGE_DELAY)
        logger.info(f"Page delay: {delay:.1f} seconds")
        
        # Split delay into chunks
        chunks = random.randint(3, 6)
        chunk_size = delay / chunks
        
        for i in range(chunks):
            if i % 2 == 0:
                time.sleep(chunk_size)
            else:
                self.simulate_mouse_movement()
                time.sleep(chunk_size - 1)
    
    def scrape_page(self, page_num):
        """Page scraping"""
        page_start_time = time.time()
        
        try:
            # Build URL - replace with your target URL pattern
            if page_num == 1:
                url = "https://example-realestate-site.com/listings"
            else:
                offset = (page_num - 1) * 20
                url = f"https://example-realestate-site.com/listings?offset={offset}&page={page_num}"
            
            logger.info(f"Scraping page {page_num}: {url}")
            
            # Navigate to page
            self.driver.get(url)
            
            # AJAX wait
            time.sleep(5)
            
            # Initial loading wait
            initial_wait = random.uniform(5, 12)
            logger.info(f"Initial loading wait: {initial_wait:.1f} seconds")
            time.sleep(initial_wait)
            
            # Scroll and activity
            self.advanced_same_page_scrolling()
            self.realistic_page_activity()
            
            # Parse HTML
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            listings = soup.find_all('tr', class_='searchResultsItem')
            
            if not listings:
                logger.warning(f"No listings found on page {page_num}")
                self.stats['failed_pages'] += 1
                return False
            
            # Process listings
            page_listings = []
            for i, listing in enumerate(listings):
                listing_data = self.extract_listing_data(listing, i+1, page_num)
                if listing_data:
                    page_listings.append(listing_data)
            
            self.listings.extend(page_listings)
            self.scraped_pages += 1
            self.stats['successful_pages'] += 1
            self.stats['total_listings'] += len(page_listings)
            
            # Update response time
            response_time = time.time() - page_start_time
            self.stats['avg_response_time'] = (
                (self.stats['avg_response_time'] * (self.stats['successful_pages'] - 1) + response_time) 
                / self.stats['successful_pages']
            )
            
            logger.info(f"Page {page_num}: {len(page_listings)} listings scraped")
            return True
            
        except Exception as e:
            logger.error(f"Page {page_num} scraping error: {e}")
            self.stats['failed_pages'] += 1
            return False
    
    def extract_listing_data(self, listing, index, page_num):
        """Listing data extraction"""
        try:
            title_elem = listing.find('a', class_='classifiedTitle')
            title = title_elem.get_text(strip=True) if title_elem else "N/A"
            url = "https://example-realestate-site.com" + title_elem.get('href') if title_elem else "N/A"
            
            price_elem = listing.find('td', class_='searchResultsPriceValue')
            price = price_elem.get_text(strip=True) if price_elem else "N/A"
            
            location_elem = listing.find('td', class_='searchResultsLocationValue')
            location = location_elem.get_text(strip=True) if location_elem else "N/A"
            
            date_elem = listing.find('td', class_='searchResultsDateValue')
            date = date_elem.get_text(strip=True) if date_elem else "N/A"
            
            attributes = listing.find_all('td', class_='searchResultsAttributeValue')
            
            listing_data = {
                'index': index,
                'title': title,
                'url': url,
                'price': price,
                'location': location,
                'date': date,
                'room_count': attributes[0].get_text(strip=True) if len(attributes) > 0 else "N/A",
                'area': attributes[1].get_text(strip=True) if len(attributes) > 1 else "N/A",
                'floor': attributes[2].get_text(strip=True) if len(attributes) > 2 else "N/A",
                'age': attributes[3].get_text(strip=True) if len(attributes) > 3 else "N/A",
                'scraped_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'page_number': page_num
            }
            
            return listing_data
            
        except Exception as e:
            logger.warning(f"Page {page_num} - Listing {index} processing error: {e}")
            return None
    
    def load_existing_data(self):
        """Load existing total_scrap.csv file"""
        try:
            if os.path.exists(self.TOTAL_CSV_FILE):
                existing_df = pd.read_csv(self.TOTAL_CSV_FILE, encoding='utf-8')
                logger.info(f"Existing {self.TOTAL_CSV_FILE} loaded: {len(existing_df)} records")
                return existing_df
            else:
                logger.info(f"{self.TOTAL_CSV_FILE} file not found, creating new file")
                return pd.DataFrame()
        except Exception as e:
            logger.error(f"Existing data loading error: {e}")
            return pd.DataFrame()
    
    def remove_duplicates(self, new_df, existing_df):
        """Remove duplicate records"""
        if existing_df.empty:
            return new_df
        
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)
        deduplicated_df = combined_df.drop_duplicates(subset=['url'], keep='last')
        new_records = deduplicated_df[~deduplicated_df['url'].isin(existing_df['url'])]
        
        logger.info(f"Duplicate check: {len(new_df)} new -> {len(new_records)} unique")
        return new_records
    
    def save_batch_data(self):
        """Save batch data"""
        if not self.listings:
            return
        
        try:
            existing_df = self.load_existing_data()
            new_df = pd.DataFrame(self.listings)
            unique_new_df = self.remove_duplicates(new_df, existing_df)
            
            if not unique_new_df.empty:
                if existing_df.empty:
                    unique_new_df.to_csv(self.TOTAL_CSV_FILE, index=False, encoding='utf-8', mode='w')
                else:
                    unique_new_df.to_csv(self.TOTAL_CSV_FILE, index=False, encoding='utf-8', mode='a', header=False)
                
                logger.info(f"{len(unique_new_df)} new records added to {self.TOTAL_CSV_FILE}")
            else:
                logger.info("No new unique records found")
                
        except Exception as e:
            logger.error(f"Batch data saving error: {e}")
    
    def calculate_success_rate(self):
        """Calculate success rate"""
        total_pages = self.stats['successful_pages'] + self.stats['failed_pages']
        if total_pages == 0:
            return 100
        return (self.stats['successful_pages'] / total_pages) * 100
    
    def assess_risk_level(self):
        """Assess risk level"""
        success_rate = self.calculate_success_rate()
        avg_response_time = self.stats['avg_response_time']
        
        if success_rate >= 95 and avg_response_time < 3:
            return "LOW"
        elif success_rate >= 85 and avg_response_time < 5:
            return "MEDIUM"
        else:
            return "HIGH"
    
    def is_peak_hours(self):
        """Check if in peak hours"""
        current_hour = datetime.now().hour
        peak_start, peak_end = self.continuation_rules['peak_hours']
        return peak_start <= current_hour <= peak_end
    
    def calculate_optimal_break(self):
        """Calculate optimal break duration"""
        base_break = self.continuation_rules['min_break_minutes']
        max_break = self.continuation_rules['max_break_minutes']
        
        # Adjust based on risk level
        risk_level = self.assess_risk_level()
        
        if risk_level == "LOW":
            return random.uniform(base_break, base_break + 30)
        elif risk_level == "MEDIUM":
            return random.uniform(base_break + 30, base_break + 60)
        else:
            return random.uniform(base_break + 60, max_break)
    
    def decide_continuation(self, completed_batch):
        """Smart continuation decision - HYBRID CORE"""
        logger.info(f"Batch {completed_batch['id']} completed, making continuation decision...")
        
        progress = self.load_progress()
        
        # 1. Daily limit check
        if progress['daily_pages_scraped'] >= self.continuation_rules['daily_page_limit']:
            logger.info("Daily page limit exceeded")
            return self.schedule_tomorrow()
        
        # 2. Same day batch limit check
        completed_today = len([b for b in progress['completed_batches'] 
                              if b.get('date') == datetime.now().strftime('%Y-%m-%d')])
        
        if completed_today >= self.continuation_rules['same_day_max_batches']:
            logger.info("Same day batch limit exceeded")
            return self.schedule_tomorrow()
        
        # 3. System health check
        success_rate = self.calculate_success_rate()
        if success_rate < self.continuation_rules['success_threshold']:
            logger.info(f"Low success rate: {success_rate:.1f}%")
            return self.schedule_tomorrow()
        
        # 4. Time check
        current_hour = datetime.now().hour
        if current_hour >= 18:  # After 6 PM
            logger.info("Evening hours, continuing tomorrow")
            return self.schedule_tomorrow()
        
        # 5. All checks OK - continue
        logger.info("All checks OK, continuing")
        return self.continue_with_break()
    
    def continue_with_break(self):
        """Continue with safe break"""
        break_duration = self.calculate_optimal_break()
        
        logger.info(f"{break_duration:.0f} minute break, then next batch")
        
        # Break activities
        self.intelligent_break(break_duration)
        
        # Move to next batch
        return "CONTINUE"
    
    def schedule_tomorrow(self):
        """Schedule for tomorrow"""
        logger.info("Continuing tomorrow at the same time")
        
        # Update progress
        progress = self.load_progress()
        progress['next_session_time'] = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
        self.save_progress(progress)
        
        return "TOMORROW"
    
    def intelligent_break(self, duration_minutes):
        """Intelligent break system"""
        logger.info(f"{duration_minutes:.0f} minute intelligent break starting...")
        
        # Close browser
        if self.driver:
            self.driver.quit()
            self.driver = None
        
        # Simulate break activities
        break_activities = [
            ("Coffee break", 0.3),
            ("Email check", 0.2),
            ("Social media", 0.2),
            ("Rest", 0.3)
        ]
        
        total_seconds = duration_minutes * 60
        
        for activity_name, ratio in break_activities:
            activity_duration = total_seconds * ratio
            logger.info(f"{activity_name}: {activity_duration/60:.1f} minutes")
            time.sleep(activity_duration)
        
        logger.info("Break completed, starting new session")
        
        # New browser session
        self.setup_driver()
    
    def run_batch(self, batch_info):
        """Run single batch"""
        logger.info(f"{batch_info['name']} starting: {batch_info['start']}-{batch_info['end']}")
        
        self.current_batch = batch_info
        self.listings = []  # Clean for batch
        
        # Scrape batch pages
        for page in range(batch_info['start'], batch_info['end'] + 1):
            success = self.scrape_page(page)
            
            if not success:
                logger.error(f"Page {page} failed")
                # Continue, just log
            
            # Page delay (except last page)
            if page < batch_info['end']:
                self.smart_page_delay()
        
        # Save batch data
        self.save_batch_data()
        
        # Update progress
        progress = self.load_progress()
        progress['completed_batches'].append({
            'id': batch_info['id'],
            'name': batch_info['name'],
            'start': batch_info['start'],
            'end': batch_info['end'],
            'completed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'date': datetime.now().strftime('%Y-%m-%d'),
            'pages_scraped': len(range(batch_info['start'], batch_info['end'] + 1)),
            'listings_found': len(self.listings)
        })
        progress['daily_pages_scraped'] += len(range(batch_info['start'], batch_info['end'] + 1))
        progress['current_batch_id'] = batch_info['id'] + 1
        progress['session_stats'] = self.stats
        
        self.save_progress(progress)
        
        logger.info(f"{batch_info['name']} completed: {len(self.listings)} listings")
        
        return True
    
    def run_hybrid_system(self):
        """Main hybrid system"""
        logger.info("Hybrid Batch Scraper starting...")
        
        try:
            # Setup driver
            if not self.setup_driver():
                logger.error("Driver setup failed")
                return
            
            # Get next batch
            next_batch = self.get_next_batch()
            
            if not next_batch:
                logger.info("All batches completed!")
                return
            
            # Run batch
            batch_success = self.run_batch(next_batch)
            
            if not batch_success:
                logger.error("Batch failed")
                return
            
            # Make continuation decision
            decision = self.decide_continuation(next_batch)
            
            if decision == "CONTINUE":
                # Move to next batch
                self.run_hybrid_system()  # Recursive call
            elif decision == "TOMORROW":
                logger.info("System will continue tomorrow")
            
        except KeyboardInterrupt:
            logger.info("\nStopped by user")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
        finally:
            if self.driver:
                self.driver.quit()
                logger.info("Browser closed")
    
    def print_final_stats(self):
        """Show final statistics"""
        final_df = self.load_existing_data()
        
        print(f"\nHYBRID BATCH SCRAPER REPORT")
        print(f"=" * 50)
        print(f"Pages scraped this session: {self.stats['successful_pages']}")
        print(f"Listings found this session: {self.stats['total_listings']}")
        print(f"Success rate: {self.calculate_success_rate():.1f}%")
        print(f"Average response time: {self.stats['avg_response_time']:.2f} seconds")
        
        if not final_df.empty:
            print(f"\nTOTAL STATISTICS:")
            print(f"   Total listings: {len(final_df)}")
            print(f"   Most common location: {final_df['location'].value_counts().index[0] if not final_df['location'].empty else 'N/A'}")
            print(f"   Most common room type: {final_df['room_count'].value_counts().index[0] if not final_df['room_count'].empty else 'N/A'}")

def main():
    """Main function"""
    print("Advanced Web Scraper System")
    print("=" * 50)
    
    scraper = HybridBatchScraper()
    
    try:
        scraper.run_hybrid_system()
        scraper.print_final_stats()
    except Exception as e:
        logger.error(f"Main system error: {e}")

if __name__ == "__main__":
    main()
    
    