import config
from GoogleSheetReader import GoogleSheetReader
from EcommerceSearch import EcommerceSearch
from youtube_data import YouTubeSearch
from authenticate import GoogleSheetAuthenticator
from write_data_to_sheet import GoogleSheetWriter
def main():
    authenticator = GoogleSheetAuthenticator()

    spread_sheet_id=config.SPREADSHEET_ID_USER_INPUT
    sheet_handler=GoogleSheetReader(spread_sheet_id,authenticator)
    data = sheet_handler.get_keywords_from_sheet()
    print(data)
    aliexpress_search = EcommerceSearch(
    site_name="aliexpress.com",
    search_url_template="https://www.aliexpress.com/w/wholesale-{keyword}.html",
    product_selector='.list--gallery--C2f2tvm',
    title_selector='.multi--titleText--nXeOvyr',
    price_selector='.multi--price-sale--U-S0jtj',
    link_selector='.multi--container--1UZxxHY'
    )
    dhgate_search = EcommerceSearch(
    site_name="dhgate.com",
    search_url_template="https://www.dhgate.com/wholesale/search.do?act=search&searchkey={keyword}",
    product_selector='.gallery-main',
    title_selector='.gallery-pro-name',
    price_selector='.current-price',
    link_selector='.gallery-img-link.gallery-a-img'
    )
    lightinthebox_search = EcommerceSearch(
    site_name="lightinthebox.com",
    search_url_template="https://www.lightinthebox.com/search?q={keyword}",
    product_selector='.ctr-track-list',
    title_selector='.prod-name',
    price_selector='.price-wrap-upgrade .price',
    link_selector='.widget.prod_item-2020.ctr-track-list.show_similar.hasReport'
    )
    ecommerce_results=[]
    # youtube_Result=[]
    # youtube_writer = GoogleSheetWriter(config.SPREADSHEET_ID_MULTIMEDIA_CONTENT_DATA, 'multimedia!A1', authenticator)
    # youtube_headers = ["Title", "Channel", "Video Link", "Description", "Views", "Likes", "Publish Date"]
    
    ecommerce_writer = GoogleSheetWriter(config.SPREADSHEET_ID_PRODUCT_DATA, 'productData!A1', authenticator)
    ecommerce_headers = ["Title", "Description", "Product Link", "Price", "Website Source"]
    # youtube_search = YouTubeSearch()

    for d in data:
        # lightinthebox_result=lightinthebox_search.fetch_data(d[0])
        # ecommerce_results.extend(lightinthebox_result)
        aliexpress_result=aliexpress_search.fetch_data(d[0])
        ecommerce_results.extend(aliexpress_result)
        # youtube_results = youtube_search.search_videos(d[0])
        # youtube_Result.extend(youtube_results)

    # youtube_results = youtube_search.search_youtube_videos("jacket or men")
    # youtube_writer.write_data_to_sheet(youtube_results, youtube_headers)
    
    ecommerce_writer.write_data_to_sheet(ecommerce_results, ecommerce_headers)
    # print(youtube_results)
if __name__=='__main__':
    main()