import feedparser, sys, urllib2

from bs4 import BeautifulSoup as BS
from feedgen.feed import FeedGenerator
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    d = feedparser.parse('http://thecodinglove.com/rss')

    fg = FeedGenerator()
    fg.title('The coding love with images.')
    fg.link(href='http://thecodinglove.com')
    fg.description('The coding love with images.')

    for entry in d.entries:

        title = entry.title

        href = entry.links[0].href
        bs = BS(urllib2.urlopen(href), "lxml")

        image = bs.p.img.get('src')
        imgsrc='<img src="%s">' % image

        fe = fg.add_entry()
        fe.id(href)
        fe.link(href=href)
        fe.title(title)
        fe.description(imgsrc)

    rssfeed  = fg.rss_str(pretty=True)
    return rssfeed

