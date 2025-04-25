import scrapy

class OverleafSpider(scrapy.Spider):
    name = 'overleaf'
    start_urls = ['https://www.overleaf.com/gallery/tagged/cv']

    def parse(self, response):
        # Extracting links for each resume template
        for link in response.css('a::attr(href)').extract():
            if "/latex/templates/" in link:
                pdf_link = link + ".pdf"
                yield {'pdf_link': pdf_link}

        # Follow pagination links and scrape other pages
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
