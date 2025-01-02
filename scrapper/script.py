import requests
from bs4 import BeautifulSoup
from scrapper.models import News

def scraper_imdb_news():
    url = "https://www.imdb.com/news/movie/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("Request successful!")
            soup = BeautifulSoup(response.text, 'html.parser')
            news_items = soup.find_all('div', class_='ipc-list-card--border-line')

            for item in news_items:
                # Extract title, description, image, and external link
                title = item.find('a', class_="ipc-link ipc-link--base sc-ed7ef9a2-3 eDjiRr")
                description = item.find('div', class_="ipc-html-content-inner-div")
                image = item.find('img', class_="ipc-image")

                title_text = title.text.strip() if title else None
                description_text = description.text.strip() if description else None
                image_url = image['src'] if image else None
                external_link = title['href'] if title and 'href' in title.attrs else "https://www.imdb.com/news/"

                # Print extracted data for debugging
                print(f"Title: {title_text}, Description: {description_text}, Image URL: {image_url}, External Link: {external_link}")

                # Skip incomplete news items
                if not (title_text and description_text and external_link):
                    print("Incomplete data, skipping...")
                    continue

                # Avoid duplicates
                if News.objects.filter(external_link=external_link).exists():
                    print("Duplicate news item, skipping...")
                    continue

                # Create a news record
                news = {
                    "title": title_text,
                    "description": description_text,
                    "image": image_url,
                    "external_link": external_link
                }
                print(news)
                News.objects.create(**news)
                print(news)
                print("News item saved successfully!")

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"Error occurred during scraping: {e}")
