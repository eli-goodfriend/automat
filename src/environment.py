"""
classes that specify automated room settings
current task is to automate music, but other settings could be added, such as
color and intensity of light or turning on an aroma diffuser
"""
import os

from src.util import Sound

class Environment(object):
    """
    manage all external devices according to input configuration
    """
    def __init__(self, configuration, data_dir='./'):
        self.name = configuration['name']
        self.data_dir = os.path.join(data_dir, self.name)

        self.processes = []

        self.init_sound(configuration)

    def init_sound(self, configuration):
        """
        initialize sound based on configuration
        """
        sound_dir = os.path.join(self.data_dir, 'sound_files')
        sound_type = configuration['sound_type']

        if sound_type == 'continuous':
            proc = Sound.play_sound_from_dir(sound_dir)
            self.processes.append(proc)
        elif sound_type == 'once':
            proc = Sound.play_one_file(sound_dir)
            self.processes.append(proc)
        elif sound_type == 'ratio':
            ratio = configuration['sound_ratio']
            proc = Sound.play_sound_from_ratios(sound_dir, ratio)
            self.processes.append(proc)
        elif sound_type == 'pandora':
            station_name = configuration['station_name']
            proc = Sound.play_pandora(station_name)
            self.processes.append(proc)
        else:
            print "Unknown sound type, not playing any sounds"

    def destroy(self):
        """
        send signals to all room setting devices to shut down setting
        """
        for proc in self.processes:
            proc.terminate()
            proc.join()
