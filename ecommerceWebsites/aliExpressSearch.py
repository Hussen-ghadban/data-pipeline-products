from playwright.sync_api import sync_playwright
from similarityScore import similarity_score

class AliExpress:
    def __init__(self):
        pass
    def fetch_data(self,keyword):
        search_url = f'https://www.aliexpress.com/w/wholesale-{keyword.replace(" ","-")}.html'
        product_data = []
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                locale='en-US',
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            )
            page = context.new_page()
            page.goto(search_url)
            page.wait_for_selector('.list--galleryWrapper--29HRJT4')  # Outer container
            products = page.query_selector_all('.list--gallery--C2f2tvm')[:1]  # Product selector

            for product in products:
                title = product.query_selector('.multi--titleText--nXeOvyr').inner_text().strip()
                description = product.query_selector('.multi--titleText--nXeOvyr').inner_text().strip()
                price = product.query_selector('.multi--price-sale--U-S0jtj').inner_text().strip()
                link = "https:" + product.query_selector('.multi--container--1UZxxHY').get_attribute('href')
                score=similarity_score(keyword,title)

                product_data.append({
                    "Title": title,
                    "Description": description,
                    "Product Link": link,
                    "Price": price,
                    "Similarity Score":score,
                    "Website Source": "aliexpress.com"
                })

            browser.close()
            return product_data