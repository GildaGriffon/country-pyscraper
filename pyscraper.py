from util import * 

#RSS Urls
rss_urls = ["http://feeds.bbci.co.uk/news/world/rss.xml#", "http://www.nytimes.com/services/xml/rss/nyt/InternationalHome.xml"]

feeds = getFeed(rss_urls)

feedObjs =  [parseFeed(feed) for feed in feeds]

#Display root feed info, place news into separate objects
for feedObj in feedObjs:
    print feedObj.title
    print feedObj.url
    print feedObj.description
    articles = [MyArticle(item["link"], item["title"], item["published_parsed"]) for item in feedObj.items]

#Display each article title, these will be interpreted
for article in articles:
    print article.title
