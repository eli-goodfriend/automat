"""
by hand integration tests
"""
import os
import pygame

from src.util import Sound

class TestSound(object):
    """
    methods for hand testing Sound class
    """
    def __init__(self):
        self.test_dir = '/home/eli/Data/automat/test/sound_files/shorts'
        self.tests = ['test_play_sound_from_dir',
                      'test_play_sound_from_file'] # TODO there must be an automated way of doing this

    def run(self):
        print "Running tests"
        for test in self.tests:
            print "Running {}".format(test)
            test_fcn = getattr(self, test)
            test_fcn()

            go_on = raw_input("Start next test?")

    def test_play_sound_from_file(self):
        test_sound = 'marbles-daniel_simon.ogg' # TODO should choose randomly from dir
        sound_file = os.path.join(self.test_dir, test_sound)
        Sound.play_sound_from_file(sound_file)

    def test_play_sound_from_dir(self):
        Sound.play_sound_from_dir(self.test_dir)

class TestPandora(object):
    """
    methods for hand testing pandora interface
    """

    def __init__(self):
        self.station = "Flogging Molly Radio"

    def run(self):
        Sound.play_pandora(self.station)
