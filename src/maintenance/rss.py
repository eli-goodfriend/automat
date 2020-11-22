"""
Update a set of sound files based on an rss feed 
"""
import os
import urllib.request
import feedparser
import moviepy.editor


class RSSReader(object):
    # abc for keeping a directory updated from an RSS feed
    def __init__(self):
        self.feed_url = ''
        self.save_dir = ''
        self.end_format = 'ogg'

    def tmp_filename(self, entry):
        """
        combine the title and id to make a unique name for each file
        """
        filename = '{}_{}.mp4'.format(entry.title, entry.id)
        return os.path.join(self.save_dir, filename)

    def final_filename(self, tmp_name):
        """
        what the final, postprocessed file should be named
        """
        return tmp_name

    def get_file_src(self, entry):
        """
        pull the file URL from the RSS entry
        """
        return entry.links[0]['href']

    def postprocess(self, filename):
        """
        how to postprocess the file
        e.g. strip the audio from a video, convert audio to .ogg
        """
        return None

    def parse(self):
        """
        parse the RSS feed, downloading and postprocessing new files
        """
        # download any new files from the feed
        feed = feedparser.parse(self.feed_url)
        #for entry in feed.entries[1:]:
        for entry in feed.entries[1:3]:
            file_dst = self.tmp_filename(entry)
            file_src = self.get_file_src(entry)
            if not os.path.exists(self.final_filename(file_dst)):
                print("Downloading to {}...".format(file_dst))
                filename, headers = urllib.request.urlretrieve(file_src, file_dst)
                print("Postprocessing {}...".format(filename))
                self.postprocess(filename)


class TinyDesk(RSSReader):

    def __init__(self):
        super().__init__()
        self.feed_url = 'https://feeds.npr.org/510292/podcast.xml'
        self.save_dir = '/home/eli/Data/automat_data/tiny_desk'

    def final_filename(self, tmp_name):
        """
        replace mp4 extension with ogg
        """
        return '{}.{}'.format(os.path.splitext(tmp_name)[0], self.end_format)

    def postprocess(self, filename):
        """
        - convert mp4 video to ogg audio
        - delete mp4 video file, since it is big
        - ...? audio normalization?
        """
        # convert video to audio
        print("\tConvert video to audio...")
        video = moviepy.editor.VideoFileClip(filename)
        audio = video.audio
        audio.write_audiofile(self.final_filename(filename))
        # clean up original (big) video
        print("\tAudio saved at {}, removing video...".format(self.final_filename(filename)))
        os.remove(filename)


class Podcast99PI(RSSReader):

    def __init__(self):
        super().__init__()
        self.feed_url = 'http://feeds.99percentinvisible.org/99percentinvisible'
        self.save_dir = '/home/eli/Data/automat_data/podcast_99pi'

    def get_file_src(self, entry):
        """
        pull the file URL from the RSS entry
        """
        return entry.links[1]['href']

    def postprocess(self, filename):
        """
        TODO convert mp4 audio files to ogg audio files???????
        """
        return None


#TinyDesk().parse()
Podcast99PI().parse()
