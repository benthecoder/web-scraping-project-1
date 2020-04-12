from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.learndatasci.com/free-data-science-books/').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['book_name', 'author_year', 'summary', 'link'])


for article in soup.find_all('div', class_='col-lg-6'):
    book_name = article.h2.text
    print(book_name)

    author_year = article.span.text
    print(author_year)

    try:
        summary = article.p.text
        link = article.find('a', class_='btn')['href']

    except Exception as e:
        summary = None
        link = None

    print(summary)
    print(link)

    print()

    csv_writer.writerow([book_name, author_year, summary, link])

csv_file.close()
