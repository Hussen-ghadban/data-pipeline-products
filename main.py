from read_keyword import get_keywords_from_sheet
from youtube_data import search_youtube_videos
from write_videos_data_to_sheet import write_youtube_data_to_sheet
from aliexpress_data import fetch_aliexpress
from write_aliexpress_data import write_aliexpress_data_to_sheet
def main():
    keywords=get_keywords_from_sheet()
    all_videos=[]
    all_aliexpress=[]
    for keyword in keywords:
        videos=search_youtube_videos(keyword)
        all_videos.extend(videos)
        aliexpress_data=fetch_aliexpress(keyword)
        all_aliexpress.extend(aliexpress_data)
    write_youtube_data_to_sheet(all_videos)
    write_aliexpress_data_to_sheet(all_aliexpress)
if __name__=='__main__':
    main()