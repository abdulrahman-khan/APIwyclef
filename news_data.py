import requests
from dotenv import load_dotenv
import os
import json

# gets the news data
def get_news_data():
    if response.status_code == 200:
        data = response.json()
        # print(data)
        with open("news_data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        return data
    else:
        return None

# loops and prints article data
def print_articles(data):
    articles = data.get('articles', [])

    for index, article in enumerate(articles[:3], start=1):
        print(f"Article Number {index}--------------------------- \n {json.dumps(article, sort_keys=True, indent=4)}\n")






load_dotenv()
KEY = os.getenv("NEWS_API_KEY")



url = f"https://newsapi.org/v2/top-headlines"
# Parameters for the API request
params = {
    "country": "us",
    "apiKey": KEY
}


response = requests.get(url, params=params)

data = get_news_data()

if data is not None:
    print_articles(data)






# # Headers (if needed)
# headers = {
#     "Authorization": "Bearer YOUR_API_KEY",
#     "Content-Type": "application/json"
# }

# # Make a GET request
# response = requests.get(url, headers=headers)

# # Check the response status
# if response.status_code == 200:
#     print("Response Data:", response.json())
# else:
#     print(f"Failed to fetch data. Status Code: {response.status_code}, Error: {response.text}")