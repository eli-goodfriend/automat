"""
class to accept settings and create the specified room environment
"""
import importlib

class Creator(object):
    """
    converts a setting command to a room environment
    """
    def __init__(self, setting, setting_module='src.settings'):
        mod = importlib.import_module(setting_module)
        try:
            setting_class = getattr(mod, setting)
            self.creator = setting_class()
            print self.creator.__class__.__name__
        except AttributeError:
            print "{} is not a known setting".format(setting)
            self.creator = None

    def create(self):
        """
        call setting class create() method to implement settings
        """
        try:
            print self.creator.__class__.__name__
            self.creator.create()
        except AttributeError:
            print "No creator, so no implementation"
