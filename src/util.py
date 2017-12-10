"""
utilities for interfacing with room controls
"""
import os
from random import shuffle, sample

import pygame

class Sound(object):
    """
    utilities for playing sounds
    """
    @staticmethod
    def play_sound_from_dir(sound_dir):
        """
        play all files in sound_dir on loop
        assumes everything in the directory is a sound file
        """
        all_files = os.listdir(sound_dir)
        all_files = [os.path.join(sound_dir, filename) for filename in all_files]
        shuffle(all_files)
        for filename in all_files:
            pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)

    @staticmethod
    def play_sound_from_file(sound_file):
        """
        play one sound file
        assumes everything in the directory is a sound file
        """
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play(0)

    @staticmethod
    def play_sound_from_ratios(sound_dir, ratios, queue_factor=10):
        """
        generate a queue of files from subdirs of sound_dir, with ratios between files drawn
        from the different subdirs drawn from ratios

        ratios = {'subdir1': 1,
                  'subdir2': 3}
        to get 3x more files from subdir2 than subdir1

        assumes everything in the subdirs are sound files
        """
        file_list = []
        for key in ratios.keys():
            subdir = os.path.join(sound_dir, key)
            all_files = os.listdir(subdir)
            all_files = [os.path.join(subdir, filename) for filename in all_files]

            num_to_draw = ratios[key]*queue_factor
            try:
                to_play = sample(all_files, num_to_draw)
            except ValueError:
                to_play = sample(all_files, len(all_files))

            file_list += to_play

        shuffle(file_list)
        for filename in file_list:
            print filename
            pygame.mixer.music.load(filename)

        pygame.mixer.music.play(-1)
