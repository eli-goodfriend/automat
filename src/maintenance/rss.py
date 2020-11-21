"""
Update a set of sound files based on an rss feed 
"""
import feedparser

ex_feed = 'https://feeds.npr.org/510292/podcast.xml' # NPR tiny desk

feed = feedparser.parse(ex_feed)
print(feed.entries[2].keys())
print(feed.entries[2].title) # human readable name of the performance
print(feed.entries[1].id) # hopefully unique ID of the performance
print(feed.entries[2].links[0]['href']) # link to mp4 audio+video

