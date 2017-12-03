"""
classes that specify automated room settings
current task is to automate music, but other settings could be added, such as
color and intensity of light or turning on an aroma diffuser
"""

class Setting(object):
    """
    abstract parent of all setting classes
    """

    def create(self):
        """
        send signals to all room setting devices to implement setting
        """
        raise NotImplementedError('{} does not implement create()'
                                  .format(self.__class__.__name__))

class DoNothing(Setting):
    """
    default class: turn everything off
    """

    def create(self):
        print "do nothing"

class CodingWork(Setting):
    """
    settings to make the room suitable for coding work ;D
    """

    def create(self):
        print "coding work"
