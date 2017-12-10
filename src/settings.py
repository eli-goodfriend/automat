"""
classes that specify automated room settings
current task is to automate music, but other settings could be added, such as
color and intensity of light or turning on an aroma diffuser
"""
import os
import subprocess

import pygame

from src.util import Sound

class Setting(object):
    """
    abstract parent of all setting classes
    """
    def __init__(self, dir_name='', data_dir='/home/eli/Data/automat/'):
        # TODO being lazy about root data directory, should have a config file
        self.top_data_dir = data_dir
        self.data_dir = os.path.join(self.top_data_dir, dir_name)

        self.processes = []
        pygame.mixer.init()

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

class Rain(Setting):
    """
    play the sound of rain
    """
    def __init__(self, dir_name='rain'):
        Setting.__init__(self, dir_name=dir_name)

    def create(self):
        """
        just play the sound of rain, that's it
        """
        print "rain"
        sound_dir = os.path.join(self.data_dir, 'sound_files')
        Sound.play_sound_from_dir(sound_dir)

class Story(Setting):
    """
    play stories randomly selected from story/sound_files/ directories
    """
    def __init__(self, dir_name='story'):
        Setting.__init__(self, dir_name=dir_name)

        # TODO this should be in a config
        # possible additions:
        # - this american life
        # - the truth
        # - the moth
        self.ratios = {'librivox': 4,
                       'old_time_radio': 4,
                       'other_nightvale': 1,
                       'welcome_to_nightvale': 1}

    def create(self):
        """
        randomly play stories from various categories
        """
        print "story"
        sound_dir = os.path.join(self.data_dir, 'sound_files')
        Sound.play_sound_from_ratios(sound_dir, self.ratios)

class Facts(Setting):
    """
    play nonfiction audio randomly selected from facts/sound_files/ directories
    """
    def __init__(self, dir_name='facts'):
        Setting.__init__(self, dir_name=dir_name)

        # TODO this should be in a config (?)
        self.ratios = {'99_percent_invisible': 2,
                       'radiolab': 2,
                       'allusionist': 2,
                       'science_friday': 1,
                       'futility_closet': 2}

    def create(self):
        """
        randomly play nonfiction from various categories
        """
        print "facts"
        sound_dir = os.path.join(self.data_dir, 'sound_files')
        Sound.play_sound_from_ratios(sound_dir, self.ratios)
