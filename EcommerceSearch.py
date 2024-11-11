from playwright.sync_api import sync_playwright

class EcommerceSearch:
    def __init__(self, site_name, search_url_template, product_selector, title_selector, price_selector, link_selector, description_selector=None):

        self.site_name=site_name
        self.search_url_template=search_url_template
        self.product_selector=product_selector
        self.title_selector=title_selector
        self.price_selector=price_selector
        self.link_selector=link_selector
        self.description_selector=description_selector or title_selector 

    def fetch_data(self, keyword):
        search_url=self.search_url_template.format(keyword=keyword.replace(" ", "-"))
        product_data=[]
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True)
            context=browser.new_context(locale='en-US', user_agent='Mozilla/5.0')
            page=context.new_page()
            page.goto(search_url)
            page.wait_for_selector(self.product_selector)
            products=page.query_selector_all(self.product_selector)[:1]
            for product in products:
                title=product.query_selector(self.title_selector).inner_text().strip() if product.query_selector(self.title_selector) else "N/A"
                description=product.query_selector(self.description_selector).inner_text().strip() if product.query_selector(self.description_selector) else "N/A"
                price=product.query_selector(self.price_selector).inner_text().strip() if product.query_selector(self.price_selector) else "N/A"
                page.wait_for_selector(self.link_selector)
                product_link=product.query_selector(self.link_selector).get_attribute('href')
                link=page.evaluate('(element) => element.href', product_link) if product_link else "N/A"

                full_link=link if link.startswith("http") else f"https:{link}"
                product_data.append({
                    "Title": title,
                    "Description": description,
                    "Product Link": link,
                    "Price": price,
                    "Website Source": self.site_name
                })

            browser.close()

        return product_data
