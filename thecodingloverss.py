import datetime
import pytz
from feedgen.feed import FeedGenerator
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    thecodingloveurl = "http://thecodinglove.com/rss"
    pubdate = datetime.datetime(2017, 8, 7, 21, 0, 0, 0, pytz.UTC)

    fg = FeedGenerator()
    fg.title('The coding love with images.')
    fg.link(href=thecodingloveurl)
    fg.description('The coding love with images.')

    fe = fg.add_entry()
    fe.id("Life is good.")
    fe.link(href=thecodingloveurl)
    fe.title("The original coding love now has images!")
    fe.pubdate(pubdate)

    rssfeed  = fg.rss_str(pretty=True)

    return rssfeed

if __name__ == "__main__":
    app.run(host='0.0.0.0')

