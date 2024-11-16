from playwright.sync_api import sync_playwright
from similarityScore import similarity_score

class AliBaba:
    def __init__(self):
        pass


    def fetch_data(self,keyword):
        search_url = f'https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.the-new-header_fy23_pc_search_bar.keydown__Enter&tab=all&SearchText={keyword.replace(" ", "+")}'
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context(
                locale='en-US',
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            )
            page = context.new_page()
            page.goto(search_url)
            page.wait_for_selector('.organic-list.app-organic-search-mb-20.viewtype-gallery')  # Outer container
            products = page.query_selector_all('.fy23-search-card.m-gallery-product-item-v2.J-search-card-wrapper.searchx-offer-item')[:1]  # Product selector

            product_data = []
            for product in products:
                title = product.query_selector('.search-card-e-title').inner_text().strip()
                description = title 
                price = product.query_selector('.search-card-e-price-main').inner_text().strip()
                link = 'https'+product.query_selector('.search-card-e-title a').get_attribute('href')
                score=similarity_score(keyword,title)

                product_data.append({
                    "Title": title,
                    "Description": description,
                    "Product Link": link,
                    "Price": price,
                    "Website Source": "alibaba.com",
                    "Similarity Score":score
                })

            browser.close()
            return product_data