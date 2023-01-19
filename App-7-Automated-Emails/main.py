# API KEY 95e78f42ecf84a268573ff67d8910db9
import requests
from pprint import pprint


class NewsFeed:
    """ Representing multiple news title and links as a single string"""

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "95e78f42ecf84a268573ff67d8910db9"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()
        # class ExcelFile:
        # response = requests.get("https://newsapi.org/v2/everything?q=bitcoin&apiKey=95e78f42ecf84a268573ff67d8910db9")
        # Get the new from 2022-12-31 to 2023-01-19

        # response = requests.get("https://newsapi.org/v2/everything?qInTitle=bitcoin&apiKey=95e78f42ecf84a268573ff67d8910db9")
        # content = response.text
        # print(content)
        # pprint(content)
        articles = self._get_articles(url)

        email_body = ''
        # pprint(content)
        # print(x)
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
            # print(article['title'], article['url'])
        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key} "
        return url


if __name__ == "__main__":
    news_feed = NewsFeed(interest='nasa', from_date='2022-12-31', to_date='2023-01-13', language='en')
    print(news_feed.get())
