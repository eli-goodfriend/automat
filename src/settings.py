"""
classes that specify automated room settings
current task is to automate music, but other settings could be added, such as
color and intensity of light or turning on an aroma diffuser
"""
import os
from random import shuffle
import subprocess

class Setting(object):
    """
    abstract parent of all setting classes
    """
    def __init__(self, data_dir='~/Data/automat/'):
        # TODO being lazy about root data directory, should have a config file
        self.top_data_dir = data_dir
        self.data_dir = data_dir # should be overwritten by child classes

        self.processes = []

    def play_music(self):
        """
        play all files in the sound_files directory
        currently assumes
        - everything in the directory is a sound file
        - the music is under a directory called sound_files
        """
        music_dir = os.path.join(self.data_dir, 'sound_files')
        all_files = os.listdir(music_dir)
        shuffle(all_files)
        music_cmd = all_files.insert(0, 'play')
        music_proc = subprocess.Popen(music_cmd, shell=True,
             stdin=None, stdout=None, stderr=None, close_fds=True)
        self.processes.append(music_proc)

    def create(self):
        """
        send signals to all room setting devices to implement setting
        """
        raise NotImplementedError('{} does not implement create()'
                                  .format(self.__class__.__name__))

    def destroy(self):
        """
        send signals to all room setting devices to shut down setting
        """
        raise NotImplementedError('{} does not implement destroy()'
                                  .format(self.__class__.__name__))

class DoNothing(Setting):
    """
    default class: turn everything off
    """

    def create(self):
        print "do nothing"

    def destroy(self):
        print "wasn't doing anything anyway"

class CodingWork(Setting):
    """
    settings to make the room suitable for coding work ;D
    """
    def __init__(self):
        Setting.__init__(self)
        self.data_dir = os.path.join(self.top_data_dir,'coding_work')

    def create(self):
        print "coding work"

    def destroy(self):
        print "not coding anymore"
