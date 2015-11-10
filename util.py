import urllib
import feedparser

#Takes a list of URLs and returns a list of feeds [index: feed]
def getFeed(urls):

    #Aggregate feeds into a list
    feeds = [feedparser.parse(url) for url in urls] 

    for feed in feeds:
        print feed
       
    return feeds
