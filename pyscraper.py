from util import * 

#RSS Urls
rss_urls_file = open('rssurls.txt', 'r')
rss_urls = rss_urls_file.readlines() 

feeds = getFeed(rss_urls)

feedObjs =  [parseFeed(feed) for feed in feeds]

#Display root feed info, place news into separate objects
articles = list()
for feedObj in feedObjs:
    #Print the feed's information
    #print feedObj.title
    #print feedObj.url
    #print feedObj.description
    #Add the articles to a list of total articles
    for item in feedObj.items:
        articles.append(MyArticle(item["link"], feedObj.title, item["title"], item["published_parsed"]))


#Display each article title, these will be interpreted
for article in articles:
    print article.title
