import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

def search_youtube_videos(keyword):
    api_key=os.getenv("YOUTUBE_API_KEY")
    youtube=build('youtube','v3',developerKey=api_key)
    search_response = youtube.search().list(
        q=keyword,
        part='snippet',
        type='video', 
        maxResults=10 
    ).execute()
    videos_data=[]

    video_ids=[item['id']['videoId'] for item in search_response['items']]
    video_ids_str=','.join(video_ids)
    video_response=youtube.videos().list(
        part='snippet,statistics',
        id=video_ids_str
    ).execute()

    for item in video_response['items']:
        video_info = {
            'title':item['snippet']['title'],
            'channel':item['snippet']['channelTitle'],
            'description':item['snippet']['description'],
            'video_link':f"https://www.youtube.com/watch?v:{item['id']}",
            'views':item['statistics'].get('viewCount','N/A'),
            'likes':item['statistics'].get('likeCount','N/A'),
            'publish_date':item['snippet']['publishedAt']
            }
        videos_data.append(video_info)
    return videos_data