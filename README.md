# Keyword Search and Data Retrieval Project

## Project Overview

This project fetches product data from multiple eCommerce websites (like DHGate, Gearbest, AliExpress) based on user-input keywords from a Google Sheet. Additionally, it fetches YouTube video data related to those keywords and writes both eCommerce and YouTube data to separate Google Sheets. The project demonstrates skills in web scraping, API integration, and cloud services (Google Sheets API).

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
   git clone https://github.com/Hussen-ghadban/data-pipeline-products.git
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

   -Install the required packges:

   ```bash
      pip install -r requirements.txt
   ```

6. **Google Sheet Setup**:
   -create a config.py file and write inside your as follows:
   ```bash
   SPREADSHEET_ID_USER_INPUT = "your-user-input-spreadsheet-id"
   SPREADSHEET_ID_PRODUCT_DATA = "your-ecommerce-product-data-spreadsheet-id"
   SPREADSHEET_ID_MULTIMEDIA_CONTENT_DATA = "your-youtube-data-spreadsheet-id"
   ```

- Update the spreadsheet IDs and ranges in the code to match your Google Sheets.

7. **Run The Project**:

```bash
python main.py
```

8. **Challenges Faced in the Project:**
   - One of the biggest challenges I encountered was with web scraping. The web scraping code would sometimes work perfectly when running the script individually, but it would intermittently fail when the same code was called within the main project script. This inconsistency made debugging particularly challenging. The issue required careful handling of exceptions, retries, and adjustments in the web scraping logic to ensure reliable performance.
   - When i create the token based on credentials file it would be in a form that will ask me to login every time i use google sheets API service, so i reformatted it so i only need to login once.
   - For fetching from youtube API i ahd to search for on how to fetch it and edit to fit my needs in the project.
   - Instead of creating a separate class for each ecommerce website, an ecommerceScraper class was developed to handle multiple websites, based on recognizing that the core scraping logic is similar across websites, and the differences lie mainly in selectors and URL patterns.
