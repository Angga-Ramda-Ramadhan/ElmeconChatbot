from scrapling.fetchers import Fetcher, FetcherSession
from scrapling.fetchers import StealthyFetcher, StealthySession

with StealthySession(headless=True, solve_cloudflare=True) as session:  # Keep the browser open until you finish
    page = session.fetch('https://www.electricautomationnetwork.com/en/omron/compact-square-photoelectric-sensor-omron-e3z-t81-5m-oms-241526', google_search=False)
    # data = page.css('#padded_content a').getall()
    print(page.html_content)
# # Or use one-off requests
# page = Fetcher.get('https://quotes.toscrape.com/')
# quotes = page.css('.quote .text::text').getall()