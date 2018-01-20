"""
module to manage settings:
    - keeps track of what setting is active
    - swaps settings when input changes
"""
import os
from pyhocon import ConfigFactory

from src.environment import Environment
from src.util import Sound

class Manager(object):
    """
    converts a setting command to a room environment
    setting = the 10 digit code output by the RFID reader, used to label a group of commands
    configuration = the dictionary of environment specifications associated with each setting
    environment = an instance of the Environment class used to interface with devices
    """
    def __init__(self, config='./config'):
        conf = ConfigFactory.parse_file(config)
        self.settings = conf.get('settings').as_plain_ordered_dict()
        self.initial_setting = conf.get('initial_setting')
        self.data_dir = conf.get('data_dir', './')
        self.new_tag_sound = conf.get('sound_effects.new_tag', '')

        self.current_setting = self.initial_setting
        configuration = self.setting_to_configuration(self.current_setting)
        self.current_environment = Environment(configuration, data_dir=self.data_dir)

    def check_setting(self, setting):
        """
        check if setting has changed
        """
        if setting != self.current_setting:
            self.announce_new_setting()
            configuration = self.setting_to_configuration(setting)
            self.change_environment(configuration)
            self.current_setting = setting

    def setting_to_configuration(self, setting):
        """
        use config dict to convert between setting and configuration
        """
        try:
            configuration = self.settings[setting]
        except KeyError:
            configuration = self.settings[self.initial_setting]
        return configuration

    def change_environment(self, new_configuration):
        """
        destroy the previous environment and create the new environment
        """
        self.current_environment.destroy()
        self.current_environment = Environment(new_configuration, data_dir=self.data_dir)

    def announce_new_setting(self):
        """
        play sound so user knows a new setting is captured
        """
        announcement = os.path.join(self.data_dir, 'sound_effects', self.new_tag_sound)
        length = 2
        Sound.play_sound_effect(announcement, length)
