import requests

class Scraper:
    def __init__(self):
        pass

    def get_list_category(self,home_url):
        xpath = '//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul'
        pass

    def pagination(self,category_url):
        xpath_number_book = '//*[@id="default"]/div/div/div/div/form/strong'
        number_book = 10
        number_page = int(number_book / 20)
        page = 'page-2.html'
        pass

    def get_list_books(self,category_url):
        xpath = '//*[@id="default"]/div/div/div/div/section/div[2]/ol'
        pass

    def get_book(self,book_url):
        html = 'html'
        book = {
            "name": self._get_name(html),
            "price": self._get_price(html),
            "stok": self._get_stok(html),
            "available": self._get_available(html),
            "image": self._get_image(html),
            "raiting": self._get_raiting(html),
            "category": self._get_category(html)
        }
        pass

    def _get_name(self,html):
        xpath = '//*[@id="content_inner"]/article/div[1]/div[2]/h1'
        pass

    def _get_price(self,html):
        xpath = '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]'
        pass

    def _get_stok(self,html):
        xpath = '//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()'
        pass

    def _get_available(self,html):
        xpath = '//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()'
        pass

    def _get_image(self,html):
        xpath = '//*[@id="product_gallery"]/div/div/div/img'
        pass

    def _get_raiting(self,html):
        xpath = '//*[@id="content_inner"]/article/div[1]/div[2]/p[3]'
        pass

    def _get_category(self,html):
        xpath = '//*[@id="default"]/div/div/ul/li[3]/a'
        pass
    