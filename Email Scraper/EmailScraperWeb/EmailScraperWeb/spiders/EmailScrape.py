import scrapy
import re
from scrapy_selenium import SeleniumRequest
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor


class EmailScraperWeb(scrapy.Spider):
    name = "GetEmail"
    uniqueEmail = set()

    def start_requests(self):
        yield SeleniumRequest(
            url="https://www.divyagyan.edu.np/",
            wait_time=5,
            screenshot=True,
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, response):
        link_extractor = LxmlLinkExtractor(allow=())
        all_links = link_extractor.extract_links(response)

        contact_keywords = ["contact", "about"]
        filtered_links = [
            link.url for link in all_links
            if any(keyword in link.url.lower() for keyword in contact_keywords)
        ]

        filtered_links.append(str(response.url))

        if filtered_links:
            first_link = filtered_links.pop(0)
            yield SeleniumRequest(
                url=first_link,
                wait_time=5,
                screenshot=True,
                callback=self.parse_links,
                dont_filter=True,
                meta={"links": filtered_links}
            )

    def parse_links(self, response):
        links = response.meta.get("links", [])

        excluded_domains = ["facebook", "instagram",
                            "youtube", "twitter", "wiki", "linkedin"]

        if not any(domain in response.url.lower() for domain in excluded_domains):
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            emails = re.findall(email_pattern, response.text)
            self.uniqueEmail.update(emails)

        if links:
            next_link = links.pop(0)
            yield SeleniumRequest(
                url=next_link,
                callback=self.parse_links,
                dont_filter=True,
                meta={"links": links}
            )
        else:
            yield SeleniumRequest(
                url=response.url,
                callback=self.finalize,
                dont_filter=True
            )

    def finalize(self, response):
        valid_domains = [".in", ".com", ".org", ".edu", ".net", ".np"]
        final_emails = [
            email for email in self.uniqueEmail
            if any(domain in email.lower() for domain in valid_domains)
        ]

        print("\n" + "="*50)
        print("Email Scraping Complete!")
        print(f"Found {len(final_emails)} valid emails:")
        for email in sorted(final_emails):
            print(f"  - {email}")
        print("="*50 + "\n")
