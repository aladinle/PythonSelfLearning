# Scrape website titles with requests + BeautifulSoup.

import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    try:
        # send HTTP GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract title tag
    title = soup.title.string.strip() if soup.title else "No title found!"

    print(f"{url} => {title}\n")

    # # Extract all links
    # for link in soup.find_all('a'):
    #     print(link.get('href'))

    # # Extract all images
    # for link in soup.find_all('img'):
    #     print(link.get('src'))

    # Find Meta Information (description, keywords)
    # for meta in soup.find_all('meta'):
    #   print(meta.get('name'), ":", meta.get('content'))

    # # Find Paragraph Texts
    # for p in soup.find_all('p'):
    #     print(p.text.strip())

    # # Find all specific Element by ID or Class
    # # Find by Id
    # soup.find(id="main-content")

    # # Find by Class
    # soup.find_all(class_="product-title")

    # # Find all Tables
    # for row in soup.find_all('tr'):
    #     cells = [cell.text.strip() for cell in row.find_all(['td','th'])]
    #     print(cells)

    
    # # Scripts or JSON Data Embedded
    # for script in soup.find_all('script'):
    #     if 'application/ld+json' in str(script):
    #         print(script.string)

    # # Find all heading h1, h2, h3
    # for heading in soup.find_all(['h1', 'h2', 'h3']):
    #     print(heading.name, ":", heading.text.strip()) 

    # # <span class="price">$19.99</span>
    # price = soup.find('span', class_='price').text.strip()
    # print(price)

if __name__ == "__main__":
    # List of website to scrape
    websites = [
        "https://www.python.org",
        "https://www.youtube.com/",
        "https://www.github.com"
    ]
    for url in websites:
        scrape_headlines(url)