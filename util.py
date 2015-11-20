import urllib, feedparser, re, sqlite3



#Functions for parsing and organizing feed data

#Takes a list of URLs and returns a list of raw feed objects [?index?: feed]
def getFeed(urls):

    feeds = [feedparser.parse(url) for url in urls] 

    return feeds

def parseFeed(feed):
    #Takes a feed and returns a list of custom MyFeed objects

    feedObj = MyFeed(feed["url"], feed["channel"]["title"], feed["channel"][ "description"], feed["items"])

    return feedObj

class MyFeed:
    'Base class for our feeds'
    feedCount=0

    def __init__(self, url, title, description, items):
        self.url=url
        self.title=title

        if(description):
            self.description=description
        else:
            self.description="NO DESCRIPTION AVAILABLE"

        self.items=[item for item in items]

        MyFeed.feedCount+=1

class MyArticle:
    'Base class for each article'
    articleCount=0

    def __init__(self, url, feed, title, date_parsed):
        self.url=url
        self.feed=feed
        self.title=title
        self.date_parsed=date_parsed
        MyArticle.articleCount+=1
