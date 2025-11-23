# Email Scraper

A powerful web scraper built with Scrapy and Selenium that automatically extracts email addresses from websites by crawling through contact and about pages.

## Features

- **Intelligent Crawling**: Automatically identifies and prioritizes contact and about pages
- **Selenium Integration**: Handles JavaScript-rendered content seamlessly
- **Email Validation**: Filters emails by valid domain extensions (.com, .org, .edu, .net, .in, .np)
- **Duplicate Prevention**: Uses set-based storage to ensure unique email collection
- **Social Media Filtering**: Excludes emails from social media platforms (Facebook, Instagram, Twitter, YouTube, LinkedIn, Wikipedia)
- **Regex-Based Extraction**: Robust email pattern matching across web pages

## Prerequisites

- Python 3.7+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. **Clone or download this project**

2. **Install required packages:**
   ```bash
   pip install scrapy scrapy-selenium selenium
   ```

3. **Download ChromeDriver:**
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Download the version matching your Chrome browser
   - Extract and place `chromedriver.exe` in the project directory

4. **Update ChromeDriver path:**
   - Open `EmailScraperWeb/settings.py`
   - Update `SELENIUM_DRIVER_EXECUTABLE_PATH` with your ChromeDriver location

## Configuration

Edit `EmailScraperWeb/spiders/EmailScrape.py` to customize:

- **Target URL**: Change the starting URL in the `start_requests()` method
  ```python
  url="https://www.divyagyan.edu.np/"  # Replace with your target website
  ```

- **Contact Keywords**: Modify the keywords to target specific pages
  ```python
  contact_keywords = ["contact", "about"]  # Add more keywords as needed
  ```

- **Valid Domains**: Customize acceptable email domains
  ```python
  valid_domains = [".in", ".com", ".org", ".edu", ".net", ".np"]
  ```

## Usage

1. **Navigate to the project directory:**
   ```bash
   cd "d:\College\Eprabidhi\Python\Email Scraper\EmailScraperWeb"
   ```

2. **Run the spider:**
   ```bash
   scrapy crawl GetEmail
   ```

3. **View results:**
   - Emails are printed to the console at the end of the crawl
   - Results are sorted and deduplicated automatically

## Project Structure

```
Email Scraper/
├── EmailScraperWeb/
│   ├── scrapy.cfg              # Scrapy configuration
│   ├── chromedriver-win64/     # ChromeDriver directory
│   └── EmailScraperWeb/
│       ├── spiders/
│       │   └── EmailScrape.py  # Main spider logic
│       ├── settings.py         # Scrapy settings & Selenium config
│       ├── items.py            # Data models
│       ├── pipelines.py        # Data processing pipelines
│       └── middlewares.py      # Custom middlewares
└── README.md                   # This file
```

## How It Works

1. **Initial Request**: Starts by loading the target website with Selenium
2. **Link Extraction**: Extracts all links and filters for contact/about pages
3. **Recursive Crawling**: Visits filtered pages and extracts email addresses
4. **Validation**: Filters out invalid emails and social media links
5. **Finalization**: Outputs unique, validated email addresses

## Settings

Key settings in `settings.py`:

- `ROBOTSTXT_OBEY = True`: Respects robots.txt rules
- `CONCURRENT_REQUESTS_PER_DOMAIN = 1`: Polite crawling with one request at a time
- `DOWNLOAD_DELAY = 1`: 1-second delay between requests
- `SELENIUM_DRIVER_NAME = "chrome"`: Uses Chrome browser

## Output Example

```
==================================================
Email Scraping Complete!
Found 5 valid emails:
  - contact@example.com
  - info@example.org
  - support@example.edu.np
  - admin@example.net
  - hello@example.in
==================================================
```

## Troubleshooting

- **ChromeDriver error**: Ensure ChromeDriver version matches your Chrome browser
- **No emails found**: Check if the website loads properly and contains visible emails
- **Timeout errors**: Increase `wait_time` parameter in SeleniumRequest calls
- **Permission errors**: Run with appropriate permissions or update file paths

## Legal & Ethical Considerations

- Always respect website terms of service
- Follow robots.txt guidelines
- Use scraped data responsibly and ethically
- Consider privacy laws and regulations (GDPR, CCPA, etc.)
- Implement appropriate rate limiting to avoid server overload

## Contact

**Made by:** Prashon  
**Email:** mr.prashon@gmail.com

## License

This project is provided as-is for educational purposes.

---

*Happy Scraping! 🕷️*
