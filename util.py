import urllib
import feedparser
#Contains functions for parsing and organizing feed data

#Takes a list of URLs and returns a list of raw feed objects [?index?: feed]
def getFeed(urls):

    feeds = [feedparser.parse(url) for url in urls] 

    return feeds


def parseFeed(feed):
    #Takes a feed and returns a list of custom MyFeed objects

    feedObj = MyFeed(feed["url"], feed["channel"]["title"], feed["channel"][ "description"])

    return feedObj


class MyFeed:
    'Base class for our feeds'
    feedCount=0

    def __init__(self, url, title, description):
        self.url=url
        self.title=title

        if(description):
            self.description=description
        else:
            self.description="NO DESCRIPTION AVAILABLE"

        MyFeed.feedCount+=1
