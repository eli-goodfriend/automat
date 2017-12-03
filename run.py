"""
main runner for automat
"""
from src.create import Creator

def run_automat():
    """
    run automat:
    - listen for RFID tag signal
    - when a signal comes in, execute its command
    - wait until get a new command
    """
    current_setting = 'DoNothing'
    while True:
        setting = raw_input('Setting:')
        if setting!=current_setting:
            creator = Creator(setting)
            creator.create()
            current_setting = setting

if __name__=="__main__":
    run_automat()
