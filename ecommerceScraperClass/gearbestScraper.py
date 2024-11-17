from ecommerceScraperClass.ecommerceScraper import EcommerceScraper

class GearBestScraper(EcommerceScraper):
    def __init__(self):
        super().__init__(space_replacement="+")
        self.website_name = "gearbest.ma"
        self.search_url_template="https://www.gearbest.ma/?s={keyword}&post_type=product&product_cat="
        self.title_selector = ".flowhidden.mb10.fontnormal.position-relative"
        self.description_selector = ".flowhidden.mb10.fontnormal.position-relative"
        self.price_selector = ".woocs_price_code"
        self.link_selector = "h3.flowhidden.mb10.fontnormal.position-relative a"
        self.image_selector = "a.img-centered-flex.rh-flex-center-align.rh-flex-justify-center img"
        self.container_selector = ".info_in_dealgrid.flowhidden" 
        self.product_selector = ".columns-5.products.col_wrap_fifth.eq_grid.pt5.rh-flex-eq-height"
