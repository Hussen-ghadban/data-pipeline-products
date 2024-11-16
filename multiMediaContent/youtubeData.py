import os
from googleapiclient.discovery import build
from dotenv import load_dotenv
# load the environment variable
load_dotenv()

class YouTubeSearch:
    def __init__(self):
        #get the youtube API key from .env 
        self.api_key=os.getenv("YOUTUBE_API_KEY")
        #create a youtube data API v3 service object
        self.youtube=build('youtube','v3',developerKey=self.api_key)
        
    def search_youtube_videos(self, keyword):
        # make a request to youtube API
        search_response = self.youtube.search().list(
            q=keyword,       # the search keyword
            part='snippet',  # retrieve snippets data
            type='video',    # search only for videos
            maxResults=10    # limit the number of results to 10
        ).execute()
        videos_data=[]
        # extract videos IDs 
        video_ids=[item['id']['videoId'] for item in search_response['items']]
        # join the vidoe IDs into a string separated with comma
        video_ids_str=','.join(video_ids)
        # make antoher request to get detailed video data by IDs
        video_response=self.youtube.videos().list(  
            part='snippet,statistics',
            id=video_ids_str             # specify the video ID to retrieve data for
        ).execute()

        for item in video_response['items']:
            #create a dictionary with detailed information for videos
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