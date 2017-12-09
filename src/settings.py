"""
classes that specify automated room settings
current task is to automate music, but other settings could be added, such as
color and intensity of light or turning on an aroma diffuser
"""
import os
from random import shuffle
import subprocess

import pygame

class Setting(object):
    """
    abstract parent of all setting classes
    """
    def __init__(self, data_dir='/home/eli/Data/automat/'):
        # TODO being lazy about root data directory, should have a config file
        self.top_data_dir = data_dir
        self.data_dir = data_dir # should be overwritten by child classes

        self.processes = []
        pygame.mixer.init()

    def play_music(self):
        """
        play all files in the sound_files directory
        currently assumes
        - everything in the directory is a sound file
        - the music is under a directory called sound_files
        """
        music_dir = os.path.join(self.data_dir, 'sound_files')
        all_files = os.listdir(music_dir)
        all_files = [os.path.join(music_dir, filename) for filename in all_files]
        shuffle(all_files)
        for filename in all_files:
            pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)

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
        pygame.mixer.quit()
        exit_code = [proc.terminate() for proc in self.processes]

class DoNothing(Setting):
    """
    default class: don't do anything
    """

    def create(self):
        print "do nothing"

class CodingWork(Setting):
    """
    settings to make the room suitable for coding work :P
    """
    def __init__(self):
        Setting.__init__(self)
        self.data_dir = os.path.join(self.top_data_dir,'coding_work')

    def create(self):
        print "coding work"
        self.play_music()
