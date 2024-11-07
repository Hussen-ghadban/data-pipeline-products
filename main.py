from read_keyword import get_keywords_from_sheet
from youtube_data import search_youtube_videos
from write_videos_data_to_sheet import write_youtube_data_to_sheet
def main():
    keywords=get_keywords_from_sheet()
    all_videos=[]
    # for keyword in keywords:
    #     print(f"\nSearching YouTube for videos about: {keyword}")
    #     videos = search_youtube_videos(keyword) 
    for keyword in keywords:
        videos=search_youtube_videos(keyword)
        all_videos.extend(videos)
    write_youtube_data_to_sheet(all_videos)

        # for video in videos:
        #         print(f"Title: {video['title']}")
        #         print(f"Channel: {video['channel']}")
        #         print(f"Video Link: {video['video_link']}")
        #         # print(f"Description: {video['description']}")
        #         print(f"Views: {video['views']}")
        #         print(f"Likes: {video['likes']}")
        #         print(f"Publish Date: {video['publish_date']}")
        #         print("-----")
    # print(videos)

if __name__=='__main__':
    main()