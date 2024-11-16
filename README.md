# Keyword Search and Data Retrieval Project

## Project Overview

This project fetches product data from multiple eCommerce websites (like DHGate, Alibaba, AliExpress, etc.) based on user-input keywords from a Google Sheet. Additionally, it fetches YouTube video data related to those keywords and writes both eCommerce and YouTube data to separate Google Sheets. The project demonstrates skills in web scraping, API integration, and cloud services (Google Sheets API).

### Prerequisites

1. **Python 3.8+**: Ensure Python is installed on your system.
2. **Google Cloud Platform Account**: Create a project and enable the Google Sheets API and download the OAuth client json file then rename it to credentials.

3. **YouTube API Key**: Obtain an API key from the Google Developer Console for YouTube Data API access.

4. **Set Up Google Sheets:**

- Prepare three Google Sheets:
  1 - One for reading the list of keywords.
  2 - One for writing YouTube video data.
  3 - One for writing eCommerce product data.

4. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repository-url.git
   cd your-repository-folder
   ```

5. **Environment Setup**: Install the required Python packages using:
   -Create a Virtual Environment:

   ```bash
   python -m venv venv
   ```

   -Activate the Virtual Environment:

   ```bash
   venv\Scripts\activate
   ```

   -Create a .env file in the root directory and add your YouTube API Key:

   ```bash
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

   ```bash
      pip install -r requirements.txt
   ```

6. **Google Sheet Setup**:
   -create a config.py file and write inside your as follows:
   SPREADSHEET_ID_USER_INPUT = "your-user-input-spreadsheet-id"
   SPREADSHEET_ID_PRODUCT_DATA = "your-ecommerce-product-data-spreadsheet-id"
   SPREADSHEET_ID_MULTIMEDIA_CONTENT_DATA = "your-youtube-data-spreadsheet-id"

- Update the spreadsheet IDs and ranges in the code to match your Google Sheets.

```

```
