"""
utilities for interfacing with room controls
"""
import os
from random import shuffle

import pygame

class Sound(object):
    """
    utilities for playing sounds
    """
    @staticmethod
    def play_sound_from_dir(sound_dir):
        """
        play all files in sound_dir
        currently assumes
        - everything in the directory is a sound file
        """
        all_files = os.listdir(sound_dir)
        all_files = [os.path.join(sound_dir, filename) for filename in all_files]
        shuffle(all_files)
        for filename in all_files:
            pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)
