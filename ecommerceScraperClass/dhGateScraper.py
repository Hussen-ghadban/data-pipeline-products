from ecommerceScraperClass.ecommerceScraper import EcommerceScraper

class DHGateScraper(EcommerceScraper):
    def __init__(self):
        super().__init__(space_replacement="+")
        self.website_name = "dhgate.com"
        self.search_url_template = "https://www.dhgate.com/wholesale/search.do?act=search&searchkey={keyword}"
        self.title_selector = ".gallery-pro-name"
        self.description_selector = ".gallery-pro-name"
        self.price_selector = ".current-price"
        self.link_selector = ".gallery-img-link.gallery-a-img"
        self.image_selector = "div.LazyLoad.is-visible img"
        self.container_selector = ".gallery-main"
        self.product_selector = ".gallery-main"
