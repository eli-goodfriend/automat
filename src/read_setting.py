"""
read settings from RFID
"""
import evdev

from pyhocon import ConfigFactory

class Reader(object):
    """
    read input setting from specific input device
    avoid having to keep cursor on terminal running automat
    """

    def __init__(self, config='./config'):
        reader = ConfigFactory.parse_file(config).get('reader')

        self.input_path = '/dev/input/event{}'.format(reader)
        self.device = evdev.InputDevice(self.input_path)
        self.device.grab()

        self.prefix = "KEY_"
        self.enter = "ENTER"

    def get_input(self):
        """
        receive input from reader event only
        return on enter
        """
	print("Waiting for code")
        code = []
        for event in self.device.read_loop():
            if event.type == evdev.ecodes.EV_KEY:
                key_event = evdev.categorize(event)
                if key_event.keystate == key_event.key_up:
                    key = key_event.keycode.replace(self.prefix, '')
                    if key == self.enter:
                        break
                    else:
                        code.append(key)
        code = ''.join(code)
        print(code)
        return code
