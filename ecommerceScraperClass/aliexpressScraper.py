from ecommerceScraperClass.ecommerceScraper import EcommerceScraper

class AliExpressScraper(EcommerceScraper):
    def __init__(self):
        super().__init__(space_replacement="-")
        self.website_name = "aliExpress.com"
        self.search_url_template = "https://www.aliexpress.com/wholesale?SearchText={keyword}"
        self.title_selector = ".multi--titleText--nXeOvyr"
        self.description_selector = ".multi--titleText--nXeOvyr"
        self.price_selector = ".multi--price-sale--U-S0jtj"
        self.link_selector = ".multi--container--1UZxxHY"
        self.image_selector = "img.images--item--3XZa6xf"
        self.container_selector = ".list--galleryWrapper--29HRJT4"
        self.product_selector = ".list--gallery--C2f2tvm" 