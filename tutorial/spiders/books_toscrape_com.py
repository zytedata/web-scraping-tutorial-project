from scrapy import Spider


class BooksToScrapeComSpider(Spider):
    name = "books_toscrape_com"
    start_urls = [
        "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    ]

    def parse(self, response):
        next_page_links = response.css(".next a")
        yield from response.follow_all(next_page_links)
        book_links = response.css("article a")
        yield from response.follow_all(book_links, callback=self.parse_book)

    def parse_book(self, response):
        yield {
            "name": response.css("h1::text").get(),
            "price": response.css(".price_color::text").re_first("£(.*)"),
            "url": response.url,
        }
