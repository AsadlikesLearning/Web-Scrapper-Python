import requests
from bs4 import BeautifulSoup
import csv


def scrape_book_titles(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h3')
        return [title.a['title'] for title in titles]
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return []


def save_to_csv(titles, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Index', 'Title'])  # Write header
        for index, title in enumerate(titles, 1):
            writer.writerow([index, title])
    print(f"Results saved to {filename}")


if __name__ == "__main__":
    url = "http://books.toscrape.com/"
    book_titles = scrape_book_titles(url)

    if book_titles:
        print("Books available:\n")
        for i, title in enumerate(book_titles, 1):
            print(f"{i}. {title}")

        # Save results to CSV
        csv_filename = "book_titles.csv"
        save_to_csv(book_titles, csv_filename)
    else:
        print("No titles were found or there was an error.")
