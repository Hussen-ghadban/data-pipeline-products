import config
from googlesheet.googleSheetReader import GoogleSheetReader

from multiMediaContent.youtubeData import YouTubeSearch
from authenticate import GoogleSheetAuthenticator
from googlesheet.googleSheetWriter import GoogleSheetWriter
from ecommerceScraperClass.aliexpressScraper import AliExpressScraper
from ecommerceScraperClass.gearbestScraper import GearBestScraper
from ecommerceScraperClass.dhGateScraper import DHGateScraper

def main():
    # Authenticate access to google sheets API
    authenticator = GoogleSheetAuthenticator() 

    spread_sheet_id=config.SPREADSHEET_ID_USER_INPUT
    sheet_handler=GoogleSheetReader(spread_sheet_id,authenticator)
    # Retrieve keywords from first google sheet
    keywords = sheet_handler.get_keywords_from_sheet()
    print(keywords)


    aliexpress_search=AliExpressScraper()
    dhgate_search=DHGateScraper()
    gear_search=GearBestScraper()

    ecommerce_results=[]
    youtube_results=[]

    dhgate_results=[]
    aliexpress_results=[]
    gearbest_results=[]
    # Initializing google wheets writers to store the results for multimedia content data
    youtube_writer = GoogleSheetWriter(config.SPREADSHEET_ID_MULTIMEDIA_CONTENT_DATA, 'multimedia!A1', authenticator)
    youtube_headers = ["Title", "Channel", "Video Link", "Description", "Views", "Likes", "Publish Date"]

    # Initializing google wheets writers to store the results for ecommerce websites data
    ecommerce_writer = GoogleSheetWriter(config.SPREADSHEET_ID_PRODUCT_DATA, 'productData!A1', authenticator)
    ecommerce_headers = ["Title", "Description", "Product Link", "Price", "Website Source","Similarity Score","Image Url"]
    
    #Initializing search classes for ecommerce websites and youtube
    youtube_search = YouTubeSearch()

    # fetching the data
    for keyword in keywords:
        try:
            dhgate=dhgate_search.fetch_data(keyword[0])
            dhgate_results+=dhgate
        except Exception as e:
            print(f"Failed to fetch DHGate data for '{keyword}': {e}")

        try:
            gearbest = gear_search.fetch_data(keyword[0]) 
            gearbest_results+=gearbest
        except Exception as e:
            print(f"Failed to fetch GearBest data for '{keyword}': {e}")
 
        try:
            aliexpress = aliexpress_search.fetch_data(keyword[0]) 
            aliexpress_results+=aliexpress
        except Exception as e:
            print(f"Failed to fetch AliExpress data for '{keyword}': {e}")

        try:
            youtube = youtube_search.search_youtube_videos(keyword[0])
            youtube_results+=youtube
        except Exception as e:
            print(f"Failed to fetch YouTube data for '{keyword}': {e}")
            
    # writing youtube results to multimedia googlesheet
    youtube_writer.write_data_to_sheet(youtube_results, youtube_headers)

    ecommerce_results=dhgate_results+aliexpress_results+gearbest_results
    print(ecommerce_results)
    # writing youtube results to ecommerce webistes googlesheet
    ecommerce_writer.write_data_to_sheet(ecommerce_results, ecommerce_headers)

    print("Cells Updated")
if __name__=='__main__':
    main()