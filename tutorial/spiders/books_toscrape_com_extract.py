from scrapy import Spider


class BooksToScrapeComExtractSpider(Spider):
    name = "books_toscrape_com_extract"
    start_urls = [
        "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    ]

    def parse(self, response):
        next_page_links = response.css(".next a")
        yield from response.follow_all(next_page_links)
        book_links = response.css("article a")
        for request in response.follow_all(book_links, callback=self.parse_book):
            request.meta["zyte_api_automap"] = {"product": True}
            yield request

    def parse_book(self, response):
        yield response.raw_api_response["product"]
