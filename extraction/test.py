from scraper import Scraper

scraper = Scraper()
home_url = 'http://books.toscrape.com/index.html'

category = scraper.get_list_category()

all_book = []
for cat in category:
    books = scraper.get_list_books(cat)
    for b in books:
        book = scraper.get_book(b)
        all_book.append(book)