from util import * 

#RSS Urls
rss_urls = ["http://feeds.bbci.co.uk/news/rss.xml?edition=int#"]

feeds = getFeed(rss_urls)

for feed in feeds:
    print feed

