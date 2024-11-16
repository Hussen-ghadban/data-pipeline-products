from playwright.sync_api import sync_playwright
from similarityScore import similarity_score

class DHGateSearch:
    def __init__(self):
        pass

    def fetch_data(self, keyword):
        try:
            search_url = f'https://www.dhgate.com/wholesale/search.do?act=search&searchkey={keyword.replace(" ","+")}'
            product_data = []
            # launch the browser
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                context = browser.new_context(
                    locale='en-US',
                    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                )
                page = context.new_page()
                page.goto(search_url)
                # wait for the selector to load

                page.wait_for_selector('.gallery-main') # Outer container
                
                products = page.query_selector_all('.gallery-main')[:1] # Product selector
                
                for product in products:
                    title = product.query_selector('.gallery-pro-name').inner_text().strip() if product.query_selector('.gallery-pro-name') else "N/A"
                    description = title 
                    price = product.query_selector('.current-price').inner_text().strip() if product.query_selector('.current-price') else "N/A"
                    link = product.query_selector('.gallery-img-link.gallery-a-img').get_attribute('href') if product.query_selector('.gallery-img-link.gallery-a-img') else "N/A"
                    score=similarity_score(keyword,title)
                    image_element = "https:"+page.query_selector('div.LazyLoad.is-visible img').get_attribute('src')
                    product_data.append({
                        "Title": title,
                        "Description": description,
                        "Product Link": link,
                        "Price": price,
                        "Website Source": "dhgate.com",
                        "Similarity Score":score,
                        "Image Url":image_element


                    })

                browser.close()
                return product_data
        except Exception as e:
            print(f"Failed to fetch DHGate data for '{keyword}': {e}")