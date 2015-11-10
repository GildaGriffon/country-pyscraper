from util import * 

#RSS Urls
rss_urls = ["http://feeds.bbci.co.uk/news/rss.xml?edition=int#", "http://www.nytimes.com/services/xml/rss/nyt/InternationalHome.xml"]

feeds = getFeed(rss_urls)

feedObjs =  [parseFeed(feed) for feed in feeds]

for feedObj in feedObjs:
    print feedObj.title
    print feedObj.url
    print feedObj.description
