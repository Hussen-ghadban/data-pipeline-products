from playwright.sync_api import sync_playwright
from similarityScore import similarity_score

class EcommerceScraper:
    def __init__(self, space_replacement="-"):
        self.website_name = "Base Website"
        self.search_url_template = ""
        self.title_selector = ""
        self.description_selector = ""
        self.price_selector = ""
        self.link_selector = ""
        self.image_selector = ""
        self.space_replacement = space_replacement

    def fetch_data(self, keyword):
        try:
            formatted_keyword = keyword.replace(" ", self.space_replacement)
            search_url = self.search_url_template.format(keyword=formatted_keyword)
            product_data = []

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                context = browser.new_context(
                    locale='en-US',
                    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                )
                page = context.new_page()
                page.goto(search_url)
                
                # Wait for the container to load, specific for each child class
                page.wait_for_selector(self.container_selector)
                
                # Select the products
                products = page.query_selector_all(self.product_selector)[:10]

                for product in products:
                    title=product.query_selector(self.title_selector).inner_text().strip() if product.query_selector(self.title_selector) else "N/A"
                    description=product.query_selector(self.description_selector).inner_text().strip() if product.query_selector(self.description_selector) else "N/A"
                    price=product.query_selector(self.price_selector).inner_text().strip() if product.query_selector(self.price_selector) else "N/A"
                    link=product.query_selector(self.link_selector).get_attribute('href') if product.query_selector(self.link_selector) else "N/A"
                    image_element=product.query_selector(self.image_selector).get_attribute('src') if product.query_selector(self.image_selector) else "N/A"
                    if link != "N/A" and not link.startswith("https:"):
                        link="https:" + link
                    if image_element != "N/A" and not image_element.startswith("https:"):
                        image_element="https:" + image_element 
                        
                    # Compute similarity score
                    score = similarity_score(keyword, title)
                    
                    product_data.append({
                        "Title": title,
                        "Description": description,
                        "Product Link": link,
                        "Price": price,
                        "Website Source": self.website_name,
                        "Similarity Score": score,
                        "Image Url": image_element
                    })
                
                browser.close()
                return product_data
        except Exception as e:
            print(f"Failed to fetch data from {self.website_name} for '{keyword}': {e}")
