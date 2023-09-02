import requests
import json

def get_news(api_key, source):
    base_url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'sources': source
    }
    response = requests.get(base_url, params=params)

    if response.status_code ==200:
        newsData = json.loads(response.text)
        articles = newsData.get('articles')

        if articles:
            for index, article in enumerate(articles):
                print(f"Article Index: {index}")
                print(f"Title: {article['title']}")
                print(f"Author: {article['author']}")
                print(f"Description: {article['description']}")
                print(f"URL: {article['url']}")
                print("\n")
        else:
            print("No Articles")
    else:
        print("Failed to fetch Data")


if __name__ == "__main__":
    source = input("Enter a news source (e.g., cnn, bbc-news): ")
    get_news("786926035391432c9cecb97d91b4f1ee", source)
