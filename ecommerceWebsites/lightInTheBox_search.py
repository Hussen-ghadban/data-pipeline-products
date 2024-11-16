from playwright.sync_api import sync_playwright
from similarityScore import similarity_score

class LightInTheBox:
    def __init__(self):
        pass

    def fetch_data(self,keyword):
        search_url = f'https://www.lightinthebox.com/search?q={keyword.replace(" ","+")}'
        product_data = []
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                locale='en-US',
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            )
            page = context.new_page()
            page.goto(search_url)
            page.wait_for_selector('.clearfix.prod-list-container.has-favorite.ctr-track-show-scroll-list')  # Outer container
            products = page.query_selector_all('.widget.prod_item-2020.ctr-track-list.show_similar.hasReport')[:1]  # Product selector

            for product in products:
                title = product.query_selector('.prod-name').inner_text().strip()
                description = product.query_selector('.prod-name').inner_text().strip()
                price = product.query_selector('.price-wrap-upgrade .price').inner_text().strip()

                link=product.get_attribute('href')
                score=similarity_score(keyword,title)

                product_data.append({
                    "Title": title,
                    "Description": description,
                    "Product Link": link,
                    "Price": price,
                    "Website Source": "lightinthebox.com",
                    "Similarity Score":score
                })

            browser.close()
            return product_data