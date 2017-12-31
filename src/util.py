"""
utilities for interfacing with room controls
"""
import os
import time
from random import shuffle, sample
from multiprocessing import Process

import pygame

class Sound(object):
    """
    utilities for playing sounds
    """
    @staticmethod
    def play_sound_from_list(file_list):
        """
        make a playlist from a list of sound files and play it, in order
        should be run in a subprocess to not block the rest of the program
        """
        pygame.mixer.init()
        for idx, filename in enumerate(file_list):
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play(0)
            # TODO this works but it's janky
            # pygame isn't really designed to make playlists, since its queue
            # only holds one file
            while True:
                time.sleep(1)
                if not pygame.mixer.music.get_busy():
                    break

    @staticmethod
    def play_sound_from_file(sound_file):
        """
        play one sound file, once
        assumes sound_file actually is a sound file
        """
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play(0)
        # keep the process alive
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    @staticmethod
    def play_sound_from_dir(sound_dir):
        """
        play all files in sound_dir once through
        assumes everything in the directory is a sound file
        """
        # TODO loop?
        all_files = os.listdir(sound_dir)
        all_files = [os.path.join(sound_dir, filename) for filename in all_files]
        shuffle(all_files)
        p = Process(target=Sound.play_sound_from_list, args=(all_files,))
        p.start()
        return p

    @staticmethod
    def play_one_file(sound_dir):
        """
        pick one file from the directory and play it
        """
        all_files = os.listdir(sound_dir)
        all_files = [os.path.join(sound_dir, filename) for filename in all_files]
        file_to_play = sample(all_files, 1)[0]
        p = Process(target=Sound.play_sound_from_file, args=(file_to_play,))
        p.start()
        return p

    @staticmethod
    def play_sound_from_ratios(sound_dir, ratios, queue_factor=10):
        """
        generate a queue of files from subdirs of sound_dir, with ratios between files drawn
        from the different subdirs drawn from ratios

        ratios = {'subdir1': 1,
                  'subdir2': 3}
        to get 3x more files from subdir2 than subdir1

        queue_factor determines how many files are drawn
        in the above example, with queue_factor=10,
            10 files from subdir1
            30 files from subdir2

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
        p = Process(target=Sound.play_sound_from_list, args=(file_list,))
        p.start()
        return p
