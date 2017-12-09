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
        print "rain"
        sound_dir = os.path.join(self.data_dir, 'sound_files')
        Sound.play_sound_from_dir(sound_dir)
