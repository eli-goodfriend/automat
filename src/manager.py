"""
module to manage settings:
    - keeps track of what setting is active
    - swaps settings when input changes
"""
import importlib

from src.settings import DoNothing

class Manager(object):
    """
    converts a setting command to a room environment
    """
    def __init__(self, setting_module='src.settings'):
        self.settings_mod = importlib.import_module(setting_module)
        
        self.current_setting = DoNothing()
        self.current_setting.create()

    def check_setting(self, setting):
        """
        check if setting has changed
        """
        try:
            setting_class = getattr(self.settings_mod, setting)
            if not isinstance(self.current_setting, setting_class):
                self.change_setting(setting_class)
        except AttributeError:
            print "{} is not a known setting".format(setting)

    def change_setting(self, new_setting):
        """
        destroy the previous setting and create the new setting
        """
        self.current_setting.destroy()
        self.current_setting = new_setting()
        self.current_setting.create()
