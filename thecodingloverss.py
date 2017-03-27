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

        contributor = entry.summary_detail.value
        href = entry.links[0].href
        published = entry.published
        title = entry.title

        bs = BS(urllib2.urlopen(href), "lxml")
        image = bs.p.img.get('src')
        imgsrc='<img src="%s">' % image

        description = "%s <br/> %s" % (imgsrc, contributor)

        fe = fg.add_entry()

        fe.id(href)
        fe.link(href=href)
        fe.pubdate(published)
        fe.title(title)
        fe.description(description)

    rssfeed  = fg.rss_str(pretty=True)
    return rssfeed

