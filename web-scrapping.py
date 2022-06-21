from time import sleep
from requests_html import HTMLSession
session = HTMLSession()
url= 'https://annapurnapost.com/tags/corona-virus'

r=session.get(url)

r.html.render(sleep=1, scrolldown=5)
articles = r.html.find('div')

newsList = []
for item in articles:
    try:
        news_items = item.find('h1', first=True)

        dict_article = {
        'title': news_items.text,
        'link' : news_items.absolute_links,
        }
        newsList.append(dict_article)

    except:
        pass
print(newsList[0])